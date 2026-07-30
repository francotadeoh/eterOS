# 🧩 Scale OS

Un sistema operativo para tu negocio, adentro de Claude Code.

Le contás cómo funciona tu empresa, te hace una auditoría, y a partir de ahí trabaja con
**objetivos** en vez de con pedidos sueltos. Vos decís a dónde querés llegar; el sistema itera hasta
llegar, y **frena solo** en lo que no puede decidir por vos.

---

## El problema que resuelve

Cuando le pedís cosas a una IA de a una, cada conversación arranca de cero. Le explicás tu negocio
otra vez, hace algo razonable, cerrás la ventana y se pierde. Al mes siguiente estás igual.

Y hay un problema peor, más difícil de ver: **sin un criterio escrito antes de empezar, "listo" se
define al final, para justificar lo que ya se hizo.** Un resultado que corrió sin errores parece
correcto aunque esté mal.

Scale OS es la estructura mínima que arregla las dos cosas.

## La secuencia

```
onboarding → auditoría → skills → objetivos → loops
```

**Sin auditoría, los objetivos salen inventados.** Ese es el orden y no se saltea. Primero el
sistema entiende tu negocio, después diagnostica dónde está parado, después arma o reusa las
herramientas que hacen falta, después recibe tus objetivos, y recién ahí itera hasta cumplirlos.

## Las tres reglas

Todo lo demás es andamio. Estas tres son el sistema:

1. **Un objetivo es una definición de "listo" más una verificación que se corre, escrita antes de
   arrancar.** Y una diferencia sin causa no cuenta como explicada.
2. **Toda comprobación se corre también contra el escenario malo, y tiene que fallar ahí.** Si pasa
   en los dos, no está midiendo lo que dice medir.
3. **Un solo dueño por dato.** Nada se copia. Dos copias de un dato son dos verdades.

Están explicadas con ejemplos en
[`referencias/las-tres-reglas.md`](skills/scale-os/referencias/las-tres-reglas.md).

---

## 🚀 Instalación

**Copiá esta línea y pegásela a Claude Code:**

> Instalá Scale OS desde este repo y guiame para armar el sistema de mi negocio paso a paso:
> https://github.com/USUARIO/scale-os

Eso es todo. A partir de ahí te va a hacer preguntas sobre tu empresa, una por vez. Podés contestarle
**por audio** si te resulta más cómodo. No hace falta que edites archivos ni que escribas comandos.

> 💡 **Atajo técnico** (opcional): `npx skills add USUARIO/scale-os` y después decile a Claude
> *"armá el Scale OS de mi negocio"*.

### Qué necesitás

1. **Claude Code** (la app de escritorio sirve, no hace falta terminal).
2. Unos **20 a 40 minutos** para la primera vez, según cuánto quieras contarle.
3. Nada más. No hay que instalar bases de datos ni contratar servicios.

### Los dos perfiles

Es **un solo sistema** con dos profundidades. El onboarding te pregunta y elige por vos:

| | **PyME** | **Empresa / avanzado** |
|---|---|---|
| Para quién | dueño que es el cuello de botella de su propio negocio | equipo con procesos ya escritos |
| Onboarding | corto, sin jerga | completo, con inventario de sistemas |
| Objetivos a la vez | **uno** | varios, con loops encima |
| Primer entregable | la auditoría y un objetivo andando | la auditoría, el catálogo de procesos y los loops |

Si dudás, empezá en PyME. Subir de perfil después es una conversación, no una reinstalación.

---

## Qué te queda instalado

```
~/.claude/scale-os/
├─ README.md        el punto de entrada
├─ frenos.md        lo que el sistema NUNCA hace sin tu OK. Dueño único
├─ negocio.md       tu empresa, en las palabras del onboarding
├─ diagnostico.md   dónde está parado, salida de la auditoría
├─ objetivos/       uno por archivo, con su verificación escrita antes
├─ loops/           lo que se repite solo
├─ procesos/        cada proceso con su forma: archivo, skill, rutina o agente
└─ estado/          el estado de máquina, para que nada se pierda al cerrar la ventana
```

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

Todo vive en **tu máquina**, en `~/.claude/scale-os/`. Este repositorio es el instalador: no recibe
ni un dato tuyo. Si conectás herramientas externas, sus claves quedan en tu equipo.

---

Hecho para que un negocio pueda funcionar sin depender de que su dueño esté en todos lados.
Si te sirve, dejá una ⭐.
