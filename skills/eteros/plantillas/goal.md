---
id: G-000
nombre: <una línea, en estado final>
estado: propuesto        # propuesto | activo | frenado | cerrado | abandonado
abierto: AAAA-MM-DD
cerrado:
duenio: <quién responde por esto>
proceso: <con qué proceso del catálogo se corresponde, si aplica>
---

# <nombre del objetivo>

## Por qué ahora

Dos o tres líneas: qué se destraba con esto y qué queda bloqueado si no se hace. Si no se puede
escribir, probablemente no sea prioritario todavía.

## Listo cuando

La definición de terminado, **verificable**. Si dos personas pueden discutir si está listo, está mal
escrita. Preferí números y estados observables antes que adjetivos.

- [ ] …
- [ ] …

## Reglas que aplican

**Punteros, no copias.** Copiar una definición adentro de cada objetivo es la forma más rápida de que
las dos se separen. Listá dónde están escritas, y abajo solo las reglas propias de este objetivo.

- …
- Propias de este objetivo: …

## Frenos propios

Los frenos del sistema se heredan de `frenos.md`. **No los copies acá.** Listá solo los propios de
este objetivo, si tiene alguno.

- …

## Verificación en vivo

**Lo que se corre.** Escrito acá **antes** de arrancar, no después. Leer un resultado no es
verificarlo.

No tiene por qué ser un comando. Sirve igual *"abrir tal página a las 9 y ver si el número del día
está, sin que lo haya puesto yo"*, siempre que se haga en vez de opinarse, pueda fallar, y dos
personas no puedan discutir el resultado. Los cuatro moldes están en `referencias/verificaciones.md`.

```
# el comando exacto, si lo hay
```

o, si no lo hay:

> **Qué se hace:** …
> **Dónde se mira:** …
> **Qué tiene que verse para estar listo:** …

**Control negativo:** contra qué versión vieja o qué escenario malo tiene que **fallar** esta
verificación. Sin terminal, casi siempre es el mismo: **apagalo y mirá que se rompa.** Si pasa en los
dos casos, el instrumento está desafinado y hay que arreglarlo antes de creerle al resultado bueno.

> Si no se te ocurre cómo verificar esto, esa es la señal de que el objetivo está mal planteado.
> No lo dejes pasar con un "revisar que esté bien".

## Evidencia

Se completa a medida que corre. Qué se corrió, cuándo, qué devolvió, dónde quedó.

| Fecha | Qué se corrió | Resultado | Dónde quedó |
|---|---|---|---|

## Preguntas abiertas

Lo que depende de una decisión que no podés tomar vos. Cada una dice **qué se hace mientras tanto**,
para que el objetivo no se frene entero por una pregunta.
