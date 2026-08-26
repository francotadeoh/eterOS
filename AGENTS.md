# AGENTS.md — para el agente que trabaja sobre este repo

Si sos un agente de código y te toca editar eterOS, esto es lo primero que leés. **Con esta página
sola tenés que poder correr la verificación y decir dónde está la deuda.** Si algo de acá no
alcanza para eso, es un bug de este archivo.

El `README.md` de al lado **no es esto**: le habla a la persona que instala eterOS en su negocio.
Este le habla a quien edita el repo.

---

## Qué es este repo

**El método de eterOS, escrito como skills de Claude Code.** Un dueño de empresa dice "instalá
eterOS", y el sistema recorre 8 pasos con él: onboarding, auditoría, conectar la fuente de verdad,
frenos, formas, objetivos del negocio, primer objetivo, cierre.

Lo que se edita acá es **texto que un modelo va a leer en voz alta frente a una persona real que
pagó.** No hay build, no hay tests unitarios, no hay runtime. El producto es la letra.

## Qué NO es

- **No es una app.** No hay servidor, no hay dependencias, no hay `package.json`. Si estás por
  agregar un paso de build, pará y preguntá.
- **No es documentación de un producto que vive en otro lado.** Esto **es** el producto.
- **No es privado.** Ver los frenos.
- **No es el lugar de la deuda.** La deuda vive fuera del repo, en `~/.claude/eteros/`.

---

## Antes de tocar nada

```bash
_build/verificar.sh
```

Corre los gates —hoy nueve— cada uno en corrida normal y con `--controles`, y devuelve **un** estado.

**Si falla, pará.** No arregles encima de un rojo: primero se entiende qué mide el gate que se puso
en rojo. Un gate rojo antes de que empieces es un problema que ya estaba, y meterle un cambio arriba
mezcla tu error con el que ya había.

Los gates se descubren solos: cualquier `_build/V<n>-*.py` entra. Uno nuevo no se puede olvidar de
agregar, uno borrado no deja un nombre colgado.

**Y un gate puede declarar qué mide.** Si adentro dice `MIDE = "una instancia"`, su sujeto no es este
repo sino **la instalación que le quedó a una persona**, y en el agregado corren solo sus controles.
El agregado del repo contesta *"¿está sano el repo?"*; el rojo de la instancia de alguien contesta
otra cosa, y un rojo que significa dos cosas distintas se empieza a ignorar. Ese gate se corre
aparte, con la ruta de la instancia:

```bash
python3 _build/V8-instalacion-de-una-persona.py ~/.claude/eteros
```

### Los tres estados, y por qué el tercero gana

| Estado | Qué significa | Exit |
|---|---|---|
| limpio | miré todo y no encontré nada | `0` |
| encontré algo | miré todo y encontré esto | `1` |
| **no pude medir** | **no pude mirar** una parte | `2` |

**El `2` pisa al `1` y al `0`.** No es el máximo: gana siempre. Si un solo gate de siete no pudo
mirar su entregable, el conjunto sale `2` aunque los otros seis estén limpios. Un agregador que no
pudo leer una fuente y sale con `0` dice *"está todo bien"* cuando lo honesto es *"no vi"*, y **nadie
revisa un verde**. Está escrito en `skills/eteros/referencias/verificaciones.md`, que es el dueño
único de la regla.

El agregador tiene su propio control negativo, y se corre a mano sobre una copia del repo:

```bash
_build/control-negativo-verificar.sh
```

---

## Dónde vive cada cosa

| Ruta | Qué es |
|---|---|
| `skills/eteros/SKILL.md` | **el método.** Los 8 pasos, MODO RECONSTRUIR y MODO OPERAR |
| `skills/eteros/plantillas/` | los archivos que se copian **a la máquina de la persona** |
| `skills/eteros/referencias/` | el criterio que el método consulta. Un tema, un dueño |
| `skills/auditor-de-procesos-pyme/` | el paso 2. Lo activa el método |
| `skills/sistematizador-de-procesos/`<br>`skills/arquitecto-de-informacion/`<br>`skills/orquestador-de-skills/` | corren **después** del cierre. Ojo con el freno 3 |
| `_build/V<n>-*.py` | los gates. Cada uno trae sus controles negativos con `--controles` |
| `_build/V8-instalacion-de-una-persona.py` | el único que mira **una instalación de una persona**, no el repo. Se engancha en el paso 8 |
| `_build/control-negativo-verificar.sh` | el control negativo del agregador. Se corre a mano, sobre una copia |
| `_build/verificar.sh` | corre todos y devuelve un estado |
| `_build/RUNBOOK.md`, `_build/INVENTARIO.md` | cómo se construyó esto |
| `~/.claude/eteros/DEUDA-DE-PRODUCTO.md` | **el dueño único de la deuda.** Fuera del repo, a propósito: tiene notas de operación que no van a un repo público |
| `~/.claude/eteros/GOAL-*.md` | los GOAL de cada sesión de trabajo sobre el repo |
| `~/.claude/eteros/` (el resto) | **una instancia instalada**, la del dueño del repo. No es el repo: es un eterOS andando |
| `~/.claude/skills/` | **el sistema vivo.** Lo que corre de verdad cuando alguien escribe "instalá eterOS" en esta máquina |

