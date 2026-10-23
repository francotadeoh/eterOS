#!/usr/bin/env python3
"""Contradicciones: lo que un archivo afirma y otro (o el mismo, más abajo) desmiente.

Mira cuatro cosas, todas determinísticas:
  1. Conteos declarados. Un título que dice "Las tres reglas" o "Los 4 principios" y abajo enumera
     otra cantidad. Cuenta subtítulos numerados (`## 1 · ...`), ítems de lista de primer nivel
     (`1. ...`) o párrafos numerados en negrita (`**1 · ...**`). Si no enumera nada, no opina.
  2. Resúmenes contra su fuente. Si esa sección enumera títulos en negrita y linkea al archivo
     que los desarrolla, los títulos tienen que ser los mismos, en el mismo orden.
  3. Los pasos del método. "recorre N pasos" en README.md o AGENTS.md tiene que coincidir con
     los `## Paso n · ...` de skills/eteros/SKILL.md (el paso 0 no cuenta: es elegir profundidad).
  4. Numeración. Los subtítulos `## n · ...` y `## Paso n · ...` de un archivo van seguidos,
     sin saltos ni repetidos.
"""

import os
import re

from _comun import (
    ENCONTRE, LIMPIO, NO_PUDE, archivos_publicados, correr, leer, numero, reemplazar,
    seccion, sin_bloques_de_codigo, sin_cambios, titulos,
)

PALABRA_NUMERO = r"(\d+|un[oa]?|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce)"
TITULO_CON_CONTEO = re.compile(r"^(?:\W*\s*)?(?:los|las)\s+" + PALABRA_NUMERO + r"\s+\w", re.I)
SUBTITULO_NUMERADO = re.compile(r"^(?:paso\s+)?(\d+)\s*·", re.I)
ITEM = re.compile(r"^(\d+)\.\s+(.*)$")
PARRAFO_NUMERADO = re.compile(r"^\*\*(\d+)\s*·")
NEGRITA = re.compile(r"^\*\*(.+?)\*\*")
LINK_MD = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
PASOS_DECLARADOS = re.compile(r"\b(?:los|recorre|sus)\s+" + PALABRA_NUMERO + r"\s+pasos\b", re.I)
PASO = re.compile(r"^##\s+Paso\s+(\d+)\s*·", re.I)
METODO = "skills/eteros/SKILL.md"


def _normalizar(texto):
    t = texto.lower()
    t = re.sub(r"[*_`\"“”«»'’]", "", t)
    t = re.sub(r"[.,;:!?¡¿]+\s*$", "", t.strip())
    return " ".join(t.split())


def _enumeracion(lineas, nivel):
    """Lo que enumera una sección: ('subtitulos'|'items'|'parrafos', [(numero, texto)])."""
    subs = []
    for linea in lineas:
        m = re.match(r"^(#{1,6})\s+(.*)$", linea)
        if m and len(m.group(1)) == nivel + 1:
            s = SUBTITULO_NUMERADO.match(m.group(2))
            if s:
                subs.append((int(s.group(1)), m.group(2)[s.end():].strip()))
    if subs:
        return "subtitulos", subs
    # Ítems de primer nivel antes del primer subtítulo: si hay subtítulos sin número, las listas de
    # adentro son de cada subsección, no de la sección.
    items, parrafos = [], []
    for linea in lineas:
        if re.match(r"^#{1,6}\s", linea):
            break
        m = ITEM.match(linea)
        if m:
            negrita = NEGRITA.match(m.group(2))
            items.append((int(m.group(1)), negrita.group(1) if negrita else None))
        if PARRAFO_NUMERADO.match(linea):
            parrafos.append((int(PARRAFO_NUMERADO.match(linea).group(1)), None))
    if items:
        return "items", items
    if parrafos:
        return "parrafos", parrafos
    return None, []


def _subtitulos_numerados(lineas):
    """[(numero, titulo)] de los `## n · titulo` de un archivo."""
    salida = []
    for _, nivel, texto in titulos(lineas):
        if nivel == 2:
            s = SUBTITULO_NUMERADO.match(texto)
            if s and not texto.lower().startswith("paso"):
                salida.append((int(s.group(1)), texto[s.end():].strip()))
    return salida


