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
