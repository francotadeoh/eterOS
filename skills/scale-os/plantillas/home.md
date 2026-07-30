# Scale OS — <nombre del negocio>

> Esto **no** es documentación. Es el estado vivo del sistema. Si lo que dice acá no coincide con lo
> que pasa de verdad, gana la realidad y el archivo está viejo.

## La secuencia

`onboarding → auditoría → skills → objetivos → loops`

Sin auditoría, los objetivos salen inventados. Ese orden no se saltea.

## Las tres reglas

1. **Un objetivo es una definición de "listo" más una verificación que se corre, escrita antes de
   arrancar.** Y una diferencia sin causa no cuenta como explicada.
2. **Toda comprobación se corre también contra el escenario malo, y tiene que fallar ahí.**
3. **Un solo dueño por dato.** Nada se copia.

## Estructura

```
~/.claude/scale-os/
├─ README.md        este archivo
├─ frenos.md        lo que nunca se hace sin OK. DUEÑO ÚNICO: no se copia a los objetivos
├─ negocio.md       la empresa, en las palabras del dueño
├─ diagnostico.md   dónde está parada
├─ objetivos/       uno por archivo, con su verificación escrita antes
├─ loops/           lo que se repite solo
├─ procesos/        cada proceso con su forma
└─ estado/          estado de máquina, para que nada se pierda al cerrar la ventana
```

## Las cuatro partes obligatorias de un objetivo

Sin las cuatro **no es un objetivo, es un deseo**. El sistema lo rechaza.

1. **Listo cuando** — verificable.
2. **Reglas que aplican** — punteros, no copias.
3. **Frenos propios** — el resto se hereda de `frenos.md`.
4. **Verificación en vivo** — el comando que se **corre**, escrito **antes**, con su control negativo.

## Estado

```bash
python3 -c "import json;d=json.load(open('$HOME/.claude/scale-os/estado/goals.json'));[print(g['id'],g['estado'],'-',g['nombre']) for g in d['goals']]"
```
