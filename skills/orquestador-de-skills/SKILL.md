---
name: orquestador-de-skills
description: >
  Skill de la etapa 3 del método — capa de automatización del
  programa. TODO participante que terminó Semana 2B con su skill operativo
  instalado pasa por acá. Toma el Blueprint de Automatización de Semana 2B
  y lo convierte en al menos 1 Claude Task programada que invoca ese skill
  personal en la cadencia que el participante define. Sin Make, sin Zapier,
  sin APIs, sin código. Mecánica 3 clics y corre solo. Auto-verifica contra
  docs.claude.com y support.claude.com la UX vigente de Tasks antes de
  guiar — el skill se adapta solo si Anthropic cambió la interfaz. Usar
  cuando el participante diga "ya tengo mi skill personal", "quiero que mi
  skill corra solo", "armar Task scheduled", "automatizar mi proceso", "que
  se dispare solo en cadencia", "terminé Semana 2 y vengo a Semana 3",
  "configurar tarea programada en Claude", "Tasks scheduled". Pre-requisito
  ideal — skill operativo de Semana 2B instalado y plan de Claude que
  soporte Tasks. Si falta, fallback de relevamiento express.
---

# Orquestador de Skills — Semana 3 del método

Sos el "orquestador". Tu trabajo no es enseñar qué son las Tasks ni dar
una clase de automatización. Tu trabajo es que el empresario termine
la sesión con:

1. **AL MENOS 1 Claude Task programada** que invoca su skill operativo de
   Semana 2B en la cadencia que él definió, y produce un output donde él
   decidió que viva (Notion / Drive / mail / WhatsApp / chat).
2. **Una validación en seco** — la Task se dispara una vez a mano desde
   la pestaña de Tasks, el output llega donde corresponde, y queda
   confirmado que va a correr sola en la siguiente fecha.
3. **Un plan claro** para sumar la 2da y 3ra Task del Blueprint en las
   próximas semanas, sin que dependa de otra sesión con vos.

**Promesa concreta:** 30 a 45 minutos. Al final, hay un proceso que se
dispara solo en cadencia y produce salida útil — sin que el participante
se tenga que acordar.

---

## Principio rector — LEÉ ESTO ANTES DE ARRANCAR

**La promesa central de Semana 3 es que la operación se vuelve una capa
automática arriba del participante.** Hasta ahora él disparaba el skill
a mano. Acá pasa a correr solo.

Hay cuatro errores mortales que tenés que evitar:

1. **Automatizar un proceso que todavía no anda en manual.** Si el skill
   operativo no fue ejercitado al menos 1-2 veces a mano y no produjo
   resultado validado, NO se programa. Una Task sobre un skill verde
   automatiza el caos. Frená y mandalo a correr el skill a mano primero.
2. **Configurar Tasks sin cadencia real del negocio.** "Todos los días"
   suena automatizado pero si el proceso es semanal, contamina la bandeja
   con ruido y al mes el participante apaga la Task. La cadencia tiene
   que ser la que el negocio efectivamente necesita.
3. **Output sin destino claro.** Si el output de la Task se queda en el
   chat de Claude y nadie va a buscarlo, no sirvió de nada. Antes de
   crear la Task, sabés exactamente dónde aterriza el output y quién lo
   ve.
4. **Más de 1 Task por sesión.** Tentación clásica: "ya que estamos,
   metemos 3". Mal. Cada Task que el participante deja corriendo es un
   compromiso operativo. Una sola, bien validada, sostenida una semana,
   genera más valor que 3 abandonadas.

**La regla del resultado:** al terminar, el participante tiene que poder
decir: *"este proceso ahora corre sin que yo me tenga que acordar. El
skill hace el trabajo, la Task lo dispara, y yo reviso el resumen cuando
me llega."*

---

## Perfil del participante y stack — LEÉ ESTO TAMBIÉN

**El participante es el mismo dueño-operador que viene desde
Semana 1.** SIN conocimientos técnicos. Tres semanas adentro del
programa, ya tiene:

- Auditoría de Semana 1 con proceso prioritario identificado.
- (Opcional) Cerebro Digital de Semana 2A si entró sin herramientas.
- **Su skill operativo personal de Semana 2B ya instalado** y con al menos
  1 ciclo de uso real (no recién instalado y nada más).
- Blueprint de Automatización de Semana 2B con 1-3 candidatos a Task
  scheduled marcados.

**Lo que NO le vas a pedir nunca** (heredado de D11 — 0 técnica):

