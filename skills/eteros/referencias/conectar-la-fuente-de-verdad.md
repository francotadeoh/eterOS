# Conectar la fuente de verdad

> **Dueño único de esta práctica.** El paso 3 del método apunta acá y no copia nada.
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
| usan varias y ninguna manda, pero el equipo mira alguna | la que tenga **lo que el equipo mira**, y se anota que hay dispersión |
| usan varias y **el equipo no mira ninguna**: todo se lo preguntan al dueño | **Notion**, y se dice que las otras siguen donde están |
| no usan ninguna: todo vive en la cabeza, en WhatsApp y en planillas sueltas | **Notion**, que es el caso base |

**La tercera fila es la más común y la que más se confunde con la segunda.** Tener ocho herramientas
no es tener una fuente de verdad: si lo que el equipo hace para saber cómo va el negocio es
preguntarte a vos, no hay ninguna que mande, y elegir «la menos mala» de las ocho es inventar una
autoridad que nadie le reconoce. En ese caso se trabaja con **una sola**, y **se dice explícitamente
que las otras siguen donde están y que nadie tiene que mudar nada hoy** — que es el miedo real de
alguien que ya se paralizó una vez mapeando.

**Si Notion ya es una de las que usa, se conecta esa. No se abre otra.** Es el caso más común de esta
fila: la tiene, la abrió alguna vez, quedó a medias. Ahí adentro está su historia, y abrirle una
segunda es dejarle nueve herramientas en vez de ocho. Se conecta la que tiene y se dice que arranca
ordenándola.

**No se propone cambiar de herramienta durante la instalación.** Migrar es un objetivo, no un paso de
onboarding. Si la que usan es mala, eso sale del diagnóstico y se trabaja después.

**Abrir una donde no había ninguna no es cambiar de herramienta**, y no cae en esta regla. Cambiar es
sacarle a alguien la que ya usa; esto es darle un lugar al estado del negocio que hoy no está en
ningún lado.

## La regla del botón

**Si la herramienta ya está conectada en esta sesión, no se pide ningún botón.** Se comprueba
leyendo algo real de ahí y se escribe `conexion: conectada` con la fecha. Pedirle que apriete un
botón que ya apretó es hacerle dudar de algo que funciona, y escribirle `conexion: hueco` a una base
que estás leyendo es una mentira del sistema sobre sí mismo, con el agravante de que la desmiente la
pantalla. **Esta regla decide qué se *ofrece*, no qué se hace con lo que ya entró.**

**Solo se ofrece conectar lo que entra con un botón.** Se aprieta, se aprueba en el navegador, y
listo.

**Si conectarla pide editar un archivo de configuración, escribir una clave o correr algo en una
terminal, no se ofrece: se declara el hueco y se sigue.** Sin excepciones, y sin "es fácil, te guío".

Por qué es una regla y no una preferencia: la persona que instala esto tiene un negocio, no un
equipo de sistemas. El día que la instalación le pide abrir un archivo de configuración, deja de ser
algo que se instala y pasa a ser un proyecto — y ahí se abandona. **Un hueco declarado es un
resultado; un hueco tapado es el problema original con mejor cara.**

## Los dos huecos no se tratan igual

> **Acá se decide.** Las dos secciones de abajo cuentan el cómo de cada uno y no repiten esta tabla.

**Hay dos motivos para terminar en hueco, y lo que se hace después es distinto.** Confundirlos es
insistirle a alguien que ya te puso un límite:

| El hueco es de… | Qué pasó | ¿Se ofrece abrir una segunda al lado? |
|---|---|---|
| **la herramienta** | no entra con un botón, o no pudiste leer nada | **Sí, una vez.** El problema es técnico y la persona no dijo que no a nada |
| **la persona** | no quiere dar el acceso | **No.** Ofrecerle abrir otra es pedirle otro acceso: es insistir con otro nombre |

Con el hueco de la persona **no hay plan B en la misma conversación, y buscarlo es el error.** Se
vuelve a ofrecer recién cuando haya visto algo funcionando, en otra sesión.

## Cómo se hace, en la conversación

1. **Decí cuál y por qué**, en una línea y en las palabras de la persona:
   *"Lo que tu equipo mira para saber cómo va el negocio está en Notion. Vamos a conectarlo para que
   yo trabaje ahí adentro y no en una copia mía."*
