# 🧩 eterOS

Un sistema operativo para tu negocio, adentro de Claude Code.

Le contás cómo funciona tu empresa, te hace una auditoría, y a partir de ahí trabaja con
**objetivos** en vez de con pedidos sueltos. Vos decís a dónde querés llegar; el sistema itera hasta
llegar, y **frena solo** en lo que no puede decidir por vos.

**A dónde va:** un equipo chico que rinde como uno gigante, y que sigue funcionando cuando vos no
estás.

---

## El problema que resuelve

Cuando le pedís cosas a una IA de a una, cada conversación arranca de cero. Le explicás tu negocio
otra vez, hace algo razonable, cerrás la ventana y se pierde. Al mes siguiente estás igual.

Y hay un problema peor, más difícil de ver: **sin un criterio escrito antes de empezar, "listo" se
define al final, para justificar lo que ya se hizo.** Un resultado que corrió sin errores parece
correcto aunque esté mal.

eterOS es la estructura mínima que arregla las dos cosas.

## La secuencia

```
onboarding → auditoría → conectar → frenos → skills → objetivos → loops
```

**Sin auditoría, los objetivos salen inventados.** Ese es el orden y no se saltea. Primero el
sistema entiende tu negocio, después diagnostica dónde está parado, después **se conecta a la
herramienta donde tu equipo mira cómo va el negocio** y **te pregunta qué no querés que haga nunca
sin avisarte**, después arma o reusa las herramientas que hacen falta, después recibe tus objetivos,
y recién ahí itera hasta cumplirlos.

**Conectar no se pospone para «cuando esté todo armado».** Un sistema que guarda el estado de tu
negocio en tu disco deja a tu equipo afuera, que es el problema que vino a resolver.

## Las tres reglas

Todo lo demás es andamio. Estas tres son el sistema:

1. **Un objetivo es una definición de "listo" más una verificación que se corre, escrita antes de
   arrancar.** Y una diferencia sin causa no cuenta como explicada.
2. **Toda comprobación se corre también contra el escenario malo, y tiene que fallar ahí.** Si pasa
   en los dos, no está midiendo lo que dice medir.
3. **Un solo dueño por dato.** Nada se copia. Dos copias de un dato son dos verdades.

Están explicadas con ejemplos en
[`referencias/las-tres-reglas.md`](skills/eteros/referencias/las-tres-reglas.md).

## Los cuatro principios

Las tres reglas dicen **cómo se trabaja**. Estos cuatro dicen **a dónde va el negocio**. Una regla
se cumple o no en cada objetivo; un principio se acerca o se aleja con los meses.

1. **Agencia total.** Cada persona opera con la capacidad de un equipo entero, porque tiene agentes
   que ejecutan por ella y contexto que no tiene que pedirle a nadie.
2. **Dependencia cero.** Entre personas y entre áreas. Si alguien se toma dos semanas, lo que se
   frena es una dependencia, y cada dependencia es un proceso que vive en una cabeza.
3. **Sistema de mejora continua.** Una capa transversal lee lo que pasa en toda la organización a
   través de la fuente de verdad y de las herramientas conectadas, y levanta la mano sola.
4. **Negocios minimalistas y descentralizados.** La menor cantidad de piezas que hace el trabajo, y
   sin el dueño ni los líderes en el medio de la operación.

El chequeo de fondo, el que engloba a los cuatro: **si el dueño se toma un mes, ¿qué se rompe?**

Están desarrollados en
[`referencias/los-cuatro-principios.md`](skills/eteros/referencias/los-cuatro-principios.md).

## Si tu negocio ya vive en una herramienta

**eterOS no la reemplaza: la ejecuta.** Si tu equipo ya trabaja en Notion, en Airtable, en una
planilla o en un CRM, esa herramienta sigue siendo la fuente de verdad de clientes, ventas, procesos
y documentos. eterOS es el brazo ejecutor: conecta, corre rutinas y automatiza lo que la
herramienta no puede.

Esto importa más de lo que parece. Un sistema que guarda el estado del negocio en archivos de tu
computadora deja al equipo afuera y te vuelve, otra vez, el único que sabe qué pasa. El reparto
completo está en
[`referencias/fuente-de-verdad.md`](skills/eteros/referencias/fuente-de-verdad.md).

---

## 🚀 Instalación

**Copiá esta línea y pegásela a Claude Code:**

> Instalá eterOS desde este repo y guiame para armar el sistema de mi negocio paso a paso:
> https://github.com/francotadeoh/eterOS

Eso es todo. A partir de ahí te va a hacer preguntas sobre tu empresa, una por vez. Podés contestarle
**por audio** si te resulta más cómodo. No hace falta que edites archivos ni que escribas comandos.

