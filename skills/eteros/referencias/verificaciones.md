# Cómo se verifica algo cuando no hay un comando que correr

La regla 1 pide una verificación **que se corra**, escrita antes de arrancar. Y ahí aparece el
malentendido más común: que verificar es escribir un comando en una terminal.

**No lo es.** Una verificación es cualquier cosa que cumpla tres condiciones:

1. **Se hace, no se opina.** Hay una acción concreta: abrir tal lugar, mirar tal cosa.
2. **Puede fallar.** Si no existe un resultado posible que te obligue a decir *no está listo*, no es
   una verificación.
3. **Dos personas no pueden discutir el resultado.** El número está o no está. El archivo apareció o
   no apareció.

Mirar la pantalla y decir *"parece que anda"* falla las tres. Abrir una página a las 9 de la mañana
y ver si el número del día está ahí las cumple las tres, sin escribir una línea de código.

---

## Los cuatro moldes

Casi todo objetivo de una empresa entra en uno de estos. Elegí el que se parezca y completá lo que está
entre corchetes.

### 1 · El número aparece solo

> **Listo cuando:** el \[dato que hoy sacás a mano\] está en \[dónde\] antes de las \[hora\],
> \[cuántos\] días seguidos, sin que vos lo pongas.

Sirve para reportes, controles diarios, tableros, arqueos, cierres.

**Lo que lo hace bueno:** el *"sin que vos lo pongas"*. Sin esa cláusula estás midiendo que el número
existe, no que el sistema lo produce.

**Control negativo:** **apagalo un día y mirá que el número NO aparezca.**
Si aparece igual, hay otra cosa poniéndolo ahí y no estás midiendo lo que creés. Averiguá qué antes
de darlo por bueno.

### 2 · La pieza aparece sola

> **Listo cuando:** en \[qué carpeta o qué lista\] hay \[qué cosa\] nueva cada \[cuándo\], y vos no
> la creaste.

Sirve para contenido, borradores, propuestas, resúmenes de reunión, fichas nuevas.

**Lo que lo hace bueno:** cuenta piezas, no calidad. La calidad es otro objetivo y se verifica
distinto (molde 4). Mezclarlos hace que ninguno de los dos se pueda cerrar.

**Control negativo:** **sacale la entrada.** Cortá lo que lo alimenta (la grabación, el formulario,
la fuente) y mirá que esa semana **no aparezca nada**. Si aparece igual, está copiando algo viejo.

### 3 · Salió sin vos

> **Listo cuando:** \[qué cosa\] salió \[cuántas\] veces, y en ninguna de esas veces la escribiste,
> la revisaste ni la disparaste vos.

Sirve para avisos, recordatorios, seguimientos, mensajes internos, alertas.

**Lo que lo hace bueno:** las tres cosas juntas. *Escribir*, *revisar* y *disparar* son tres formas
distintas de seguir siendo el cuello, y la que más sobrevive es la del medio: si todavía lo revisás
antes de que salga, no está delegado, está esperándote.

**Control negativo:** **avisá que te vas dos semanas y no toques nada.** Si sigue saliendo, está
delegado. Si no sale, encontraste la dependencia exacta, que era el objetivo de todos modos.

> ⚠️ Si lo que sale va hacia afuera, hacia una persona de verdad, esto es un freno. Se prueba con
> vos mirando la primera vez, y recién después se suelta.

### 4 · El cero

> **Listo cuando:** durante \[cuánto tiempo\] **no** pasó \[qué cosa\].

Sirve para lo que se mide por ausencia: nadie tuvo que preguntarte, no hubo que corregir a mano, no
se cayó, no se atrasó.

**Lo que lo hace bueno:** es el único molde que verifica una delegación de verdad, porque mide que no
te necesitaron. También es el más fácil de falsear sin querer: si nadie te preguntó porque nadie usó
el sistema, el cero no significa nada.

**Control negativo:** **contá también el uso.** Cero preguntas sobre cero uso no es un cero, es un
sistema apagado. El cero vale solamente si al lado hay un número mayor a cero de veces que se usó.

---

### 5 · Las horas devueltas