2. **Pedí el botón, una sola vez y sin jerga** —y solo si hace falta pedirlo: **si ya está conectada,
   saltá directo al punto 3.** Nombrá la herramienta, no la app desde donde está hablando, ni el
   protocolo, ni el formato. Si pregunta qué es, la respuesta es *"es el permiso para que yo pueda
   leer y escribir en tu Notion, igual que cuando conectás dos apps entre sí"*.
3. **Comprobalo vos leyendo algo real de ahí.** Esto no es opcional y es el paso que más se saltea.
4. **Escribí el resultado en `negocio.md`**, en el frontmatter, en la misma vuelta.

### Las dos objeciones del caso base, contestadas

Cuando la recomendación es Notion porque no había ninguna herramienta, aparecen siempre las mismas
dos. Van contestadas en una línea, sin vender nada:

- **"¿Otra suscripción más?"** — *"Es gratis para esto. No hay que pagar nada."* La persona que
  llega sin herramienta de gestión suele ser la que ya se quemó pagando cosas que no usa: si la
  primera respuesta no es el precio, no escucha la segunda.
- **"No tengo cuenta."** — Se le dice que hace falta abrir una, **antes de pedirle nada**, y se cuenta
  como lo que es: **el único costo de la instalación que no es apretar un botón.** No se disimula
  diciendo "es un minuto". Ver *Cuando hay que abrir una cuenta*, abajo.

## Cuando la persona no quiere dar el acceso

**Es un caso distinto de la regla del botón, y termina distinto.** La regla del botón habla de
herramientas que no se pueden conectar. Acá la herramienta entra perfecto: **la persona no quiere.**

Pasa, y pasa con la que más tiene para ganar: alguien que ya tuvo un problema con un acceso, o que
maneja plata o datos de otros y decidió hace rato no repartir permisos.

1. **No se insiste.** Una sola vez, y se acepta a la primera. La instrucción de volver a pedir el
   botón —*"volvé al punto 2 una vez más"*— es para cuando **vos** no pudiste leer nada, nunca para
   cuando la persona dijo que no. Insistirle a alguien que puso un límite es la forma más rápida de
   perder la instalación entera, y el límite es suyo.
2. **Se dice qué se pierde, sin dramatizar, y se sigue.** *"Perfecto. Entonces por ahora yo no voy a
   poder escribir donde tu equipo lo vea: lo que armemos queda en mi lado. Lo dejo anotado y seguimos."*
3. **Se escribe con su motivo propio**, que **no** es el de la regla del botón:

```yaml
conexion: hueco
conexion_motivo: la persona prefiere no dar accesos
```

**Escribir "no entró con un botón" acá es mentir en el archivo**, y es la clase de mentira que se
descubre tarde: dentro de dos meses alguien va a leer ese `negocio.md`, va a creer que la herramienta
es el problema y va a salir a buscar un conector que no hacía falta.

4. **Se vuelve a ofrecer una sola vez más, y no en esta sesión.** Cuando la persona haya visto algo
   funcionando. Un acceso se da por confianza, y en el minuto tres de la instalación todavía no la hay.

## Cuando hay que abrir una cuenta

Si la herramienta recomendada es Notion y la persona no la tiene, **abrir la cuenta es parte de la
instalación y hay que decirlo antes**, no descubrirlo en el medio.

**Se declara como costo.** Instalar cuesta *0 comandos y 0 archivos editados* — eso sigue siendo
cierto y no se toca. Pero un alta no es ninguna de las dos cosas, así que no aparece en esa cuenta:
si no se dice aparte, el número publicado describe una instalación más barata que la real.

- **Se avisa antes de empezar el paso:** *"Para esto hace falta abrir una cuenta de Notion, que es
  gratis. Es lo único de toda la instalación que tenés que hacer vos por fuera de apretar un botón."*
- **Si no quiere abrirla, es un hueco** con su motivo, igual que arriba. No se negocia y no se
  insiste.

## Comprobar no es preguntar

**Que la persona diga que apretó el botón no es una conexión comprobada.** La comprobación es que
**vos leas algo de la herramienta y se lo muestres**: el nombre de una base, la cantidad de páginas,
el título de algo que ella reconozca.

> *"Listo: estoy viendo tu Notion. Tenés una base que se llama Clientes con 43 filas. ¿Es esa la que
> mira tu equipo?"*

Si no podés leer nada, **no está conectado**, diga lo que diga la pantalla. Volvé al punto 2 una vez
más; si tampoco, es un hueco. (Esa segunda vuelta es solo para este caso —vos no pudiste leer—, nunca
para cuando la persona dijo que no.)