def medir(raiz):
    publicados = archivos_publicados(raiz)
    if publicados is None:
        return NO_PUDE, ["no pude listar los archivos publicados (git ls-files falló)"]
    md = [p for p in publicados if p.endswith(".md")]
    if not md:
        return NO_PUDE, ["no encontré ningún .md publicado: no hay qué mirar"]

    estado, hallazgos = LIMPIO, []

    def hallazgo(texto):
        nonlocal estado
        estado = ENCONTRE
        hallazgos.append(texto)

    lineas_de = {}
    for ruta in md:
        texto = leer(raiz, ruta)
        if texto is None:
            return NO_PUDE, [f"no pude leer {ruta}"]
        lineas_de[ruta] = sin_bloques_de_codigo(texto)

    for ruta, lineas in lineas_de.items():
        # 1 y 2: conteos declarados y resúmenes contra su fuente
        for i, nivel, texto in titulos(lineas):
            m = TITULO_CON_CONTEO.match(texto)
            if not m:
                continue
            declarado = numero(m.group(1))
            cuerpo, _ = seccion(lineas, i, nivel)
            forma, enumerados = _enumeracion(cuerpo, nivel)
            if forma and declarado and len(enumerados) != declarado:
                hallazgo(
                    f"{ruta}:{i + 1} «{texto}» dice {declarado} y abajo enumera {len(enumerados)}"
                )
                continue
            if forma != "items" or not all(t for _, t in enumerados):
                continue
            for link in LINK_MD.findall("\n".join(cuerpo)):
                fuente = os.path.normpath(os.path.join(os.path.dirname(ruta), link)).replace(os.sep, "/")
                if fuente not in lineas_de:
                    continue  # el link roto lo reporta referencias.py
                desarrollados = _subtitulos_numerados(lineas_de[fuente])
                if not desarrollados:
                    continue
                if len(desarrollados) != len(enumerados):
                    hallazgo(
                        f"{ruta}:{i + 1} «{texto}» resume {len(enumerados)} y {fuente} "
                        f"desarrolla {len(desarrollados)}"
                    )
                    continue
                for (n, resumido), (_, desarrollado) in zip(enumerados, desarrollados):
                    if _normalizar(resumido) != _normalizar(desarrollado):
                        hallazgo(
                            f"{ruta}:{i + 1} el {n} dice «{resumido}» y {fuente} lo titula "
                            f"«{desarrollado}»"
                        )

        # 4: numeración seguida
        numerados = {"subtítulos numerados": [], "pasos": []}
        for _, nivel, texto in titulos(lineas):
            s = SUBTITULO_NUMERADO.match(texto)
            if nivel == 2 and s:
                tipo = "pasos" if texto.lower().startswith("paso") else "subtítulos numerados"
                numerados[tipo].append(int(s.group(1)))
        for tipo, numeros in numerados.items():
            if numeros and numeros != list(range(numeros[0], numeros[0] + len(numeros))):
                hallazgo(f"{ruta}: los {tipo} no van seguidos: {numeros}")

    # 3: los pasos del método
    declaraciones = []
    for ruta in ("README.md", "AGENTS.md"):
        for n, linea in enumerate(lineas_de.get(ruta, []), 1):
            for m in PASOS_DECLARADOS.finditer(linea):
                declaraciones.append((ruta, n, numero(m.group(1))))
    if declaraciones:
        if METODO not in lineas_de:
            return NO_PUDE, hallazgos + [f"se declaran pasos del método y no pude leer {METODO}"]
        pasos = [int(m.group(1)) for linea in lineas_de[METODO] for m in [PASO.match(linea)] if m]
        reales = len([p for p in pasos if p >= 1])
        for ruta, n, declarado in declaraciones:
            if declarado != reales:
                hallazgo(f"{ruta}:{n} dice {declarado} pasos y {METODO} tiene {reales}")

    return estado, hallazgos


CONTROLES = [
    ("la instancia sana da limpio", sin_cambios, LIMPIO),
    ("el título dice tres y la lista tiene cuatro",
     reemplazar("README.md", "3. **Un solo dueño por dato.**\n",
                "3. **Un solo dueño por dato.**\n4. **Una cuarta que nadie escribió.**\n"), ENCONTRE),
    ("el archivo dice tres y desarrolla dos",
     reemplazar("skills/eteros/referencias/las-tres-reglas.md", "\n## 3 · Un solo dueño por dato\n", "\n"),
     ENCONTRE),
    ("el resumen cambia el título de una regla",
     reemplazar("README.md", "**Un solo dueño por dato.**", "**Cada dato con su copia.**"), ENCONTRE),
    ("AGENTS dice más pasos de los que tiene el método",
     reemplazar("AGENTS.md", "recorre 2 pasos", "recorre 3 pasos"), ENCONTRE),
    ("un paso que se saltea un número",
     reemplazar("skills/eteros/SKILL.md", "## Paso 2 · Cerrar", "## Paso 3 · Cerrar"), ENCONTRE),
    ("un subtítulo numerado repetido",
     reemplazar("skills/eteros/referencias/las-tres-reglas.md", "## 2 · Toda", "## 1 · Toda"), ENCONTRE),
    ("se declaran pasos y el método no está",
     lambda raiz: os.remove(os.path.join(raiz, METODO)), NO_PUDE),
]

if __name__ == "__main__":
    correr(medir, CONTROLES)
