# Diseño humano

**Para qué:** tener una lente más sobre **cómo funciona la energía de la persona y cómo decide
mejor.** Sirve para elegir la forma de trabajar —en solitario o con gente, iniciando o respondiendo, en
sesiones largas o cortas— cuando llegue la fase 4.

**Es opcional y es una lente, no un destino.** Hay gente a la que le sirve mucho y gente a la que no le
cierra. Las dos están bien. Si la carta dice una cosa y la experiencia de la persona dice otra, **gana
la experiencia**, y se anota la diferencia.

## Cómo se consigue la carta

**El sistema no calcula la carta.** La persona la saca gratis en cualquier sitio de diseño humano con
tres datos: **fecha, hora y lugar de nacimiento.** La hora importa: sin ella la carta puede salir mal.

Decíselo así, en una línea: *"Para esta parte necesitás tu fecha, hora y lugar de nacimiento. Con eso
sacás tu carta gratis en internet en dos minutos. Pegame lo que te sale, o mandame una captura."*

**Si no sabe su hora, o no quiere hacerlo:** se escribe el archivo con `estado: salteado`, el motivo
en una línea, y se sigue con la entrevista. No se insiste y no se vuelve a ofrecer.

## Lo que se lee de la carta

Cuatro datos. Del resto de la carta no hace falta nada para esto.

| Dato | Qué es, en palabras normales |
|---|---|
| **Tipo** | Cómo se mueve su energía. Generador, Generador Manifestante, Proyector, Manifestador o Reflector |
| **Estrategia** | Cómo le conviene entrar en las cosas: responder, esperar que la inviten, informar antes de actuar, darse tiempo |
| **Autoridad** | Desde dónde decide mejor: el cuerpo, la emoción con tiempo, la intuición del momento, hablarlo con otros |
| **Perfil** | Dos números que describen su forma de aprender y de mostrarse |

## Cómo se usa

Por cada uno de los cuatro, una pregunta que contrasta la carta con su vida:

- *"Tu carta dice que sos Proyector: que te va mejor guiando a otros que haciendo todo vos, y cuando
  te invitan más que cuando empujás. ¿Te pasó? ¿Cuándo?"*
- *"Tu autoridad es emocional: decidir en caliente te sale peor que esperar un día. ¿Te reconocés?"*

**Lo que se anota es la respuesta de la persona, no la definición del tipo.** La definición está en
cualquier sitio; lo valioso es dónde se reconoce y dónde no.

Para la fase 4 dejá escrito, en una línea por cada una, qué sugiere sobre:

1. **Trabajar en solitario o con gente.**
2. **Iniciar o responder**: salir a buscar clientes o que lleguen.
3. **El ritmo**: sostenido todos los días o en picos.
4. **Cómo tomar la decisión del primer camino**: rápido, con tiempo o hablándolo.

## Qué queda escrito

`~/.claude/autoconocimiento/diseno-humano.md`:

```markdown
---
estado: completo          # completo | salteado
motivo:                   # obligatorio si es "salteado"
fecha: AAAA-MM-DD
---

# Tu diseño humano

## Tipo · Estrategia · Autoridad · Perfil
## Dónde te reconociste
## Dónde no
## Lo que sugiere para trabajar
En solitario o con gente · iniciar o responder · el ritmo · cómo decidir.
```
