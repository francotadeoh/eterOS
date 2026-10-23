# Los tres caminos

**Esta página es el dueño único de la regla de camino.** Cómo se elige, qué cambia entre uno y otro y
cómo se pasa de uno al siguiente se lee de acá. No se repite en otro lado.

Es **un solo sistema con tres puertas.** Las tres comparten lo de fondo: las tres reglas, los frenos
con dueño único, la verificación escrita antes y la carpeta de la instalación. Lo que cambia es **con
qué se arranca** y **qué hoja de ruta sigue**.

| | **Emprender** | **Empresarios** | **Corporativo** |
|---|---|---|---|
| Para quién | Todavía no emprendió, trabaja en relación de dependencia o está dando los primeros pasos. Arma sin equipo | Dueño que es el cuello de botella de su negocio | Un área o una empresa grande, con varias áreas y alguien que aprueba |
| La pregunta de fondo | ¿Qué negocio sale de vos? | ¿Qué se rompe si te vas un mes? | ¿Qué área opera con la capacidad de un equipo entero? |
| Arranca con | El skill `autoconocimiento` | El onboarding y la auditoría | — |
| Estado | Disponible | Disponible, con los perfiles de `perfiles.md` | **Todavía no está escrito** |

## Cómo se elige

Es la primera pregunta del paso 0, antes que cualquier otra:

> **"¿Hoy tenés un negocio funcionando, o estás por arrancar el tuyo?"**

- **Está por arrancar, o tiene algo que todavía no le deja ingresos** → **Emprender**.
- **Tiene un negocio funcionando** → **Empresarios**, y el paso 0 sigue con la pregunta de cuánta gente
  trabaja, que elige el perfil.
- **Lo instala para un área de una organización grande, y no es el dueño** → hoy entra a
  **Empresarios** con perfil `empresa`. Anotá en `negocio.md` que llegó por Corporativo. **No le
  ofrezcas un camino que no está escrito:** prometer algo que el sistema no cumple es peor que no
  ofrecerlo.

**Si ya existe `~/.claude/autoconocimiento/`, no lo preguntes de cero.** Usó el skill solo, antes de
instalar eterOS. Confirmalo en una línea —*"Veo que ya arrancaste a trabajar en tu diferencial.
¿Seguimos por ahí?"*— y si dice que sí es Emprender, y retoma donde quedó sin repetir nada.

**Si duda entre Emprender y Empresarios** —tiene un emprendimiento chico que factura poco—,
preguntá una sola cosa: *"¿Lo que querés ahora es ordenar lo que ya tenés, o encontrar qué querés
hacer?"*. Ordenar es Empresarios. Encontrar es Emprender.

## Dónde queda anotado

- **Emprender** escribe `~/.claude/eteros/hoja-de-ruta.md` en el paso 0, desde
  `plantillas/hoja-de-ruta.md`. Hace falta porque `negocio.md` recién se escribe varias sesiones
  después, y sin un rastro el que vuelve a la semana cae en el paso 1 de Empresarios.
- **Empresarios** no escribe hoja de ruta. Su camino es el campo `camino` de `negocio.md`.
  **Una instalación sin `hoja-de-ruta.md` y sin `camino` es Empresarios**: así quedan todas las
  instalaciones anteriores a esta versión, y no se les toca nada.

## La hoja de ruta de Emprender

| Etapa | Qué se hace | Quién lo hace |
|---|---|---|
| **A · Autoconocimiento** | Las cuatro fases: adentro, diferencial, público y primer camino | el skill `autoconocimiento` |
| **B · Tu negocio, escrito** | Se arma `negocio.md` desde lo que dejó la etapa A, sin volver a preguntar | este método |
| **C · Conectar** | El paso 3, igual que en Empresarios | este método |
| **D · Frenos** | El paso 4, con un freno más ya cargado | este método |
| **E · Tu primer objetivo** | El paso 7, con el objetivo que dejó escrito `primera-oferta.md` | este método |
| **F · Cierre** | El paso 8, con lo que no aplica dicho en voz alta | este método |

**Los pasos 2, 5 y 6 de Empresarios no aplican todavía.** No hay un negocio que auditar, ni procesos
que mapear, ni un año de facturación sobre el que poner números. Se saltean a propósito y se dice.
Cuando la persona ya cobra y quiere ordenar lo que armó, pasa a Empresarios (abajo) y ahí entran.

