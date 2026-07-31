# La fuente de verdad, y el brazo ejecutor

Esta es la regla 3 (*un solo dueño por dato*) aplicada a la decisión más importante del sistema:
**dónde vive el estado de tu negocio.**

## El reparto

Si tu negocio ya vive en una herramienta de gestión (Notion, Airtable, una planilla, un CRM), **esa
herramienta es la fuente de verdad y no se discute**. eterOS no la reemplaza: la ejecuta.

| | **La fuente de verdad** | **El brazo ejecutor** |
|---|---|---|
| Qué es | tu herramienta de gestión | Claude Code |
| Es dueño de | el **estado del negocio**: clientes, ventas, procesos, tareas, documentos, informes | los **objetivos**, los loops y el criterio de verificación |
| Hace | guarda, muestra, comparte con el equipo | conecta herramientas, corre rutinas, automatiza lo que la herramienta no puede |
| Ante contradicción sobre un dato | **gana** | obedece |
| Ante contradicción sobre una definición | obedece | gana el **contrato de datos** (ver abajo) |

**Por qué así y no al revés.** Tu equipo trabaja en la herramienta, no en tu disco. Un sistema que
guarda el estado del negocio en archivos locales deja al equipo afuera y te vuelve, otra vez, el
único que sabe qué pasa. Eso es exactamente el problema que eterOS viene a resolver.

## Las tres reglas del reparto

1. **Si un dato define el estado del negocio, se persiste en la herramienta en el mismo turno.**
   Dinero, membresías, etapa de un cliente, proceso vigente. *Un cálculo que no queda escrito no
   existe.*
2. **Si la tarea es ejecutar contra sistemas externos, correr scripts o mover archivos, es del brazo
   ejecutor.** La herramienta no promete hacer eso.
3. **Toda decisión de negocio o cambio de esquema se registra con fecha en el contrato de datos.**

## El contrato de datos

Es el documento donde los dos sistemas se encuentran. Vive **en la fuente de verdad**, no en el
disco, porque tu equipo también lo lee. Define, como mínimo:

- **Quién manda sobre qué dominio.** Dinero, relación con el cliente, conversación: cada uno tiene un
  dueño distinto y los conflictos se resuelven por dominio, no por antigüedad del dato.
- **Las zonas de escritura.** Qué campos escribe una sincronización automática y cuáles escribe una
  persona. **La zona humana no se toca nunca**, ni siquiera para corregirla: es lo único que no se
  puede reconstruir.
- **La definición exacta de cada métrica**, con la fórmula. Si una métrica no está definida ahí, no
  se reporta.
- **Una línea base con fecha.** Contra esos números se valida cualquier cálculo nuevo. Si da
  distinto, el cálculo está mal, no la línea base.

> Escribir la línea base parece redundante hasta la primera vez que un cálculo nuevo da un número
> lindo y equivocado. Ahí es lo único que lo caza.

## El error que hay que evitar

**Mantener una copia local de una lista cuyo dueño es la herramienta.** Es cómodo el primer día y
miente el segundo, en cuanto alguien agrega una fila del otro lado.

Si necesitás algo en disco que ya vive en la herramienta, que sea **derivado y con fecha de corte
visible**, para que se note cuando está viejo. Nunca una segunda copia editable.

## Cómo se ve en la práctica

Un objetivo que calcula algo del negocio hace esto, en este orden:

1. **Lee** de la fuente de verdad. Solo lectura.
2. **Calcula** con las definiciones del contrato, recalculando desde los campos base en vez de leer
   una fórmula ya hecha. Si la fórmula estuviera mal, leerla directo escondería el error.
3. **Valida** contra la línea base. Cada número dice *coincide* o *difiere con causa nombrada*.
4. **Escribe el resultado como documento nuevo**, nunca encima de los datos vivos.
5. **Si apareció una decisión o una deuda, la registra con fecha** en el contrato, en el mismo turno.

Un sistema que audita no debería poder modificar lo que audita. Esa no es una limitación temporal:
es el diseño.
