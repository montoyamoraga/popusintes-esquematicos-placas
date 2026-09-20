# relo

## Revisiones

- `rev-a`: en progreso, septiembre 2026.

## Esquemático y placa (rev-a)

Generados automáticamente por GitHub Actions a partir de `relo/relo-v-0-rev-a/relo-v-0-rev-a.kicad_sch` y `.kicad_pcb` en cada push que los modifica.

![Esquemático de relo rev-a](./images/relo-esquematico.svg)

![Placa de relo rev-a](./images/relo-placa.svg)

## Bill of materials (rev-a)

Generado a partir de `relo/relo-v-0-rev-a/relo-v-0-rev-a.kicad_sch`.

Esta revisión está en progreso: algunos componentes todavía tienen el valor por defecto de la biblioteca (`C_Polarized`) en vez de un valor real. Esta BOM es un punto de partida, no una lista final para comprar partes.

<!-- BOM_TABLE_START -->
| Referencias | Cantidad | Valor | Huella | Descripción |
| --- | --- | --- | --- | --- |
| C1, C2 | 2 | 1u | *(sin huella asignada)* | Capacitor electrolítico |
| C3, C4 | 2 | 100n | *(sin huella asignada)* | Capacitor cerámico |
| C5, C6 | 2 | C_Polarized | *(sin huella asignada)* | Capacitor electrolítico |
| D1, D2 | 2 | D_Schottky | *(sin huella asignada)* | Diodo Schottky |
| J1 | 1 | Conn_02x05_Odd_Even | relo-v-0-rev-a:IDC-Header_2x05_P2.54mm_Vertical | Header de alimentación Eurorack (10 pines) |
| J2, J3 | 2 | AudioJack2_SwitchT | relo-v-0-rev-a:Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical | Jack de audio 3.5mm |
| R1, R2 | 2 | 1k | *(sin huella asignada)* | Resistencia |
| R3, R5 | 2 | 10k | *(sin huella asignada)* | Resistencia |
| R4, R6 | 2 | 100k | *(sin huella asignada)* | Resistencia |
| RV1, RV2 | 2 | 470k | relo-v-0-rev-a:POT_TH_Alps_RK09K_Single_Vertical | Potenciómetro |
| U1 | 1 | NA556 | *(sin huella asignada)* | Temporizador doble 556 |
| U2 | 1 | TL072 | *(sin huella asignada)* | Amplificador operacional dual |

21 componentes en total. Los ítems marcados *(sin huella asignada)* todavía no están completos en el esquemático — hay que completarlos antes de generar gerbers o comprar partes para esta revisión.
<!-- BOM_TABLE_END -->
