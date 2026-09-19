# popusintes-esquematicos-placas

Parte de la tesis de Aarón Montoya-Moraga, en el Doctorado de Artes y Humanidades del Instituto de Estudios Avanzados de la Universidad de Santiago de Chile.

## Módulos

- [ataconso](./docs/ataconso.md)
- [parla](./docs/parla.md)
- [relo](./docs/relo.md)

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

[bloques](./bloques) contiene esquemáticos compartidos que se insertan como hoja jerárquica (hierarchical sheet) en otros proyectos de KiCad, en vez de duplicar los mismos componentes en cada módulo.

- [fuente-alimentacion](./bloques/fuente-alimentacion): conector eurorack 2x05, diodos Schottky de protección contra polaridad inversa en ±12V, y un regulador 7805 para obtener +5V.
- [salida](./bloques/salida): dos buffers de salida de audio (un TL072 completo, usando sus dos mitades A y B en configuración de seguidor de voltaje) con acoplo AC de entrada y salida, y jack de 3.5mm cada uno. Tiene dos entradas jerárquicas, `IN_A` e `IN_B`, una por canal. Si un módulo solo necesita una salida, se conecta solo `IN_A` (o `IN_B`) y se deja la otra sin conectar (con bandera de no conexión en el símbolo de hoja); el canal no usado simplemente no se puebla en la placa.

La [plantilla](./plantillas/kicad/plantilla-popusintes) ya incluye este bloque como hoja jerárquica, así que los módulos nuevos creados a partir de ella lo heredan automáticamente. Los módulos existentes (ataconso, parla, relo) todavía tienen su propia fuente de alimentación dibujada directamente en el esquemático.
