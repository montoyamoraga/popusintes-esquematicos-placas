# ataconso

## Revisiones

- `rev-a`: experimento, no ha sido fabricado.
- `rev-b`: fabricado entre agosto y septiembre 2026, funcionó.
- `rev-c`: revisión activa (en desarrollo). Es la que se documenta abajo.

## Bill of materials (rev-c)

Generado a partir de `ataconso/ataconso-rev-c/ataconso-rev-c.kicad_sch`.

| Referencias | Cantidad | Valor | Huella | Descripción |
| --- | --- | --- | --- | --- |
| C1 | 1 | 10n | Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm | Capacitor cerámico |
| C2, C5, C6 | 3 | 100n | Capacitor_THT:C_Disc_D3.8mm_W2.6mm_P2.50mm | Capacitor cerámico |
| C3, C4, C8, C9, C10 | 5 | 100n | *(sin huella asignada)* | Capacitor cerámico |
| C7 | 1 | 1u | *(sin huella asignada)* | Capacitor electrolítico |
| D1, D2 | 2 | 1N5817 | Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal | Diodo Schottky |
| J1 | 1 | Conn_02x05_Odd_Even | *(sin huella asignada)* | Header de alimentación Eurorack (10 pines) |
| J2 | 1 | AudioJack2_SwitchT | *(sin huella asignada)* | Jack de audio 3.5mm |
| R1 | 1 | 10k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal | Resistencia |
| R2 | 1 | 1k | Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal | Resistencia |
| R3 | 1 | 100k | *(sin huella asignada)* | Resistencia |
| RV1, RV2 | 2 | 470k | Potentiometer_THT:Potentiometer_Piher_PT-6-V_Vertical | Potenciómetro |
| U1 | 1 | TL072 | *(sin huella asignada)* | Amplificador operacional dual |
| U2, U3 | 2 | NE555D | Package_DIP:DIP-8_W7.62mm_Socket_LongPads | Temporizador 555 |
| U4, U5 | 2 | MC78L05_SO8 | Package_SO:SOIC-8_3.9x4.9mm_P1.27mm | Regulador de voltaje lineal +5V |

24 componentes en total. Los ítems marcados *(sin huella asignada)* todavía no tienen footprint definido en el esquemático — hay que asignarlos antes de generar gerbers o comprar partes para esta revisión.
