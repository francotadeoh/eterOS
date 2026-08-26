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

## Cuando hay más de una máquina, o entra el equipo

El reparto de arriba ya resuelve casi todo esto, y conviene decirlo porque no se ve: **si el estado
del negocio vive en la herramienta, dos computadoras no se sincronizan entre ellas — las dos leen del
mismo lugar.** No hay nada que copiar de una a la otra y no hay una que sea la buena. La pregunta
*"¿cómo mantengo iguales mis dos computadoras?"* no se contesta: se disuelve.

**Lo que no viaja es el criterio del sistema.** `negocio.md`, `diagnostico.md`, `frenos.md` y el
estado viven en el disco de cada máquina. Ahí aparecen los dos casos reales.

### La segunda máquina de la misma persona

**No se rehace el onboarding.** Volver a contestar las siete preguntas produce un segundo diagnóstico
que no coincide con el primero, y a partir de ahí hay dos versiones del mismo negocio sin que ninguna
esté marcada como vieja.

Se instala, se conecta **la misma** fuente de verdad, y el criterio se reconstruye leyendo de ahí.
Eso es MODO RECONSTRUIR y ya existe. Lo que la segunda máquina escribe en disco es **derivado, con su
fecha de corte visible**, igual que cualquier otro derivado.

### Los frenos son la excepción, y es a propósito

**`frenos.md` no se reconstruye desde la herramienta y sigue siendo dueño único en cada máquina.** Un
freno tiene que funcionar cuando la conexión no responde. Si la última barrera del sistema depende de
poder leer algo por internet, no es una barrera: es una barrera con horario.

Pero **dos máquinas con frenos distintos es peor que no tener frenos**, porque la persona cree que
tiene una lista y tiene dos. Entonces:

1. La fuente de verdad guarda **una copia de referencia con fecha**. De referencia, no dueña.
2. Al arrancar, **se comparan**.
3. **Si difieren, se dice y se pregunta.** Nunca se sincroniza en silencio y nunca gana el más nuevo.
   Un freno que aparece o desaparece solo es exactamente lo que la lista vino a impedir.

### Cuando entra el equipo

**El equipo no necesita instalar nada.** Trabaja en la herramienta, que es donde el sistema escribe.
Esa es la razón de fondo por la que el paso 3 no se saltea: no es una preferencia técnica, es lo que
hace que el equipo esté adentro.

**Si además alguien del equipo instala el sistema**, es el caso de la segunda máquina con una
diferencia: hereda el negocio y el diagnóstico, y **los frenos los confirma, no los escribe**. Los
frenos son de quien responde por el negocio.

Y el contrato de datos gana una fila: **quién escribe qué, desde dónde**. Dos personas con el mismo
sistema escribiendo sobre el mismo campo es la regla 3 fallando, y no se nota hasta que un número
cambia sin que nadie lo haya cambiado.

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
