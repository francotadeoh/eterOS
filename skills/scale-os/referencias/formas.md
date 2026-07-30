# Las cuatro formas de un proceso

Cada proceso del negocio toma una de cuatro formas. Elegir mal no rompe nada de entrada: se nota
meses después, cuando algo que debería correr solo sigue esperando que alguien lo dispare.

**Criterio maestro, antes de elegir forma:** ¿esto es de las pocas cosas que **solo vos** podés hacer
y que además mueven el negocio? Si no lo es, se delega. La forma es *cómo* se delega.

| Forma | Cuándo | Quién lo dispara |
|---|---|---|
| **Archivo** | se consulta, no se ejecuta. Es referencia que una persona sigue | una persona, leyéndolo |
| **Skill** | se ejecuta a pedido, con criterio, y vos estás en la conversación | vos, pidiéndolo |
| **Rutina** | se repite en el tiempo **sin** que vos estés | el calendario |
| **Agente** | necesita juicio propio sostenido, o abarca más de lo que entra en una conversación | un evento, o él mismo |

**La regla que resuelve casi todo:**

> Si lo dispara el calendario, es **rutina**.
> Si lo dispara una persona, es **skill**.
> Si lo hace una persona, es **archivo**.
> Si necesita criterio propio sostenido en el tiempo, es **agente**.

## El error más común

Confundir **quién debería hacerlo** con **qué forma toma**. Son dos ejes distintos y hace falta
anotarlos por separado.

Decir "esto lo hace una máquina" no dice si esa máquina **arranca sola** o si **la tenés que
disparar vos cada vez**. Esa diferencia es la que separa un proceso delegado de uno que solo cambió
de manos.

Es un patrón frecuente: procesos que ya están construidos y funcionan, pero que alguien tiene que
acordarse de disparar. Pasarlos a rutina no es trabajo nuevo, es enchufarlos al calendario. Suele ser
el mejor retorno disponible, y es invisible mientras no separes los dos ejes.

## Cuándo NO conviene un loop

Un loop (un objetivo que itera solo) rinde cuando hay **estado vivo que se puede verificar** y
**muchas vueltas**. No rinde cuando:

- **No hay forma de verificar el resultado sin una persona.** Decisiones de negocio, precio, a quién
  le hablás. Ahí el loop gira en falso.
- **El trabajo es una sola pasada.** Ahí el loop solo agrega ceremonia.
- **El estado no se puede leer.** Si no podés mirar qué quedó, no podés cerrar la vuelta.