> **Listo cuando:** \[qué proceso\] pasó de \[horas del mes medido\] a \[horas nuevas\] **y** la
> causa declarada es *cambió de manos*, *cambió de forma* o *se eliminó*, con fecha, contra una línea
> base congelada el \[fecha\].

Sirve para lo único que el sistema promete de verdad: devolver horas.

**Lo que lo hace bueno:** que la causa sea parte del *listo*, no un comentario al costado.

> **Una hora cuenta como devuelta solo si el proceso cambió de manos o de forma, con fecha.
> No si el número cambió.**

Sin esa cláusula, cada error de estimación se convierte en una victoria. El caso que lo obliga: el
soporte del Club pasó de 10 h/mes a 0,5 y un contador ingenuo habría anunciado 9,5 horas
recuperadas. **La estimación estaba mal por un factor de 20 y el proceso nunca cambió de manos.**

**Control negativo:** **bajale las horas a una fila sin cambiarle el ejecutor ni la forma.** El
medidor tiene que decir que **no** cuenta como devuelta. Si la cuenta igual, no está midiendo horas
devueltas: está midiendo que alguien editó un número.

**Segundo control, el de la línea base:** **volvé a generar el "antes".** Si el sistema lo deja
re-escribir, todas las horas devueltas van a dar cero para siempre, porque el antes se mueve con el
después. Tiene que negarse.

---

## Los tres estados de todo agregador, y por qué el tercero gana

Cualquier cosa que junte resultados de varias fuentes —un gate, un medidor, un total de horas, un
tablero— tiene **tres** estados, no dos:

| Estado | Qué significa | Exit code |
|---|---|---|
| **limpio** | miré todo y no encontré nada | `0` |
| **encontré algo** | miré todo y encontré esto | `1` |
| **no pude medir** | **no pude mirar** una parte | `2` |

**El tercero es el que se disfraza de buena noticia.** Un agregador que no pudo leer una fuente y
sale con `0` está diciendo *"está todo bien"* cuando lo honesto es *"no vi"*. Nadie revisa un verde.

**En el exit code, el `2` pisa al `1` y al `0`.** No es el máximo, no es el último: **gana siempre**.
Si una sola fuente de veinte no se pudo leer, el resultado del conjunto es `2`, aunque las otras
diecinueve estén limpias.

**Y se aplica igual sin exit codes.** Un total de horas donde una fila está en *no se pudo medir*
**no se publica como número**: se publica el rango y se dice qué falta. Un número que nadie puede
reproducir hace más daño que no tener número, porque se cita después.

## Cómo se elige el molde

| Si el objetivo es | Molde |
|---|---|
| que un dato aparezca sin que lo calcules | **1 · El número aparece solo** |
| que se produzca algo con cierta frecuencia | **2 · La pieza aparece sola** |
| que algo salga sin que estés en el medio | **3 · Salió sin vos** |
| que dejen de necesitarte para algo | **4 · El cero** |
| que un proceso te devuelva horas | **5 · Las horas devueltas** |

Si el objetivo no entra en ninguno, lo más probable es que sea **dos objetivos mezclados**. Partilo.

## El error que hay que evitar

**Escribir la verificación después de que la cosa ya anda.** Cuando ya viste el resultado, la
verificación se escribe sola para aprobarlo: elegís sin darte cuenta el día que salió bien, el
número que dio, la ventana que funcionó.

Por eso se escribe antes. No es burocracia: es lo único que impide que *"listo"* se defina al final,
para justificar lo que ya hiciste.

## Y si igual no se te ocurre ninguna

Eso es información, no un problema tuyo. Quiere decir una de dos cosas:

- **El objetivo está escrito como un deseo** (*"ordenar la información"*, *"mejorar el
  seguimiento"*). Preguntá qué sería distinto un martes cualquiera si estuviera hecho, y verificá
  eso.
- **Es una decisión, no un objetivo** (a quién le hablás, qué precio ponés, qué ofrecés). Eso no se
  verifica corriendo nada: se decide. Un sistema que itera sobre decisiones que no puede verificar
  gira en falso. Ver la última sección de `formas.md`.

Ver `las-tres-reglas.md` y la plantilla `plantillas/goal.md`.