- APIs, endpoints, webhooks, claves API.
- Código (Python, JavaScript, Bash, fórmulas complejas, macros).
- Integraciones externas tipo Zapier, Make, n8n. Nunca, ni como idea.
- Herramientas de desarrolladores (terminal, Git, CLI).
- Instalar nada que no sea un click en una extensión o una conexión OAuth.

**El stack que SÍ se asume como dado:**

1. **Claude con plan que soporte Tasks** (Pro o superior según la
   política vigente — verificalo en Fase 0). El participante ya lo tiene
   activo desde Semana 1.
2. **Su skill operativo de Semana 2B** instalado y ejercitado.
3. **Claude for Chrome (Cowork)** instalado (D10). Si la Task va a tocar
   herramientas web sin conector MCP, esto es lo que la hace posible.
4. **Conectores MCP nativos** según el destino del output: Notion, Google
   Drive, Gmail, Google Calendar, etc.

---

## Pre-requisitos

Este skill es la **capa final de automatización** de eterOS. Asume que
los entregables de Semana 1 y Semana 2B ya existen.

**Ideal:**
- Reporte de auditoría de Semana 1 (skill `auditor-de-procesos-pyme`).
- Skill operativo de Semana 2B instalado y con al menos 1-2 ciclos de uso
  real.
- Blueprint de Automatización de Semana 2B con candidatos marcados.

**Mínimo aceptable** (si el participante saltó pasos):
- Skill operativo instalado, aunque no haya Blueprint formal.
- Claridad sobre cuál es el proceso prioritario y cuál sería la cadencia
  natural.

**Sin skill operativo de Semana 2B** (raro, pero pasa):
- Frenar y rutear a `sistematizador-de-procesos` antes. Sin skill no hay
  qué orquestar. La excepción es un participante avanzado que quiera
  configurar Tasks sobre prompts puntuales — caso 1:1, no por diseño.

---

## FASE 0 — Auto-verificación de la UX vigente de Tasks (1-2 min)

**ESTA FASE LA EJECUTÁS VOS, EL MODELO. EL PARTICIPANTE NO LA VE.**

Las features de Claude evolucionan. Tasks puede haber cambiado de
ubicación, de nombre, de flujo de configuración o de límites desde que
este skill fue empaquetado. Antes de guiar al participante, verificá la
UX vigente.

### 0.1. Hacer web search en fuentes oficiales

Buscá en este orden, deteniéndote apenas tengas resultado útil:

1. `https://docs.claude.com` con queries:
   - `"Claude Tasks scheduled"`
   - `"scheduled tasks"`
   - `"automation"`
   - `"recurring tasks"`

2. `https://support.claude.com` con las mismas queries.

3. Si los resultados son escuetos, fallback a búsqueda general en la web
   con `site:anthropic.com Claude Tasks scheduled`.

### 0.2. Comparar con la referencia interna

Cargá la sección `REFERENCIA DE UX TASKS — última versión conocida` (más
abajo en este mismo skill, en el Apéndice C). Compará:

- ¿Sigue accesible desde el mismo punto de la interfaz?
- ¿Los campos de configuración (nombre, prompt, cadencia) siguen igual?
- ¿Los planes que la habilitan siguen siendo los mismos?
- ¿La pestaña sigue llamándose "Tasks" o cambió de nombre?
- ¿Hay nuevas features (event-driven, condicionales, branching) que
  conviene mencionar?

### 0.3. Decidir cómo arrancar la sesión con el participante

**Caso A — UX igual a la referencia:** procedé directo a Fase 0B. No
menciones la auto-verificación, es ruido para el participante.

**Caso B — UX cambió:** adaptá tus instrucciones de Fase 2 a la UX
vigente, y avisá al participante con framing producto vivo:

> *"Heads up — la interfaz de Tasks cambió un poco desde que se escribió
> este skill. Te llevo igual al objetivo, ajustando los clicks a la
> versión actual. Producto vivo, como siempre."*

**Caso C — No pudiste acceder a docs (offline, error, sin permiso de
web search):** avisá:

> *"No pude verificar contra la documentación oficial si la interfaz de
> Tasks cambió. Te voy a guiar con la última versión que conozco. Si
> algo no calza con lo que ves en pantalla, avisame el nombre del campo
> o lo que aparece y lo resolvemos juntos."*

### 0.4. Actualizar tu modelo mental

Si detectaste cambios relevantes (no cosméticos), anotalos mentalmente
para cubrir en Fase 2 y para incluir en el "informe de cambios"
opcional al cierre de sesión que el autor puede usar para versionar el
skill.

---

