---
id: L-000
nombre: <qué persigue este loop>
estado: propuesto        # propuesto | corriendo | pausado | cerrado
objetivo: G-000          # un loop sin objetivo gira en falso
cadencia: <cada cuánto>
disparador: tiempo       # tiempo | evento:<cuál> | manual
abierto: AAAA-MM-DD
---

# <nombre del loop>

## Qué persigue

El objetivo `G-000`. Una línea de por qué hace falta iterar en vez de hacer una sola pasada.

> **Antes de armarlo, chequeá que corresponda.** Un loop rinde cuando hay estado vivo que se puede
> verificar y muchas vueltas. No rinde si el resultado no se puede verificar sin una persona (gira en
> falso), si el trabajo es una sola pasada (solo agrega ceremonia), o si el estado no se puede leer
> (no podés cerrar la vuelta).

## Qué hace cada iteración

Pasos concretos. Cada iteración tiene que dejar el sistema **mejor y guardado**, nunca a medio
camino.

1. Leer el estado.
2. …
3. Escribir el checkpoint y anotar qué pasó.

## Cuándo despierta

- **Cadencia:** …
- **Disparador de evento** (si aplica): qué cosa observable lo despierta antes de la cadencia.

## Cuándo para

Condición de salida **escrita**. Un loop sin condición de salida corre para siempre.

- Para solo cuando: …
- Para y pide OK cuando: …

## Log de iteraciones

| # | Fecha | Qué hizo | Qué resultó | Estado al cerrar |
|---|---|---|---|---|
