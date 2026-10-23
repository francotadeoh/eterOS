#!/usr/bin/env python3
"""Referencias rotas: todo archivo que el repo nombra tiene que existir para quien lo clona.

Mira tres cosas:
  1. Los links markdown a archivos locales: [texto](ruta).
  2. Las rutas entre backticks que apuntan adentro del repo: `skills/...`, `referencias/...`,
     `plantillas/...`. Un nombre suelto como `DEUDA-DE-PRODUCTO.md` no se mira: puede vivir
     fuera del repo a propósito, y adivinar dónde da rojos que nadie va a creer.
  3. Que cada `!/ruta` del whitelist del .gitignore exista. Un permiso para algo que no está es
     una de dos: un archivo que se borró, o un nombre mal escrito que deja afuera al bueno.

"Existir" es estar publicado (`git ls-files`), no estar en tu disco: si un archivo no pasa el
whitelist, para quien instala no existe.

No mira lo que vive fuera del repo a propósito: `~/...`, `_build/...`, rutas absolutas y
patrones con `*` o `<...>`.
"""

import os
import re

from _comun import (
    ENCONTRE, LIMPIO, NO_PUDE, archivos_publicados, borrar, correr, leer, reemplazar,
    sin_bloques_de_codigo, sin_cambios,
)

LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RUTA_EN_BACKTICKS = re.compile(r"`((?:skills|referencias|plantillas)/[^`\s]*)`")
FUERA_DEL_REPO = ("~", "/", "_build", "http:", "https:", "mailto:", "#")


def _se_ignora(ruta):
    return ruta.startswith(FUERA_DEL_REPO) or any(c in ruta for c in "*<>{}$")


def _existe(ruta, publicados, carpetas):
    ruta = os.path.normpath(ruta).replace(os.sep, "/")
    if ruta.startswith("../"):
        return False
    return ruta in publicados or ruta.rstrip("/") in carpetas


def _candidatos(origen, ruta):
    """Dónde puede vivir una ruta nombrada desde `origen`.

    Al lado del archivo, en la raíz del skill que la nombra, en la raíz del repo, y en el
    skill principal: los satélites nombran `referencias/...` del método sin repetir el prefijo.
    """
    base = os.path.dirname(origen)
    candidatos = [os.path.join(base, ruta), ruta, os.path.join("skills/eteros", ruta)]
    partes = origen.split("/")
    if len(partes) >= 2 and partes[0] == "skills":
        candidatos.insert(1, os.path.join("skills", partes[1], ruta))
    return candidatos


def medir(raiz):
    publicados = archivos_publicados(raiz)
    if publicados is None:
        return NO_PUDE, ["no pude listar los archivos publicados (git ls-files falló)"]
    if not any(p.endswith(".md") for p in publicados):
        return NO_PUDE, ["no encontré ningún .md publicado: no hay qué mirar"]

    publicados_set = set(publicados)
    carpetas = set()
    for p in publicados:
        partes = p.split("/")
        for i in range(1, len(partes)):
            carpetas.add("/".join(partes[:i]))

    estado, hallazgos = LIMPIO, []

    for origen in publicados:
        if not origen.endswith(".md"):
            continue
        texto = leer(raiz, origen)
        if texto is None:
            return NO_PUDE, [f"no pude leer {origen}"]
        for n, linea in enumerate(sin_bloques_de_codigo(texto), 1):
            for m in LINK.finditer(linea):
                ruta = m.group(1).split("#", 1)[0]
                if not ruta or _se_ignora(m.group(1)):
                    continue
                destino = os.path.join(os.path.dirname(origen), ruta)
                if not _existe(destino, publicados_set, carpetas):
                    estado = ENCONTRE
                    hallazgos.append(f"{origen}:{n} link roto → {m.group(1)}")
            for m in RUTA_EN_BACKTICKS.finditer(linea):
                ruta = m.group(1).rstrip(".,;:")
                if _se_ignora(ruta):
                    continue
                if not any(_existe(c, publicados_set, carpetas) for c in _candidatos(origen, ruta)):
                    estado = ENCONTRE
                    hallazgos.append(f"{origen}:{n} nombra `{ruta}` y no existe en el repo")

    gitignore = leer(raiz, ".gitignore")
    if gitignore is None:
        return NO_PUDE, hallazgos + ["no pude leer .gitignore"]
    for n, linea in enumerate(gitignore.splitlines(), 1):
        linea = linea.strip()
        if not linea.startswith("!/"):
            continue
        ruta = linea[2:].rstrip("/")
        if " #" in ruta or "\t#" in ruta:
            estado = ENCONTRE
            hallazgos.append(
                f".gitignore:{n} tiene un comentario al final del patrón; gitignore no los "
                f"acepta y el patrón deja de matchear: {linea}"
            )
            continue
        if any(c in ruta for c in "*?["):
            continue
        if ruta not in publicados_set and ruta not in carpetas:
            estado = ENCONTRE
            hallazgos.append(f".gitignore:{n} habilita {linea} y eso no está publicado")

    return estado, hallazgos


CONTROLES = [
    ("la instancia sana da limpio", sin_cambios, LIMPIO),
    ("un link a un archivo que no existe",
     reemplazar("README.md", "referencias/las-tres-reglas.md)", "referencias/las-cuatro-reglas.md)"),
     ENCONTRE),
    ("una ruta en backticks a un archivo borrado",
     borrar("skills/eteros/referencias/las-tres-reglas.md"), ENCONTRE),
    ("un permiso del .gitignore para algo que no existe",
     reemplazar(".gitignore", "!/AGENTS.md\n", "!/AGENTS.md\n!/GUIA.md\n"), ENCONTRE),
    ("un comentario al final de la línea del patrón",
     reemplazar(".gitignore", "!/NOVEDADES.md\n", "!/NOVEDADES.md  # lo que se lee\n"), ENCONTRE),
    ("un repo sin ningún .md no es un repo limpio",
     lambda raiz: [borrar(p)(raiz) for p in ("README.md", "AGENTS.md", "NOVEDADES.md", "skills")],
     NO_PUDE),
]

if __name__ == "__main__":
    correr(medir, CONTROLES)