### Conectada no quiere decir que adentro haya algo

Se comprueba que la conexión funciona, no que el contenido sirva. Es muy común que lo único que haya
del otro lado sea una base vieja que la persona abandonó hace un año: *"esa no la uso más"*.

**Eso es una conexión comprobada igual, y se escribe como tal.** Pero se dice en la misma línea, sin
que suene a reproche: *"Perfecto, entonces está conectado y vacío. Lo que armemos ahora arranca de
cero acá adentro."* Callarlo sale caro dos pasos después, cuando el catálogo de procesos aparezca en
un lugar que la persona creía lleno y no reconozca nada.

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

**Y si aceptó abrir una al lado, se escriben las dos.** `fuente_de_verdad` y `conexion` siguen
hablando **del negocio** —el hueco no se borra porque haya un plan B—, y dos campos más dicen dónde
vive lo del sistema:

```yaml
fuente_de_verdad: Tango Gestión          # el dueño de la facturación y el stock, en hueco
conexion: hueco
conexion_motivo: no entra con un botón
fuente_del_sistema: Notion               # donde viven los objetivos y el catálogo de procesos
fuente_del_sistema_comprobada: 2026-08-07
```

**Los dos campos van juntos o no van ninguno**, y el de la fecha se gana igual que el otro: leyendo
algo real de ahí. Sin fecha, `fuente_del_sistema` es la misma mentira que `conexion: conectada` sin
haber leído, con un nombre nuevo.

**No existe `fuente_del_sistema` con la del negocio conectada.** Si la del negocio entró, ahí adentro
vive todo: dos lugares para lo mismo es la regla 3 fallando.

**`conexion: conectada` sin haber leído nada de la herramienta es una mentira del sistema sobre sí
mismo**, y es peor que el hueco: el hueco se ve y se trabaja, la mentira se descubre el día que el
equipo no encuentra lo que el sistema dijo que había guardado.

## Qué se hace con el hueco de la herramienta

**Cuál de los dos huecos es esto está decidido arriba, en la tabla.** Para el de la persona, ver
*Cuando la persona no quiere dar el acceso*.

No se disimula y no frena la instalación:

1. **Decílo en una línea, sin culpa y sin tecnicismo.** *"Tango no se puede conectar apretando un
   botón, así que por ahora no voy a poder escribir ahí. Lo dejo anotado y seguimos."*
2. **Anotalo como deuda en `negocio.md`.**
3. **Ofrecé abrir una al lado, para lo del sistema.** Un ERP que no se conecta sigue siendo la fuente
   de verdad de lo suyo —facturación, stock, lo que ya vive ahí— y no se toca. Pero **el estado del
   sistema** (los objetivos del negocio, el catálogo de procesos, los objetivos abiertos) hoy no vive
   en ningún lado, y ese es el que el equipo necesita ver.

   *"Tu ERP sigue siendo el dueño de la facturación y del stock, no lo tocamos. Lo que te propongo es
   abrir un Notion al lado, solo para el mapa de procesos y los objetivos, que hoy no están en ningún
   lado. No hay que mudar nada."*

   **Esto no es cambiar de herramienta ni migrar**, y por eso no cae en la regla de más arriba: no se
   le saca nada a nadie, se le da un lugar a lo que no lo tiene. Si acepta, esa segunda queda como
   fuente de verdad **del sistema**, se comprueba igual que cualquier otra, y en `negocio.md` quedan
   las dos: la del negocio en hueco, y la del sistema conectada.

   **Si no acepta, el hueco queda entero y se sigue igual.** Se ofrece una vez.
4. **Nunca ofrezcas el drive, el mail o el calendario como fuente de verdad.** Entran con un botón y
   por eso tientan, pero un catálogo de procesos en un drive es una carpeta con archivos sueltos: es
   el problema original con otro nombre. Sirven para lo suyo —un archivo, una fecha— y para nada más.
5. **Mientras haya hueco entero, el disco es la fuente de verdad provisoria** y se dice que es
   provisoria, con fecha. Un derivado con fecha de corte visible, nunca una segunda copia editable.

## El error que hay que evitar

**Ofrecer un catálogo.** "¿Qué querés conectar: Notion, Slack, Drive, Airtable?" convierte un paso de
diez segundos en una decisión que la persona no tiene con qué tomar, y termina eligiendo lo que le
suena en vez de donde está su información. **Una recomendación con motivo, y una sola.**