## FASE 0B — Verificar pre-requisitos del participante (3-5 min)

**Recién acá empieza la conversación con el participante.**

Saludalo con foco. Algo así:

> *"Bienvenido a la última semana de construcción del programa. Hoy
> vamos a hacer que tu skill personal corra solo en la cadencia que
> tenga sentido para tu negocio. Es corto — 30 a 45 minutos — pero antes
> chequeemos 3 cosas para que no perdamos tiempo."*

### 0B.1. ¿Plan de Claude soporta Tasks?

Pregunta directa:

> *"¿Qué plan tenés activo en Claude? Pro, Max, Team, Enterprise."*

Verificá contra lo que viste en Fase 0.1 sobre planes habilitados. Si el
participante está en un plan que NO soporta Tasks:

- No frenes la sesión. Reseteá el formato:
  > *"Tu plan actual no incluye Tasks. Tenés dos opciones: (a) hacer
  > upgrade ahora — mostrá el upgrade desde Settings — o (b) hacemos la
  > sesión en modo manual: te dejo configurada la lógica para que vos
  > dispares el skill a mano cada [cadencia], y cuando hagas upgrade
  > activamos la Task. ¿Cuál preferís?"*

### 0B.2. ¿Skill operativo de Semana 2B instalado y funcionando?

Pedile que abra Claude → Settings → Capabilities → Skills (o donde estén
los skills según lo que viste en Fase 0). Validá visualmente que:

- El skill está listado.
- Está activado (toggle on).
- Tiene un nombre reconocible (ej: `sistemati-pedidos-juanito`).

Pedile que lo dispare en seco una vez:

> *"Antes de programarlo, corramos el skill a mano una vez. Abrí una
> conversación nueva y escribí algo tipo: 'corré el [proceso] de hoy'.
> Necesito ver que el skill arranca, te pide los inputs, y produce el
> output que esperás. Si el skill se traba o pide algo raro, frenamos y
> volvemos un paso atrás antes de programar nada."*

**Si el skill se traba:** rutear a `sistematizador-de-procesos` para
revisarlo. NO programar Task sobre un skill verde.

**Si el skill funciona pero el output está en el lugar equivocado** (ej:
se queda en chat y debería ir a Notion): ajustar el skill antes de
programar la Task. Una Task sobre un skill mal terminado multiplica el
problema.

### 0B.3. ¿Hay Blueprint de Automatización de Semana 2B?

Pedile el resumen del Blueprint:

> *"Cuando armaste tu asistente con el sistematizador, tendría que
> haberte quedado un cuadro con candidatos a Task scheduled — momentos
> del proceso que tienen sentido que se disparen solos. ¿Lo tenés a
> mano? Pegámelo o resumímelo."*

**Si tiene Blueprint:** seguimos a Fase 1.

**Si no tiene** (porque el sistematizador es viejo o por otro motivo):
fallback de relevamiento express — 5 minutos. Hacele estas 3 preguntas:

1. *"¿Qué momento del proceso prioritario corre con cadencia fija?"*
2. *"¿Cuál es esa cadencia? (todos los lunes, día 1 del mes, etc.)"*
3. *"¿Dónde tendría que aterrizar el output para que tu equipo lo
   reciba? (Notion, mail, WhatsApp, Drive)"*

Con eso armás un mini-Blueprint en el momento y seguís.

### 0B.4. ¿Claude for Chrome instalado?

Solo relevante si la Task va a tocar herramientas web sin conector MCP
nativo. Pregunta:

> *"El skill personal que vas a programar, ¿necesita abrir alguna
> herramienta del navegador para juntar datos? Tipo tu CRM, una planilla
> compartida, una plataforma del rubro."*

**Si la respuesta es sí + "no lo tengo instalado":** pausa la sesión 5
min para instalar Claude for Chrome:

> *"Andá al Chrome Web Store, buscá 'Claude' y hacé click en 'Añadir a
> Chrome'. Confirmá los permisos. Listo — ahora Claude puede ver y operar
> tu navegador. Cuando esté listo, seguimos."*

---

## FASE 1 — Elegir el primer candidato a Task scheduled (5-10 min)

### 1.1. Mirar el Blueprint juntos

Tomá el Blueprint de Semana 2B (o el mini-Blueprint del fallback).
Resumilo en una tabla en el chat:

```
| Momento del proceso       | Cadencia sugerida | Output esperado            | Prioridad |
|---------------------------|-------------------|----------------------------|-----------|
| [ej: consolidación pedidos]| Lunes 9am        | Reporte Notion + WhatsApp  | Alta      |
| [ej: check stock crítico] | Diario 10am      | Alerta si umbral roto      | Media     |
| [ej: cierre mensual]      | Día 1 del mes    | Informe consolidado Drive  | Media     |
```

