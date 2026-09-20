# docs

Documentación por módulo, incluyendo la lista de materiales bill of materials (BOM) de cada uno.

- [ataconso](./ataconso.md)
- [parla](./parla.md)
- [relo](./relo.md)
- [suma](./suma.md)

Cada BOM se generó leyendo el archivo `.kicad_sch` de la revisión más reciente del módulo (referencia, valor y huella de cada símbolo colocado en el esquemático). Si el esquemático cambia, hay que regenerar la tabla a mano o con una herramienta como `kicad-cli sch export bom`.
