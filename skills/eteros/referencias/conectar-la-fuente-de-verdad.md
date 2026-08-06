# Conectar la fuente de verdad

> **Dueño único de esta práctica.** El paso 2.5 del método apunta acá y no copia nada.
> Qué es la fuente de verdad y por qué manda ella está en `fuente-de-verdad.md`; acá está
> **cómo se conecta**, qué pasa cuando no se puede, y cómo se comprueba.

## Por qué existe este paso

Hasta acá el sistema sabe **dónde vive** la información del negocio. Saberlo y no estar ahí adentro
son cosas distintas: un sistema que guarda el estado en tu disco deja al equipo afuera y te vuelve,
otra vez, el único que sabe qué pasa. Ese es el problema que el sistema vino a resolver, así que no
puede terminar la instalación produciéndolo.

**La instalación no se da por cerrada sin una de estas dos cosas:** la herramienta conectada, o el
hueco escrito con nombre y motivo.

## Quién decide qué se conecta

**La auditoría, no una lista de herramientas disponibles.** `auditor-de-procesos-pyme` ya releva qué
usan y dónde vive hoy la información operativa. Esa respuesta es la recomendación.

| Lo que encontró la auditoría | Qué se conecta |
|---|---|
| ya usan una herramienta de gestión donde el equipo mira cómo va el negocio | **esa**, aunque no sea la que vos elegirías |
| usan varias y ninguna manda | la que tenga **lo que el equipo mira**, y se anota que hay dispersión |
| no usan ninguna: todo vive en la cabeza, en WhatsApp y en planillas sueltas | **Notion**, que es el caso base |

**No se propone cambiar de herramienta durante la instalación.** Migrar es un objetivo, no un paso de
onboarding. Si la que usan es mala, eso sale del diagnóstico y se trabaja después.

## La regla del botón

**Solo se ofrece conectar lo que entra con un botón.** Se aprieta, se aprueba en el navegador, y
listo.

**Si conectarla pide editar un archivo de configuración, escribir una clave o correr algo en una
terminal, no se ofrece: se declara el hueco y se sigue.** Sin excepciones, y sin "es fácil, te guío".

Por qué es una regla y no una preferencia: la persona que instala esto tiene un negocio, no un
equipo de sistemas. El día que la instalación le pide abrir un archivo de configuración, deja de ser
algo que se instala y pasa a ser un proyecto — y ahí se abandona. **Un hueco declarado es un
resultado; un hueco tapado es el problema original con mejor cara.**

## Cómo se hace, en la conversación

1. **Decí cuál y por qué**, en una línea y en las palabras de la persona:
   *"Lo que tu equipo mira para saber cómo va el negocio está en Notion. Vamos a conectarlo para que
   yo trabaje ahí adentro y no en una copia mía."*
2. **Pedí el botón, una sola vez y sin jerga.** Nombrá la herramienta, no la app desde donde está
   hablando, ni el protocolo, ni el formato. Si pregunta qué es, la respuesta es *"es el permiso para
   que yo pueda leer y escribir en tu Notion, igual que cuando conectás dos apps entre sí"*.
3. **Comprobalo vos leyendo algo real de ahí.** Esto no es opcional y es el paso que más se saltea.
4. **Escribí el resultado en `negocio.md`**, en el frontmatter, en la misma vuelta.

## Comprobar no es preguntar

**Que la persona diga que apretó el botón no es una conexión comprobada.** La comprobación es que
**vos leas algo de la herramienta y se lo muestres**: el nombre de una base, la cantidad de páginas,
el título de algo que ella reconozca.

> *"Listo: estoy viendo tu Notion. Tenés una base que se llama Clientes con 43 filas. ¿Es esa la que
> mira tu equipo?"*

Si no podés leer nada, **no está conectado**, diga lo que diga la pantalla. Volvé al punto 2 una vez
más; si tampoco, es un hueco.

## Cómo se escribe el resultado

En el frontmatter de `negocio.md`, siempre uno de los dos, nunca vacío:

```yaml
fuente_de_verdad: Notion
conexion: conectada          # comprobada leyendo de ahí
conexion_comprobada: 2026-08-05
```

```yaml
fuente_de_verdad: Tango Gestión
conexion: hueco              # no entra con un botón
conexion_motivo: no tiene forma de conectarse sin instalar y configurar algo a mano
conexion_comprobada: 2026-08-05
```

**`conexion: conectada` sin haber leído nada de la herramienta es una mentira del sistema sobre sí
mismo**, y es peor que el hueco: el hueco se ve y se trabaja, la mentira se descubre el día que el
equipo no encuentra lo que el sistema dijo que había guardado.

## Qué se hace con un hueco declarado

No se disimula y no frena la instalación:

1. **Decílo en una línea, sin culpa y sin tecnicismo.** *"Tango no se puede conectar apretando un
   botón, así que por ahora no voy a poder escribir ahí. Lo dejo anotado y seguimos."*
2. **Anotalo como deuda en `negocio.md`.**
3. **Seguí con lo que sí se puede.** Si hay una segunda herramienta del negocio que sí entra con un
   botón —el calendario, el drive, el mail—, ofrecé esa para lo que sirva, y decí para qué sirve y
   para qué no.
4. **Mientras haya hueco, el disco es la fuente de verdad provisoria** y se dice que es provisoria,
   con fecha. Un derivado con fecha de corte visible, nunca una segunda copia editable.

## El error que hay que evitar

**Ofrecer un catálogo.** "¿Qué querés conectar: Notion, Slack, Drive, Airtable?" convierte un paso de
diez segundos en una decisión que la persona no tiene con qué tomar, y termina eligiendo lo que le
suena en vez de donde está su información. **Una recomendación con motivo, y una sola.**
