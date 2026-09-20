#!/usr/bin/env python3
"""Regenera la tabla "Bill of materials" en docs/<modulo>.md a partir del
.kicad_sch correspondiente (ya incluye los bloques/ jerárquicos, kicad-cli
aplana la jerarquía solo).

Uso: python3 docs/generar_bom.py
Requiere kicad-cli (KiCad 10) en el PATH, o la variable de entorno KICAD_CLI
con el comando completo (por ejemplo, envuelto en "docker run ... kicad-cli"
como en .github/workflows/actualizar-capturas.yml).
"""
import csv
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Rutas relativas a REPO_ROOT: cuando KICAD_CLI envuelve un "docker run"
# (como en CI), el contenedor solo tiene montado REPO_ROOT como /work, así
# que tanto la entrada como el archivo temporal de salida deben pasarse
# como rutas relativas a ese directorio, nunca absolutas del host.
MODULOS = [
    ("ataconso", "ataconso/ataconso-v-0-rev-c/ataconso-v-0-rev-c.kicad_sch"),
    ("parla", "parla/parla-v-0-rev-c/parla-v-0-rev-c.kicad_sch"),
    ("relo", "relo/relo-v-0-rev-a/relo-v-0-rev-a.kicad_sch"),
    ("suma", "suma/suma-v-0-rev-a/suma-v-0-rev-a.kicad_sch"),
]

# lib_id ("Libreria:Nombre") -> descripcion en español, para la columna
# Descripción de la tabla. Si aparece un lib_id que no está acá, el script
# avisa por stderr y usa el lib_id tal cual como descripción de respaldo.
DESCRIPCIONES = {
    "Device:R": "Resistencia",
    "Device:R_Potentiometer": "Potenciómetro",
    "Device:C": "Capacitor cerámico",
    "Device:C_Polarized": "Capacitor electrolítico",
    "Device:D_Schottky": "Diodo Schottky",
    "Amplifier_Operational:TL072": "Amplificador operacional dual",
    "Amplifier_Audio:PAM8403D": "Amplificador de audio clase D",
    "Connector_Audio:AudioJack2_SwitchT": "Jack de audio 3.5mm",
    "Connector_Generic:Conn_02x05_Odd_Even": "Header de alimentación Eurorack (10 pines)",
    "Timer:NA556": "Temporizador doble 556",
    "Regulator_Linear:L7805": "Regulador de voltaje lineal +5V",
}

INICIO_MARCA = "<!-- BOM_TABLE_START -->"
FIN_MARCA = "<!-- BOM_TABLE_END -->"

KICAD_CLI = shlex.split(os.environ.get("KICAD_CLI", "kicad-cli"))


def exportar_bom(kicad_sch_rel: str) -> list[dict]:
    # kicad-cli no soporta escribir a stdout: "--output -" crea un archivo
    # literal llamado "-". Hay que darle un archivo real, y con ruta
    # relativa a REPO_ROOT (ver comentario de MODULOS arriba).
    tmp_name = f"_bom_tmp_{Path(kicad_sch_rel).stem}.csv"
    tmp_path = REPO_ROOT / tmp_name
    try:
        subprocess.run(
            [
                *KICAD_CLI, "sch", "export", "bom",
                "--output", tmp_name,
                "--fields", "Reference,Value,Footprint,QUANTITY,${SYMBOL_LIBRARY},${SYMBOL_NAME}",
                "--labels", "Refs,Value,Footprint,Qty,Lib,Name",
                "--group-by", "Value,Footprint",
                "--ref-range-delimiter", "",
                "--ref-delimiter", ", ",
                kicad_sch_rel,
            ],
            capture_output=True, text=True, check=True, cwd=REPO_ROOT,
        )
        with open(tmp_path, newline="") as f:
            return list(csv.DictReader(f))
    finally:
        tmp_path.unlink(missing_ok=True)


def generar_tabla(filas: list[dict]) -> str:
    lineas = [
        "| Referencias | Cantidad | Valor | Huella | Descripción |",
        "| --- | --- | --- | --- | --- |",
    ]
    total = 0
    for fila in filas:
        lib_id = f"{fila['Lib']}:{fila['Name']}"
        descripcion = DESCRIPCIONES.get(lib_id)
        if descripcion is None:
            print(f"[aviso] sin descripción para '{lib_id}', agregar a DESCRIPCIONES en generar_bom.py", file=sys.stderr)
            descripcion = lib_id
        valor = fila["Value"] or "*(valor sin definir)*"
        huella = fila["Footprint"] or "*(sin huella asignada)*"
        total += int(fila["Qty"])
        lineas.append(f"| {fila['Refs']} | {fila['Qty']} | {valor} | {huella} | {descripcion} |")
    lineas.append("")
    faltan_valor = any(f["Value"] == "" for f in filas)
    faltan_huella = any(f["Footprint"] == "" for f in filas)
    if faltan_valor or faltan_huella:
        lineas.append(
            f"{total} componentes en total. Los ítems marcados "
            + ("*(valor sin definir)*" if faltan_valor else "")
            + (" y " if faltan_valor and faltan_huella else "")
            + ("*(sin huella asignada)*" if faltan_huella else "")
            + " todavía no están completos en el esquemático — hay que completarlos antes de generar gerbers o comprar partes para esta revisión."
        )
    else:
        lineas.append(f"{total} componentes en total.")
    return "\n".join(lineas)


def actualizar_doc(nombre: str, tabla: str) -> None:
    doc_path = REPO_ROOT / "docs" / f"{nombre}.md"
    texto = doc_path.read_text()
    patron = re.compile(
        re.escape(INICIO_MARCA) + r".*?" + re.escape(FIN_MARCA), re.S
    )
    reemplazo = f"{INICIO_MARCA}\n{tabla}\n{FIN_MARCA}"
    nuevo_texto, n = patron.subn(reemplazo, texto)
    if n == 0:
        print(f"[error] no se encontraron las marcas {INICIO_MARCA}/{FIN_MARCA} en {doc_path}", file=sys.stderr)
        sys.exit(1)
    if nuevo_texto != texto:
        doc_path.write_text(nuevo_texto)
        print(f"actualizado: {doc_path}")
    else:
        print(f"sin cambios: {doc_path}")


def main() -> None:
    for nombre, kicad_sch in MODULOS:
        filas = exportar_bom(kicad_sch)
        tabla = generar_tabla(filas)
        actualizar_doc(nombre, tabla)


if __name__ == "__main__":
    main()