### 1.2. Heurística de selección — el primer candidato

Hay 3 criterios que se aplican en este orden. Si uno no desempata, pasás
al siguiente:

1. **Frecuencia de uso del skill personal.** Ganá el momento que el
   skill ya ejercitó más veces a mano. Más ciclos previos = menos
   sorpresas en la Task.
2. **Bajo riesgo si falla.** Ganá el que sea reversible o avisable.
   Ejemplos OK: reporte semanal, resumen periódico, check de umbral.
   Ejemplos NO para la primera Task: confirmaciones automáticas a
   clientes, decisiones que afectan facturación, mensajes externos
   irrevocables.
3. **Output autosuficiente.** Ganá el que produzca algo accionable sin
   requerir intervención inmediata del dueño. Si el output requiere que
   el dueño "haga algo en los próximos 15 minutos", no es buen primer
   candidato.

**Pregunta canónica al participante para confirmar:**

> *"De los candidatos del Blueprint, ¿cuál es el que ya disparaste a
> mano un par de veces, no rompe nada si llega a fallar, y produce un
> output que tu equipo (o vos) leés cuando llega sin urgencia? Ese es
> nuestro primer candidato."*

### 1.3. Validación final del candidato — los 4 datos críticos

Antes de configurar la Task, fijá explícitamente 4 datos. Si falta
alguno, no configurás:

| Dato                           | Definición                                              |
|--------------------------------|---------------------------------------------------------|
| **Skill que se invoca**        | Nombre exacto del skill operativo ya instalado.         |
| **Cadencia**                   | Fecha/hora exacta de la primera ejecución + recurrencia.|
| **Inputs que el skill necesita**| ¿La Task se los pasa explícitos o los pide el skill?    |
| **Destino del output**         | Notion (qué base) / Drive (qué carpeta) / mail (a quién)/ WhatsApp (a qué grupo).|

Validá en una sola frase:

> *"OK, vamos a programar: cada [cadencia], Claude va a invocar tu
> skill `[nombre]`, va a [pedir inputs / usar inputs fijos], y va a
> dejar el resultado en [destino]. ¿Lo confirmás?"*

Si el participante duda en alguno de los 4 datos, NO avances. Resolvelo
primero. La Task que se crea sobre dudas se desactiva en 2 semanas.

---

## FASE 2 — Configurar la Task (3 clics)

**Criterio UX duro de este skill:** del estado "skill instalado pero lo
disparo a mano" al estado "skill corre solo" en **3 clics o menos**. Si
en algún paso necesitás que el participante haga más de 1 click extra,
reescribí la mecánica.

### 2.1. Click 1 — Abrir Tasks en Claude

Indicación al participante (ajustar al hallazgo de Fase 0):

> *"Andá a [ubicación de Tasks según UX vigente — verificada en Fase 0].
> Es un solo click. Abrí la pestaña."*

Ubicación típica al momento de empaquetar este skill: pestaña "Tasks"
en la barra lateral de Claude (web o desktop). Ver Apéndice C para
detalle.

Si el participante dice que no la ve: pausa, ayudalo a encontrarla. NO
arranques con configuración hasta que efectivamente la vea.

### 2.2. Click 2 — Crear Task nueva

Indicación al participante:

> *"Click en 'Nueva Task' (o el botón de crear, según cómo aparezca).
> Se va a abrir un formulario."*

**Vos ya tenés todos los datos preparados de Fase 1.3. Pasale al
participante el contenido exacto a poner en cada campo:**

```
Nombre de la Task:    [nombre claro y reconocible — ej: "Consolidación pedidos lunes"]

Cadencia / Schedule:  [fecha/hora primera ejecución + recurrencia
                       — ej: "Cada lunes 09:00 ARG, empezando
                       el [próximo lunes]"]

Prompt / Instrucción: [Plantilla — ver Apéndice A según tipo de skill.
                       Plantilla genérica abajo.]
```

**Plantilla genérica del prompt de la Task** (adaptá a cada caso):

```
Invocá el skill [nombre-del-skill-personal] con los siguientes inputs:

- [Input 1]: [valor fijo o "pedímelo si no lo tenés"]
- [Input 2]: [valor fijo o "pedímelo si no lo tenés"]
- [Contexto de fecha]: hoy es {{TODAY}}

Cuando termine de ejecutar el skill, dejá el output en
[destino concreto: Notion DB X / carpeta Drive Y / mandalo por mail
a Z / posteá en WhatsApp grupo W].

Si el skill se traba, mandame un aviso al chat y no intentes seguir.
```

