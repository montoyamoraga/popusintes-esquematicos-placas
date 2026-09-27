# popusintes-esquematicos-placas

Parte de la tesis de Aarón Montoya-Moraga, en el Doctorado de Artes y Humanidades del Instituto de Estudios Avanzados de la Universidad de Santiago de Chile.

## Módulos

- [ataconso](./docs/ataconso.md)
- [parla](./docs/parla.md)
- [relo](./docs/relo.md)
- [suma](./docs/suma.md)

## Desarrollo

Los esquemáticos y placas están hechos en KiCad. Para regenerar los BOM u otras exportaciones se usa un entorno virtual de Python:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

`env/` está en `.gitignore`, así que hay que crearlo localmente antes de correr herramientas como `kicad-cli` o `easyeda2kicad`.

## Bibliotecas

Las bibliotecas de KiCad (símbolos, huellas y modelos 3D) están en [bibliotecas](./bibliotecas):

- [byom](./bibliotecas/byom): biblioteca BYOM (símbolos, huellas y modelos 3D de terceros).
- [easyeda2kicad.kicad_sym](./bibliotecas/easyeda2kicad.kicad_sym), [easyeda2kicad.pretty](./bibliotecas/easyeda2kicad.pretty) y [easyeda2kicad.3dshapes](./bibliotecas/easyeda2kicad.3dshapes): símbolos, huellas y modelos 3D convertidos desde EasyEDA con `easyeda2kicad`.

Hay que agregar `bibliotecas` como ruta de biblioteca en KiCad (Preferencias → Administrar bibliotecas de símbolos/huellas) para que los esquemáticos y placas encuentren estas piezas.

## Bloques reutilizables

[popusintes.kicad_blocks](./bibliotecas/popusintes.kicad_blocks) es una biblioteca de bloques de diseño (design blocks) de KiCad 10: fragmentos de circuito que se copian dentro de cada módulo, en vez de enlazarlos como hoja jerárquica compartida. Cada módulo queda con su propia copia, congelada en la versión con que se fabricó, así que cambiar un bloque no altera las revisiones ya hechas.

- [fuente-alimentacion](./bibliotecas/popusintes.kicad_blocks/fuente-alimentacion.kicad_block): conector eurorack 2x05 y diodos Schottky de protección contra polaridad inversa en ±12V.

Para usarlos:

1. Registrar la biblioteca en Preferencias → Administrar bibliotecas de bloques de diseño. La [plantilla](./plantillas/kicad/plantilla-popusintes) ya trae una tabla de proyecto (`design-block-lib-table`) que apunta a `${KIPRJMOD}/../../bibliotecas/popusintes.kicad_blocks`, válida para proyectos ubicados en `<modulo>/<modulo>-v-X-rev-Y/`.
2. En el editor de esquemáticos, abrir el panel de bloques de diseño y colocar el bloque, ya sea en línea o como hoja (_place as sheet_).
3. Para agregar o actualizar un bloque, seleccionar el circuito en un esquemático y guardarlo en la biblioteca desde el mismo panel.

Los módulos que usaban la hoja compartida antigua ([suma-v-0-rev-a](./suma/suma-v-0-rev-a) y [ataconso-v-0-rev-c](./ataconso/ataconso-v-0-rev-c)) ahora tienen su propia copia de `fuente-alimentacion.kicad_sch` junto al proyecto. Parla y relo tienen la fuente de alimentación dibujada directamente en el esquemático.
