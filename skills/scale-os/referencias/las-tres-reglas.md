# Las tres reglas

Scale OS tiene muchas carpetas, pero **el sistema son tres reglas**. Todo lo demás es andamio: puede
quedarse, pero no es lo que hace la diferencia.

Estas tres sobrevivieron a un filtro concreto: cada pieza del sistema se corrió también **sin** el
sistema, y la que salía igual de bien se sacó.

---

## 1 · Un objetivo es una definición de "listo" más una verificación que se corre, escrita antes de arrancar

Escribir la verificación **antes** parece burocracia. No lo es. Es lo único que impide que "listo" se
defina al final, para justificar lo que ya se hizo.

Y de ahí sale el corolario que hace casi todo el trabajo:

> **Una diferencia sin causa no cuenta como explicada.**

Un resultado que dice *"esto no coincide, no sé por qué"* es un **fallo**, no un resultado.

**Por qué aporta, medido.** Se tomó un cálculo con un error adentro y se lo juzgó con dos criterios:

| | criterio de sentido común<br>*"¿corrió y dio números?"* | criterio de Scale OS<br>*"¿toda diferencia tiene causa?"* |
|---|---|---|
| cálculo con el error | ✅ **pasa** | ❌ **falla** |
| cálculo corregido | ✅ pasa | ✅ pasa |

El criterio de sentido común **aprueba los dos**. No distingue. El de Scale OS rechaza el malo. Esa
es la definición de aportar: **rechazar un resultado que cualquiera daría por bueno**.

## 2 · Toda comprobación se corre también contra el escenario malo, y tiene que fallar ahí

Un test en verde tiene **dos** formas de pasar, y son distintas:

1. el sistema anda, o
2. **la comprobación no mide lo que dice medir.**

Correrla solo contra la versión buena no las distingue. Por eso toda comprobación nueva se corre
también contra la versión vieja, o contra el escenario que sabés que está mal, y **tiene que fallar
ahí**. Si pasa en los dos, pará: o el cambio no cambia nada, o el instrumento está desafinado.
Averiguá cuál antes de seguir.

**Tres cosas que se aprenden aplicándola:**

- **Elegí el caso donde las dos versiones tienen que divergir**, no el camino feliz. El camino feliz
  suele andar por casualidad y no discrimina.
- **Si el control no discrimina, sospechá del instrumento antes que del cambio.**
- **Guardá las corridas de la versión mala.** Sin ellas, "el test discrimina" es otra afirmación sin
  verificar. Vale la pena dejar el código viejo detrás de un flag, a propósito.

El mejor resultado posible de un control negativo no es que dé distinto: es que dé **el número que
habías predicho**. Ahí sabés que falla por el motivo que pensabas, no por otro.

## 3 · Un solo dueño por dato

Cada dato tiene **un** lugar donde vive. Todo lo demás apunta ahí. Nada se copia.

Suena obvio y se rompe todo el tiempo, porque copiar es más cómodo que enlazar. El costo aparece
después: se edita una copia, la otra queda vieja, y el sistema tiene **dos verdades**.

Dónde más duele:

- **Los frenos.** Dos copias de un freno son dos verdades sobre qué se puede tocar, que es el peor
  lugar posible para tener ambigüedad. Por eso `frenos.md` es dueño único y los objetivos heredan.
- **Las definiciones.** Copiar una definición adentro de cada objetivo es la forma más rápida de que
  se separen. Van punteros, no copias.
- **Las listas.** Si una lista vive en una herramienta externa, el archivo local es **derivado**, no
  una segunda copia. En cuanto alguien agregue algo allá, el archivo miente.

---

## Cómo se ven juntas

Las tres se apoyan entre sí. La regla 1 dice qué significa terminar. La regla 2 te dice si podés
creerle a la regla 1. La regla 3 evita que el criterio se bifurque mientras trabajás.

Si tuvieras que quedarte con una sola: **escribí cómo vas a verificar antes de empezar.** Las otras
dos protegen a esa.