(Las plantillas específicas por tipo de skill — reporte, check, resumen,
conciliación — están en el Apéndice A.)

### 2.3. Click 3 — Confirmar y activar

Indicación final:

> *"Revisá los 3 campos: nombre, cadencia, prompt. Si está todo, click
> en 'Crear' o 'Guardar y activar'. Listo. La Task quedó programada."*

Pedile que te confirme con captura o descripción que la Task aparece en
la lista de Tasks activas.

---

## FASE 3 — Validación en seco (5-10 min)

**No te vayas sin disparo manual exitoso.** Una Task que nunca corrió
por primera vez es una hipótesis, no un sistema.

### 3.1. Disparo manual

Indicación al participante:

> *"Volvé a la lista de Tasks. Buscá la que acabás de crear. Hay una
> opción para dispararla a mano en este momento, sin esperar a la
> cadencia — buscala (botón 'Run now', menú de tres puntos, según UX).
> Disparala."*

Esperá a que termine. Tiempos típicos: entre 30 segundos y 5 minutos
según lo que hace el skill.

### 3.2. Verificación del output

Acompañalo a verificar que el output efectivamente llegó al destino
configurado:

- **Si destino = Notion:** abrí la base destino. ¿Aparece la entrada?
  ¿Tiene el formato esperado?
- **Si destino = Drive:** abrí la carpeta. ¿Aparece el archivo? ¿El
  nombre tiene el patrón esperado?
- **Si destino = mail:** abrí la bandeja del destinatario. ¿Llegó?
  ¿El asunto y cuerpo tienen el formato esperado?
- **Si destino = WhatsApp:** abrí el grupo. ¿Llegó el mensaje?
- **Si destino = chat de Claude solamente:** mala señal. Si no tiene
  destino externo, en 2 semanas el participante deja de mirarlo.
  Volvé a Fase 1.3 y redefiní el destino.

### 3.3. Capturar el screenshot del primer output

Pedile que saque captura del output llegado al destino. Esa captura es
el primer activo concreto de Semana 3 — sirve para el formulario de
feedback y para el caso del participante.

### 3.4. Si algo falló

Diagnóstico simple:

| Síntoma                          | Causa probable                              | Acción                                    |
|----------------------------------|---------------------------------------------|-------------------------------------------|
| La Task no arrancó               | Cadencia mal configurada / plan no lo soporta| Verificar campo cadencia y plan activo.   |
| Arrancó pero el skill se trabó   | Skill operativo no estaba listo             | Volver a `sistematizador-de-procesos`.    |
| Skill ejecutó pero output no llegó| Conector destino no autorizado / mal config | Revisar conector MCP en Settings.         |
| Output llegó incompleto          | Inputs faltantes en el prompt de la Task    | Editar la Task, agregar inputs faltantes. |

---

## FASE 4 — Documentación y plan (5 min)

### 4.1. Tabla resumen de la Task creada

Entregá al participante este bloque copiable:

```
TASK ACTIVA — [nombre]

- Skill invocado:    [nombre-del-skill-personal]
- Cadencia:          [Y]
- Próxima ejecución: [fecha exacta]
- Inputs fijos:      [lista]
- Destino del output:[lugar exacto]
- Validada en seco:  ✅ [fecha]
- Output de prueba:  [link al archivo / captura]
```

### 4.2. Plan para las próximas Tasks

Volvé al Blueprint de Semana 2B. Marcá:

- 🟢 **Esta semana en producción:** la Task que acabás de crear.
- 🟡 **Próxima semana:** el siguiente candidato del Blueprint —
  configurable solo, repitiendo este flujo.
- 🟡 **En 2-3 semanas:** el tercer candidato.
- ⚪ **Postergados:** los que no entraron en el Blueprint o los que
  decidiste mantener manuales.

Recomendación al participante:

> *"No agregues la 2da Task hasta que esta haya corrido al menos 2-3
> ciclos completos. Querés ver cómo se comporta sin estar mirando. Si
> a los 2-3 ciclos sigue funcionando, sumás la siguiente. Si falla,
> primero arreglamos antes de sumar más."*

### 4.3. Métrica inicial de ahorro estimado

Cierre con números — concretos, no vagos:

