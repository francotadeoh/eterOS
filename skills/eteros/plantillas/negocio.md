---
perfil: basico               # basico | empresa
fuente_de_verdad: disco      # disco | <nombre de la herramienta donde vive el estado del negocio>
conexion: pendiente          # conectada | hueco | pendiente | no-aplica
conexion_motivo:             # obligatorio si conexion es "hueco": por qué no entró con un botón
conexion_comprobada:         # AAAA-MM-DD del día que leíste algo real de la herramienta
fuente_del_sistema:          # solo si conexion es "hueco" Y aceptó abrir una al lado. Van los dos o ninguno
fuente_del_sistema_comprobada:   # AAAA-MM-DD. Se gana igual: leyendo algo real de ahí
objetivos_del_negocio:       # dónde viven, en la fuente de verdad. Vacío = todavía no se escribieron
maquinas: una                # una | varias. Con "varias" no se rehace el onboarding: se reconstruye
equipo_adentro: no           # no | sí. "sí" = alguien más que el dueño mira o trabaja en la herramienta
frenos_copia:                # solo con "varias" o "sí": dónde quedó la copia de referencia. Vacío = no hay
frenos_copia_fecha:          # AAAA-MM-DD. Sin fecha, la copia no sirve para comparar
actualizado: AAAA-MM-DD
---

# El negocio

> Escrito **en las palabras de la persona**, no traducido a lenguaje de consultor. Si más adelante no
> se reconoce leyéndolo, el onboarding falló.

## A qué se dedica

## A quién le vende, y qué problema le resuelve

## Qué hizo el dueño la semana pasada

Lo que hace **él solo**, no lo que hace el negocio. Y de la semana concreta que
contó, no de una promediada: el archivo se titula igual que se preguntó.

## De todo eso, qué preferiría no estar haciendo

## Con qué herramientas trabajan hoy

## Cuál es la fuente de verdad

En cuál de esas herramientas está lo que el equipo mira para saber cómo va el negocio.

**Si hay una, eterOS no la reemplaza: la ejecuta.** Ella es dueña del estado del negocio (clientes,
ventas, procesos, documentos) y el disco es dueño de los objetivos y del criterio. Ver
`referencias/fuente-de-verdad.md`.

Si no hay ninguna, el disco lo es por ahora. Anotarlo como deuda: un negocio con equipo la va a
necesitar.

## Cómo quedó la conexión

Una de dos, nunca vacío. Lo mismo que dice el frontmatter, en una frase:

- **Conectada** — y qué leíste de ahí para comprobarlo. *"Leí la base Clientes, 43 filas."*
- **Hueco** — y por qué no entró con un botón, más qué se hace mientras tanto.

Ver `referencias/conectar-la-fuente-de-verdad.md`. **Decir "conectada" sin haber leído nada de la
herramienta es el peor estado posible del sistema**: el hueco se ve y se trabaja; la mentira se
descubre el día que el equipo no encuentra lo que el sistema dijo que guardó.

## Quiénes entran, y desde dónde

Dos líneas, salidas de las dos preguntas del paso 3.

- **En cuántas computadoras trabaja.** Con más de una **no se rehace el onboarding en la segunda**:
  se conecta esta misma herramienta y se reconstruye desde ahí. No hay nada que copiar de una máquina
  a la otra, porque las dos leen del mismo lugar.
- **Si hay alguien más además del dueño.** El equipo **no instala nada**: mira y trabaja en la
  herramienta conectada. Si además alguien del equipo instala el sistema, hereda el negocio y el
  diagnóstico, y **los frenos los confirma, no los escribe**.

**Los frenos no se reconstruyen desde la herramienta**, a propósito: tienen que funcionar aunque la
conexión no responda. Si algún día las listas de dos máquinas no coinciden, se dice y decide la
persona; nunca se sincronizan en silencio. Ver `referencias/fuente-de-verdad.md`.

## A dónde va el negocio

**No se escribe acá.** Los objetivos viven en la fuente de verdad conectada, y en el frontmatter va
el puntero (`objetivos_del_negocio`). Ver `plantillas/objetivos-del-negocio.md`.

Si la conexión es un hueco, **las preguntas se hacen igual** y el resultado queda **donde vos ya
escribís** — tu planilla, tu documento, el mail que te mandás a vos mismo. En el frontmatter va el
puntero, diciendo que por ahora el sistema no los puede leer.

**Lo que no se hace es la copia local de consuelo:** un objetivo que solo vive en el disco de eterOS
es un objetivo que solo existe para una persona, y es exactamente lo que el sistema vino a evitar.

## Si el negocio funcionara dos semanas sin él, qué se rompe primero

> Esta es la respuesta más importante del onboarding. Es el diagnóstico, no un dato de color.

## Huecos

Lo que quedó sin responder. Anotarlo es mejor que trabar el onboarding esperándolo.
