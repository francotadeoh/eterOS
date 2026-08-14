# eterOS — <nombre del negocio>

> Esto **no** es documentación. Es el estado vivo del sistema. Si lo que dice acá no coincide con lo
> que pasa de verdad, gana la realidad y el archivo está viejo.

## La secuencia

`onboarding → auditoría → conectar → frenos → skills → objetivos → loops`

Sin auditoría, los objetivos salen inventados. Y **conectar no se saltea ni se pospone**: un sistema
que guarda el estado en un disco deja al equipo afuera. Ese orden no se saltea.

## Las tres reglas

1. **Un objetivo es una definición de "listo" más una verificación que se corre, escrita antes de
   arrancar.** Y una diferencia sin causa no cuenta como explicada.
2. **Toda comprobación se corre también contra el escenario malo, y tiene que fallar ahí.**
3. **Un solo dueño por dato.** Nada se copia.

## Estructura

```
~/.claude/eteros/
├─ README.md        este archivo
├─ frenos.md        lo que nunca se hace sin OK. DUEÑO ÚNICO: no se copia a los objetivos
├─ negocio.md       la empresa, en las palabras del dueño
├─ diagnostico.md   dónde está parada
└─ estado/          estado de máquina, para que nada se pierda al cerrar la ventana
```

**Los objetivos y el catálogo de procesos no están acá: viven en la herramienta conectada**, que es
la que mira tu equipo. Este disco guarda el criterio y el estado, no el estado del negocio.

Solo si la conexión quedó en hueco aparece `procesos/catalogo.md` acá, y se dice que es provisorio.

## Las cuatro partes obligatorias de un objetivo

Sin las cuatro **no es un objetivo, es un deseo**. El sistema lo rechaza.

1. **Listo cuando** — verificable.
2. **Reglas que aplican** — punteros, no copias.
3. **Frenos propios** — el resto se hereda de `frenos.md`.
4. **Verificación en vivo** — algo que se **corre**, escrito **antes**, con su control negativo.
   **No tiene por qué ser un comando:** *"abrir tal página a las 9 y ver si el número está"* sirve
   igual. Lo que hace falta es que se haga en vez de opinarse, que pueda fallar, y que dos personas
   no puedan discutir el resultado.

## Estado

Pedíselo al sistema: **"¿cómo vienen mis objetivos?"**. Te lo lee de `estado/goals.json` y te lo
cuenta en prosa. No hay nada que corras vos.