### Lo que NO viaja con el repo

El `.gitignore` es **whitelist**: ignora todo (`/*`) y habilita a mano lo que sí es framework
genérico. Por eso `_build/` —los gates, el runbook, el inventario— **no está publicado**: tiene IDs,
nombres y números reales de empresas concretas. Si clonaste esto desde GitHub, **no tenés los
gates**: tenés el método.

**Consecuencia práctica, y muerde:** un archivo nuevo en la raíz **no entra al repo solo**. Lo
escribís, `git status` no lo muestra, y parece que no pasó nada. Si agregás uno que tiene que
publicarse, agregá su `!` al `.gitignore` — y ojo, **gitignore no acepta comentarios al final de la
línea del patrón**: el comentario queda pegado al patrón y el patrón deja de matchear.

---

## Los tres frenos, y ya se pagaron

No son recomendaciones. Los tres se aprendieron rompiendo algo.

**1 · El push lo autoriza el dueño del repo.** Commiteá todo lo que quieras. `git push` se pide.

**2 · El repo es público.** `github.com/francotadeoh/eterOS`. Nada del programa pago, ni precios, ni
nombres de participantes, ni datos de nadie. Antes de commitear algo con números adentro,
preguntate de quién son.

**3 · Sincronizar `~/.claude/skills/` es tocar el sistema vivo.** Ahí es donde el método atiende a
una persona real. Se hace con backup previo, y **el backup nunca va adentro de `~/.claude/skills/`**:
va a `~/.claude/eteros/backups-skills/`. Un backup ahí adentro queda registrado como **skill
invocable** — un eterOS viejo listo para atender a alguien. Ya pasó: uno estuvo **trece días**
activable sin que nadie lo notara.

> Y ojo con lo que NO se sincroniza. `sistematizador-de-procesos`, `arquitecto-de-informacion` y
> `orquestador-de-skills` en esta máquina los sirve el plugin `anthropic-skills:`, no
> `~/.claude/skills/`. **Lo que se les arregle en el repo no corre acá.** `V5` lo declara en
> amarillo. Copiarlos taparía el plugin en silencio: es decisión del dueño del repo, no tuya.

---

## La regla del control negativo

> **Un gate que no falla contra un caso malo conocido no es un gate.**

Vale para todo lo que se escriba acá, y es la razón por la que cada `V<n>-*.py` trae su
`--controles`: fabrica el caso malo, lo corre, y exige rojo. **Si el control no falla contra la
versión vieja, la verificación no sirve** — está midiendo el harness, no el producto.

Y lo mismo al revés: **el caso sano tiene que dar verde.** Un gate que da rojo contra una instancia
sana es un gate que nadie va a correr dos veces.

Corolario: **un modelo no es un gate.** "Un agente revisor que aprueba o rechaza" no es
determinístico y no falla contra un caso malo conocido. Un gate es un `.py` con exit code.

---

## Cómo se trabaja acá

1. **Un cambio por vuelta.** Nombralo antes de escribirlo.
2. **Grepealo en `skills/` entero antes de aplicarlo.** El error que originó `V4`: aplicar un cambio
   mirando solo el archivo que se tocaba, mientras otro archivo lo contradecía.
3. **Corré su verificación y su control negativo.**
4. **Anotalo en `DEUDA-DE-PRODUCTO.md` en el mismo turno en que lo cerrás.**
5. **Cerrá la vuelta solo con `_build/verificar.sh` en verde.**

**No arregles de paso.** Lo que aparezca y no sea del objetivo de la sesión va a la deuda.

---

## Dos cosas de la letra

**Se dice "empresarios", nunca "PyME".** Única excepción: citas textuales de otros. Grepealo antes
de entregar.

**Cero jerga en lo que la persona lee.** No tiene por qué saber qué es un skill, un loop ni un data
source. La regla vive en `skills/eteros/SKILL.md` y `V4` la vigila: si escribís jerga en un bloque
que el modelo lee en voz alta, el gate se pone en rojo. Está bien que se ponga.