> *"Antes este proceso te tomaba [X] horas/semana. Con el skill operativo
> manual te bajó a [Y]. Con la Task corriendo sola, esperamos [Z]
> horas/semana. Eso son [W] horas al mes que volvés a tener."*

Pedile que anote el número objetivo. En Semana 4 se mide.

---

## Cierre de la sesión

Decile al participante, en estos términos o muy parecidos:

> *"Listo. Tenés tu skill personal corriendo solo. La Task se va a
> disparar [cadencia] sin que vos hagas nada — el output va a llegar a
> [destino]. Tu trabajo desde hoy es revisar el output cuando llegue,
> no acordarte de disparar el proceso."*
>
> *"En las próximas 2 semanas, sumá la siguiente Task del Blueprint
> usando el mismo flujo — abrís Tasks, nueva, prompt invocando tu
> skill, cadencia, listo. 3 clics. Si te trabás, hablamos en el
> próximo encuentro del Club."*
>
> *"Más adelante vamos a medir cuántas horas recuperaste y a diseñar el
> ritmo operativo nuevo para que el cambio se sostenga. Acá termina la
> parte de construir — lo que viene es operar."*

---

## REGLAS DE COMPORTAMIENTO INVIOLABLES

### 1. UNA Task por sesión
Nunca configures más de 1 Task en la misma sesión. Cada Task que el
participante deja corriendo es un compromiso operativo. Una sola, bien
validada, sostenida una semana, genera más valor que 3 abandonadas.

### 2. CADENCIA REAL, NO COSMÉTICA
Si el proceso es semanal, la Task corre semanal — no diaria. "Más
frecuente" no es "más útil". La cadencia tiene que ser la que el
negocio efectivamente necesita, no la que suena más profesional.

### 3. DESTINO EXTERNO OBLIGATORIO
El output de la Task NUNCA puede quedar solo en el chat de Claude. El
participante no va a abrir el chat todos los lunes a buscarlo. Si el
destino no es Notion / Drive / mail / WhatsApp / un dashboard que él ya
mira, la Task no se crea — primero se define el destino.

### 4. NO AUTOMATIZAR LO QUE TODAVÍA NO ANDA
Si el skill operativo de Semana 2B no fue ejercitado al menos 1-2 veces
a mano con resultado validado, NO programes Task sobre él. Frená la
sesión y mandalo a correr el skill a mano primero. Una Task sobre skill
verde es automatizar caos.

### 5. CRITERIO 3 CLICS
Del estado "skill instalado pero a mano" al estado "skill corre solo":
3 clics como máximo. Si tu indicación al participante requiere más, la
mecánica está mal escrita y hay que reescribirla.

### 6. AUTO-VERIFICACIÓN OBLIGATORIA AL ARRANCAR
Antes de guiar al participante por la UX de Tasks, ejecutá la Fase 0
contra `docs.claude.com` y `support.claude.com`. Si la UX cambió, te
adaptás. Si no podés verificar, avisás al participante. NO improvises
con la versión vieja sin avisar.

### 7. CERO TÉCNICA (heredado de D11 — el método)
Tres tests canónicos que cualquier paso debe pasar:
- **Test del click:** ¿se ejecuta haciendo click en interfaces que el
  participante ya usa? Si sí, OK. Si no, reescribir.
- **Test del paste:** ¿si falla un conector, el participante puede
  pegar texto/CSV y el skill se hace cargo? Si sí, OK. Si no, reescribir.
- **Test del navegador:** ¿si la herramienta no tiene MCP nativo, se
  puede operar vía Claude for Chrome? Si sí, OK. Si no, postergar o
  resolver por upload manual.

**Prohibiciones explícitas — NUNCA en ninguna fase:**
- Make / Zapier / n8n / iPaaS de cualquier tipo.
- APIs, claves API, webhooks, OAuth a mano.
- Código (Python, JS, Bash, fórmulas Excel complejas, macros).
- Terminal, Git, CLI, GitHub.
- Pedir al participante que contrate técnico para un paso.

### 8. PRODUCTO VIVO — SKILL QUE SE ADAPTA
Si Anthropic cambia la UX de Tasks, el skill se adapta solo via Fase 0
sin esperar a que el autor lo reescriba. El participante no tiene por qué
enterarse de eso — solo que "la interfaz cambió un poco, te llevo igual
al objetivo". Producto vivo en acción.

### 9. RECUPERACIÓN ANTE FALLO
Si en Fase 3 (validación en seco) la Task falla, NO la dejes activa con
"a ver qué pasa el lunes". Frená, diagnosticá con la tabla de Fase 3.4,
arreglalo, y volvé a probar. Una Task fallando en silencio es peor que
no tener Task.

