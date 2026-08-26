---
congelada_el:                # fecha en que se cerró esta foto. Se escribe UNA vez y no se toca
mes_medido:                  # el mes ya terminado del que salen las horas (ej: 2026-07)
filas_totales:               # cuántos procesos tenía el catálogo ese día
filas_medidas:               # cuántas con Calidad de las horas = medido
filas_a_ojo:                 # cuántas con estimado a ojo
filas_sin_medir:             # cuántas con no se pudo medir
horas_del_mes:               # la suma SOLO de las filas medidas. Nunca el total de todas.
                             # Si no hay ninguna fila medida, va "sin dato". NUNCA 0:
                             # 0 se lee como "no gastaba horas", que es otra cosa y es falsa
---

# Línea base — la foto del antes

**Esta foto se congela una sola vez y no se regenera.** Un "antes" que se re-escribe cada vez que
cambia el catálogo es un espejo del presente: siempre da cero horas devueltas, porque el antes se
mueve junto con el después.

**Si este archivo ya existe con `congelada_el` lleno, no lo pises.** No lo actualices, no lo
"refresques", no lo regeneres con datos nuevos. Si el catálogo cambió, eso se anota como movimiento
contra esta foto, no encima de ella.

**Si hace falta una foto nueva** —porque el negocio cambió tanto que la vieja no compara nada—, se
crea `linea-base-<fecha>.md` al lado y se dice en voz alta que la comparación arranca de cero desde
ahí. La vieja queda.

## La foto

| Proceso | Forma | Ejecutor hoy | Horas del mes medido | Calidad de las horas | Medido el | Estado |
|---|---|---|---|---|---|---|
| | | | | | | |

## Cuando no hay ninguna fila medida

Pasa, y es el caso de quien más horas tiene para devolver: no usa calendario, no tiene sistema, la
única superficie es su cabeza. **La foto se congela igual**, con `horas_del_mes: sin dato` y las filas
en `no se pudo medir`.

**Esa foto sirve.** No para contar horas, sí para contar **procesos**: quién los hace hoy y con qué
forma. Contra eso se mide "cambió de manos", que es la mitad de la regla y la que más importa.

## Qué se puede decir con esto, y qué no

- **Se puede** comparar cualquier medición futura contra estas filas, y declarar la causa de cada
  baja contra la lista cerrada del catálogo.
- **No se puede** anunciar un total de horas devueltas si `filas_sin_medir` es mayor que cero, ni si
  `filas_a_ojo` es mayor que `filas_medidas`. En esos casos se informan las filas por estado, no un
  número.
