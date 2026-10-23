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

**Emprender corre los mismos ocho pasos que Empresarios. Cambian dos y se adaptan otros dos.**

| Etapa | En Empresarios es | En Emprender | Quién lo hace |
|---|---|---|---|
| **A · Autoconocimiento** | el paso 1, el onboarding | las cuatro fases: adentro, diferencial, público y primer camino | el skill `autoconocimiento` |
| **B · Tu negocio, escrito** | el final del paso 1 | se arma `negocio.md` desde lo que dejó la etapa A, sin volver a preguntar | este método |
| **Paso 2** | la auditoría del negocio | **la auditoría de tu semana**: `referencias/tu-semana.md` | este método |
| **Paso 3** | conectar | igual | este método |
| **Paso 4** | frenos | igual, con un freno más ya cargado | este método |
| **Paso 5** | las formas de cada proceso | **tu equipo, siendo una persona**: `referencias/equipo-de-una-persona.md` | este método |
| **Paso 6** | los objetivos del negocio | igual, con el molde de abajo | este método |
| **Paso 7** | el primer objetivo | **ya viene escrito** de `primera-oferta.md` | este método |
| **Paso 8** | el cierre | igual, con las cinco revisiones | este método |

**Al cerrar cada paso, tildá su línea en `hoja-de-ruta.md`.** Es lo que la persona mira para saber
dónde está, y una hoja de ruta que no se mueve es una que deja de mirar.

**Sin la etapa A, el diferencial sale inventado, y sin el paso 2 las horas también.** Ninguno de los
dos se saltea, igual que la auditoría en Empresarios.

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
| Qué hizo el dueño la semana pasada | `primera-oferta.md` · tus horas reales. El paso 2 lo afina |
| Lo que preferiría no estar haciendo | `entrevista.md` · lo que te saca energía |
| Herramientas y fuente de verdad | **se pregunta**: es lo único que no está escrito |
| Qué se rompe si no está | **casi todo, y está bien**: el paso 2 dice qué podría seguir solo |

Mostráselo para que lo corrija. Marcá `[FALTA]` lo que no pudiste deducir y preguntá solo eso.
Cuando quede, poné `fase: sistema` en `hoja-de-ruta.md` y seguí con el paso 2.

### Paso 4 · El freno que ya viene cargado

Además de los que arme la persona, `frenos.md` de Emprender arranca con este, y se lo decís en una
línea:

> **Nunca te recomiendo renunciar, dejar un ingreso ni poner plata tuya.** Te puedo mostrar números y
> qué implica cada opción; la decisión es tuya y te la pregunto.

### Paso 6 · El molde para un proyecto que arranca

Las tres preguntas son las mismas. **La primera casi nunca sale como número de facturación**, porque
el proyecto todavía no factura: ofrecé este molde y que corrija.

> *"¿Sería algo como: en un año, mi proyecto me deja X por mes con Y clientes, y le dedico Z horas
> por semana?"*

Las tres cosas grandes van a tener *"yo"* como responsable tres veces. Está bien: anotalo así.

### Paso 7 · El primer objetivo

**Ya está escrito**: es el de `primera-oferta.md`, con sus cuatro partes. Pasalo a `plantillas/goal.md`
sin reescribirlo y llevalo a la fuente de verdad, con la misma regla del paso 7. En `sirve_a` va el
número del paso 6 al que sirve: casi siempre el de clientes.

## La regla de retomar en Emprender

**Si existe `hoja-de-ruta.md` con `camino: emprender`, primero mirá su `fase`:**

| `fase` | Sigue |
|---|---|
| `A1` a `A4` | **A** — el skill `autoconocimiento`, que sabe en qué fase quedó |
| `B` | **B** — armar `negocio.md` |
| `sistema` | **la tabla de RECONSTRUIR, tal cual**, desde `negocio.md` para abajo. El paso 2 es la auditoría de tu semana y el 5 es tu equipo, pero los rastros que dejan son los mismos archivos |
| `graduada` | ya pasó a Empresarios: la tabla de RECONSTRUIR, tal cual |

## Cómo se pasa de camino

**Es una conversación, no una reinstalación.** Igual que subir de perfil.

**De Emprender a Empresarios** cuando la persona ya cobró, cerró su primer objetivo y lo que quiere
ahora es ordenar lo que armó para que no dependa de ella. Cambiá `camino` en `negocio.md` a
`empresarios`, marcá `fase: graduada` en `hoja-de-ruta.md` y corré el paso 2 de Empresarios: la
auditoría, ahora de un negocio que existe. El diagnóstico nuevo va al lado del anterior, con fecha,
nunca encima. Lo demás ya está: el catálogo, la línea base y los
objetivos tienen el mismo formato en los dos caminos. **Lo que ya está escrito no se vuelve a
preguntar.**

## Qué NO cambia entre caminos

- Las tres reglas.
- Que la verificación se escribe **antes**.
- Que los frenos tienen dueño único y no se copian.
- Que el sistema no publica ni le escribe a nadie por su cuenta.
- Que sin diagnóstico los objetivos salen inventados. En Emprender el diagnóstico es el
  autoconocimiento más la auditoría de la semana: por eso ninguno de los dos se saltea.