### A · Autoconocimiento

**Activá `autoconocimiento` y dejalo hacer las cuatro fases.** Tiene su propia regla de retomar y lee
y escribe en `~/.claude/autoconocimiento/`, que es la dueña de lo que la persona escribió sobre sí
misma. **No lo copies a `~/.claude/eteros/`**: se apunta, no se duplica.

Cada vez que cierra una fase, actualiza `fase` en `hoja-de-ruta.md` —de `A1` a `A2`, `A3`, `A4`— y
tilda lo que se cerró. Cuando cierra la 4 deja `fase: B`, y sigue la B.

### B · Tu negocio, escrito

Copiá `plantillas/negocio.md` con su frontmatter, con `camino: emprender` y `perfil: basico`, y
llenalo **leyendo** `~/.claude/autoconocimiento/`, no preguntando:

| Sección de `negocio.md` | Sale de |
|---|---|
| A qué se dedica | `primera-oferta.md` · qué ofrecés |
| A quién le vende, y qué problema le resuelve | `publico.md` |
| Qué hizo el dueño la semana pasada | `primera-oferta.md` · tus horas reales |
| Lo que preferiría no estar haciendo | `entrevista.md` · lo que te saca energía |
| Herramientas y fuente de verdad | **se pregunta**: es lo único que no está escrito |
| Qué se rompe si no está | **no aplica todavía**: escribilo así |

Mostráselo para que lo corrija. Marcá `[FALTA]` lo que no pudiste deducir y preguntá solo eso.

### D · El freno que ya viene cargado

Además de los que arme la persona, `frenos.md` de Emprender arranca con este, y se lo decís en una
línea:

> **Nunca te recomiendo renunciar, dejar un ingreso ni poner plata tuya.** Te puedo mostrar números y
> qué implica cada opción; la decisión es tuya y te la pregunto.

### E · El primer objetivo

**Ya está escrito**: es el de `primera-oferta.md`, con sus cuatro partes. Pasalo a `plantillas/goal.md`
sin reescribirlo y llevalo a la fuente de verdad, con la misma regla del paso 7. En `sirve_a`
escribí `primera-oferta`: en Emprender todavía no hay números del año, y el objetivo sirve a probar
la primera oferta.

### F · El cierre

El paso 8 se corre igual. De las cinco revisiones, en Emprender **aplican la 1 y la 4**. La 2 (línea
base), la 3 (catálogo) y la 5 (total de horas) **no aplican todavía** porque salen del paso 5, que no
corrió. **Decilo así, en una línea:** una revisión que no se corrió y no se nombra parece aprobada.

## La regla de retomar en Emprender

**Si existe `hoja-de-ruta.md` con `camino: emprender`, esta tabla reemplaza a la de RECONSTRUIR.**

| Lo que hay | Sigue |
|---|---|
| `hoja-de-ruta.md` con `fase` menor a `B` | **A** — el skill `autoconocimiento`, que sabe en qué fase quedó |
| `fase: B` y no existe `negocio.md` | **B** |
| `negocio.md`, con `conexion` en `pendiente` o vacía | **C** — el paso 3 |
| `negocio.md`, con `conexion` en `conectada` o `hueco`, y sin `frenos.md` | **D** — el paso 4 |
| `frenos.md` | **E** — el paso 7 |
| `estado/goals.json` | ya no es RECONSTRUIR: es **OPERAR** |

## Cómo se pasa de camino

**Es una conversación, no una reinstalación.** Igual que subir de perfil.

**De Emprender a Empresarios** cuando la persona ya cobró, cerró su primer objetivo y lo que quiere
ahora es ordenar lo que armó para que no dependa de ella. Cambiá `camino` en `negocio.md` a
`empresarios`, marcá `fase: graduada` en `hoja-de-ruta.md` y corré los pasos que no corrieron: el 2
(la auditoría, ahora de un negocio real), el 5 y el 6. **Lo que ya está escrito no se vuelve a
preguntar.**

## Qué NO cambia entre caminos

- Las tres reglas.
- Que la verificación se escribe **antes**.
- Que los frenos tienen dueño único y no se copian.
- Que el sistema no publica ni le escribe a nadie por su cuenta.
- Que sin diagnóstico los objetivos salen inventados. En Emprender el diagnóstico es el
  autoconocimiento: por eso la etapa A no se saltea.