---

## APÉNDICE A — Plantillas de prompt de Task según tipo de skill

Las Tasks programadas se configuran con un prompt en lenguaje natural
que invoca al skill. Estas son 4 plantillas según el patrón del skill
personal del participante. Adaptá nombres, inputs y destinos a cada caso.

### A.1. Reporte recurrente

```
Invocá el skill [nombre-del-skill] para generar el reporte de
[período: semanal/mensual].

Inputs:
- Período de referencia: del [primer día del período] al [último día].
- Hoy es {{TODAY}}.

Cuando el skill termine, dejá el output:
1. En la base de Notion "[nombre de la base]" como nueva entrada.
2. Resumen ejecutivo en 5 bullets enviado por mail a [email].

Si el skill pide algún input que no le pasé, frenate y mandame un
aviso al chat. No inventes datos.
```

### A.2. Check de alertas / umbrales

```
Invocá el skill [nombre-del-skill] en modo "check de alertas".

Inputs:
- Umbral A: [valor]
- Umbral B: [valor]
- Hoy es {{TODAY}}.

Cuando el skill termine:
- Si TODOS los umbrales están dentro del rango → mandá mensaje de
  status verde al WhatsApp grupo "[nombre]" diciendo "Todo OK al [fecha]".
- Si HAY alguno fuera de rango → mandá alerta detallada al WhatsApp
  grupo "[nombre]" con el indicador, valor actual y umbral violado.

Output adicional: dejá un registro en la base Notion "Logs de Alertas"
con el resultado de hoy.
```

### A.3. Resumen ejecutivo periódico

```
Invocá el skill [nombre-del-skill] para generar el resumen ejecutivo
de [período].

Inputs:
- Hoy es {{TODAY}}.
- Período cubierto: [N] días hacia atrás desde hoy.

Cuando el skill termine, mandame el resumen ejecutivo en estos formatos:
1. PDF en la carpeta Drive "[nombre]".
2. Highlights en 3 bullets enviados por mail a [email] con asunto
   "Resumen ejecutivo [período] — [fecha]".

El resumen ejecutivo no debería superar 1 página A4. Si hay riesgos
relevantes, marcalos en rojo arriba de todo.
```

### A.4. Conciliación / cruce de datos

```
Invocá el skill [nombre-del-skill] para hacer la conciliación
[descripción].

Inputs:
- Fuente A: [ubicación de los datos — Drive, Notion, paste manual].
- Fuente B: [ubicación de los datos].
- Hoy es {{TODAY}}.

Cuando el skill termine:
- Si NO hay diferencias → mandá mensaje de "Conciliación OK
  [fecha]" al chat del equipo en WhatsApp.
- Si HAY diferencias → genera planilla con las diferencias detalladas
  en Drive carpeta "[nombre]" con nombre "Conciliación-[YYYY-MM-DD]"
  y mandá alerta por mail a [email].

Si una de las fuentes no se puede leer, frenate y avisame al chat
en lugar de generar la conciliación incompleta.
```

---

## APÉNDICE B — Workarounds si la UX no soporta lo que necesitás

### B.1. Tasks no soporta cadencias muy específicas

**Síntoma:** el participante necesita cadencia tipo "primer martes hábil
del mes" y Tasks solo soporta "todos los martes" o "día N del mes".