> 💡 **Atajo técnico** (opcional): `npx skills add francotadeoh/eterOS` y después decile a Claude
> *"armá el eterOS de mi negocio"*.

### Qué necesitás

1. **Claude Code** (la app de escritorio sirve, no hace falta terminal).
2. Entre **una hora y media y dos horas y media** para la primera vez. El grueso se lo lleva la
   auditoría de procesos, que sola declara 45 a 90 minutos según el tamaño del negocio.
   **No hace falta hacerlo de una sentada:** si cerrás y volvés otro día, retoma donde quedaste.
3. **Una cuenta gratis de Notion, solo si hoy no usás ninguna herramienta de gestión.** Es lo único
   de toda la instalación que hacés vos por fuera de aprobar un permiso, y por eso va dicho acá y no
   en el medio. Si ya usás Notion, Airtable, una planilla o un CRM, no hace falta: se conecta esa.
4. Nada más. No hay que instalar bases de datos, escribir comandos ni contratar servicios.

### Los dos perfiles

Es **un solo sistema** con dos profundidades. El onboarding te pregunta y elige por vos:

| | **PyME** | **Empresa / avanzado** |
|---|---|---|
| Para quién | dueño que es el cuello de botella de su propio negocio | equipo con procesos ya escritos |
| Onboarding | 7 preguntas, sin jerga | completo, con inventario de sistemas |
| Objetivos a la vez | **uno** | varios, con loops encima |
| Primer entregable | la auditoría y un objetivo andando | la auditoría, el catálogo de procesos y los loops |

Si dudás, empezá en PyME. Subir de perfil después es una conversación, no una reinstalación.

---

## El método viene adentro

eterOS no es solo la estructura: **trae los skills del método y te va diciendo cuál usar en cada
momento.** No te los tira todos juntos el primer día.

| Skill | Cuándo entra |
|---|---|
| **Auditor de procesos** | en la auditoría, para saber dónde estás parado de verdad |
| **Arquitecto de información** | solo si tu información está tan desordenada que no se puede sistematizar encima |
| **Sistematizador de procesos** | al escribir cada proceso, para sacarlo de tu cabeza |
| **Orquestador de skills** | cuando cerraste tu primer objetivo, para que empieces a **construir los tuyos** |

Ese último es el que cierra el círculo. Hasta ahí usaste herramientas que ya existían; a partir de
ahí construís las propias, para lo que tu negocio necesita y nadie más, y las enganchás a tus
objetivos y a tus loops. Ese es el momento en que el sistema deja de ser algo que te instalaron y
pasa a ser tuyo.

## Qué te queda instalado

```
~/.claude/eteros/
├─ README.md        el punto de entrada
├─ frenos.md        lo que el sistema NUNCA hace sin tu OK. Dueño único
├─ negocio.md       tu empresa, en las palabras del onboarding
├─ diagnostico.md   dónde está parado, salida de la auditoría
└─ estado/          el estado de máquina, para que nada se pierda al cerrar la ventana
```

**Tus objetivos y tu catálogo de procesos no quedan acá: quedan en la herramienta conectada**, que
es la que mira tu equipo. Este disco guarda el criterio y el estado; el estado del negocio vive
donde tu gente lo puede ver. Solo si la conexión quedó en hueco aparece un `procesos/catalogo.md`
local, y el sistema te dice que es provisorio.

## Los frenos

El sistema para y te pregunta antes de cualquier cosa **irreversible o que salga hacia afuera**:
publicar algo, mandarle un mensaje a una persona, escribir sobre datos de clientes, cambiar precios,
borrar algo. El onboarding te deja armar tu propia lista, y esa lista tiene **un solo dueño**:
`frenos.md`. No se copia a los objetivos, se hereda.

## Alcance y límites

- **Sirve para** ordenar procesos, sostener objetivos en el tiempo, decidir qué automatizar y
  verificar que lo automatizado hace lo que dice.
- **No sirve para** reemplazar tu criterio comercial. Todo lo que es decisión de negocio (precio, a
  quién le hablás, qué ofrecés) se frena y te lo pregunta. Un sistema que itera solo sobre decisiones
  que no puede verificar gira en falso.
- **No manda mensajes ni publica nada** por su cuenta. Nunca.

## Privacidad

Todo vive en **tu máquina**, en `~/.claude/eteros/`. Este repositorio es el instalador: no recibe
ni un dato tuyo. Si conectás herramientas externas, sus claves quedan en tu equipo.

---

Hecho para que un negocio pueda funcionar sin depender de que su dueño esté en todos lados.
Si te sirve, dejá una ⭐.