**Workaround:** usar la cadencia más simple disponible (ej: "todos los
martes 9am") + agregar al prompt de la Task un check inicial:

```
ANTES de invocar al skill, verificá: ¿hoy es el primer martes hábil
del mes (no es feriado, y es el primer martes que cae después del día 1)?

- Si sí → procedé con la invocación normal.
- Si no → no hagas nada, no generes output, no avises. Salí.
```

### B.2. Tasks no soporta event-driven todavía

**Síntoma:** el participante quiere disparar la Task cuando ocurre algo
(ej: cuando llega un mail, cuando se actualiza una base de Notion).

**Workaround para Grupo 1:** configurar la Task con cadencia frecuente
(diaria o cada 6 hs) + el skill internamente verifica si el evento ya
ocurrió y solo actúa si sí. No es event-driven puro pero es la forma
de simularlo sin Make/Zapier.

**Para Grupo 2+:** revisar si Anthropic estabilizó event-driven y
volver a evaluar.

### B.3. Tasks tira límite de uso por plan

**Síntoma:** el plan del participante limita el número de Tasks activas
o las ejecuciones por mes y el participante necesita más.

**Acción:** no autoupgrade. Volvé al Blueprint y prioricá las Tasks de
mayor impacto. Recordale al participante que cada Task es un compromiso
operativo — 2-3 Tasks bien sostenidas suelen ser suficientes para el
proceso prioritario en Semana 3.

---

## APÉNDICE C — Referencia de UX de Tasks (última versión conocida)

**Esta sección es tu fallback cuando NO podés acceder a docs.claude.com
en Fase 0.** Refleja la UX al momento de empaquetar este skill.

> ⚠️ Importante: SIEMPRE intentá la auto-verificación de Fase 0 primero.
> Esta referencia es snapshot, no fuente de verdad. La fuente de verdad
> es `docs.claude.com` y `support.claude.com`.

### C.1. Ubicación

- En Claude web (claude.ai) y desktop: pestaña **"Tasks"** en la barra
  lateral izquierda, junto a "Chat" y "Projects".
- En Claude móvil: ícono de Tasks en el menú inferior (puede variar).

### C.2. Crear una Task scheduled

1. Click en **"Tasks"** en la barra lateral.
2. Click en **"New Task"** (botón arriba a la derecha).
3. Completar el formulario:
   - **Name:** texto libre.
   - **Schedule:** selector con opciones "Once" / "Daily" / "Weekly" /
     "Monthly" / "Custom (cron-like)".
   - **First run:** fecha y hora.
   - **Prompt:** campo de texto multilínea con el prompt en lenguaje
     natural.
4. Click en **"Create"** o **"Save and activate"**.

### C.3. Disparar una Task a mano

- Desde la lista de Tasks, click en la Task → menú de tres puntos →
  **"Run now"**.
- O abrir la Task y click en el botón **"Run now"** dentro del detalle.

### C.4. Editar / pausar / eliminar

- Lista de Tasks → tres puntos → "Edit" / "Pause" / "Delete".
- Las Tasks pausadas no corren pero quedan en la lista.
- Las eliminadas se pierden — usar pausa si querés volver atrás.

### C.5. Planes que la habilitan (verificar en docs)

- **Pro:** [verificar — al momento de empaquetar este skill, Pro
  habilita Tasks con límites]
- **Max / Team / Enterprise:** [verificar — al momento de empaquetar,
  límites más altos o sin límite]

### C.6. Límites conocidos

- Cantidad de Tasks activas por usuario: **verificar en docs vigentes**.
- Ejecuciones por mes: **verificar**.
- Duración máxima de la ejecución: **verificar**.
- Capacidad de invocar skills personales: confirmar — al momento de
  empaquetar este skill, la Task ejecuta el prompt en una sesión
  efímera con todos los skills del usuario disponibles, lo que permite
  invocar el skill personal por nombre.

### C.7. Si algo en C.1 a C.6 no calza con lo que ves en pantalla

Estás en Caso B de Fase 0.3 — la UX cambió. Adaptate a la versión
vigente y avisale al participante con el framing producto vivo.

---

## APÉNDICE D — Glosario rápido

- **Task scheduled:** función nativa de Claude que ejecuta un prompt en
  una cadencia definida (todos los lunes, el día 1 del mes, etc.).
- **Skill personal / skill operativo:** el skill que el participante
  construyó en Semana 2B con `sistematizador-de-procesos`. Contiene el
  SOP del proceso prioritario en formato ejecutable por Claude.
- **Blueprint de Automatización:** tabla entregada al final de Semana
  2B con 1-3 candidatos a Task scheduled marcados.
- **Cadencia:** frecuencia de ejecución de la Task (semanal, mensual,
  diaria, custom).
- **eterOS:** el sistema operativo del negocio. Nombre del sistema
  de skills encadenados que entrega el método.
- **Producto vivo:** principio de diseño del método. Los skills
  evolucionan mensualmente con feedback. En este skill se manifiesta en
  la Fase 0 (auto-verificación).

---

## Cierre del SKILL.md

Si llegaste acá leyendo el skill como participante: ya sabés cómo
funciona. Pedile a Claude que lo invoque diciéndole *"vamos con la
semana 3"*, *"orquestemos mi skill personal"*, o cualquier de los
triggers de la descripción.

Si llegaste acá como modelo ejecutando el skill: arrancá por Fase 0,
silenciosa. No avises de la auto-verificación al participante salvo
que detectes cambios. Volvé a este skill cada vez que necesites
verificar que estás siguiendo la mecánica canónica de Semana 3 — Tasks
scheduled invocando el skill personal, sin iPaaS, sin código, en 3
clics, con destino externo claro y validación en seco al final.

— el autor / el método
