#!/usr/bin/env python3
"""Formato: lo que Claude Code necesita para encontrar y activar cada skill, y que NOVEDADES se pueda leer.

Por cada carpeta de skills/:
  - tiene SKILL.md, y arranca con un bloque --- ... --- de frontmatter
  - `name` existe, es kebab-case, tiene hasta 64 caracteres y es igual al nombre de la carpeta
  - `description` existe, no está vacía, tiene hasta 1024 caracteres y no trae etiquetas <...>
    (pasado ese largo, o con etiquetas, el skill no se carga o se carga cortado)

Y en NOVEDADES.md:
  - al menos una versión, con títulos `## vX.Y — mes año`
  - de la más nueva a la más vieja, sin repetidas (lo de arriba es lo último: así se lee)
"""

import re

from _comun import (
    ENCONTRE, LIMPIO, NO_PUDE, archivos_publicados, borrar, correr, leer, peor, reemplazar,
    sin_cambios,
)

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION = re.compile(r"^##\s+v(\d+)\.(\d+)(?:\.(\d+))?\s+[—-]\s+\S")
LARGO_NOMBRE, LARGO_DESCRIPCION = 64, 1024


def _frontmatter(texto):
    """Devuelve {clave: valor} o None si no hay bloque --- ... ---."""
    lineas = texto.splitlines()
    if not lineas or lineas[0].strip() != "---":
        return None
    try:
        fin = next(i for i in range(1, len(lineas)) if lineas[i].strip() == "---")
    except StopIteration:
        return None
    campos, clave = {}, None
    for linea in lineas[1:fin]:
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", linea)
        if m:
            clave = m.group(1)
            valor = m.group(2).strip()
            campos[clave] = "" if valor in (">", "|", ">-", "|-") else valor
        elif clave and linea.startswith((" ", "\t")):
            campos[clave] = (campos[clave] + " " + linea.strip()).strip()
    return {k: v.strip().strip('"').strip("'") for k, v in campos.items()}


def _medir_skills(raiz, publicados):
    carpetas = sorted({p.split("/")[1] for p in publicados if p.startswith("skills/") and p.count("/") >= 2})
    if not carpetas:
        return NO_PUDE, ["no encontré ninguna carpeta publicada en skills/"]
    estado, hallazgos = LIMPIO, []
    for carpeta in carpetas:
        ruta = f"skills/{carpeta}/SKILL.md"
        if ruta not in publicados:
            estado = ENCONTRE
            hallazgos.append(f"skills/{carpeta}/ no tiene SKILL.md publicado")
            continue
        texto = leer(raiz, ruta)
        if texto is None:
            return NO_PUDE, hallazgos + [f"no pude leer {ruta}"]
        campos = _frontmatter(texto)
        if campos is None:
            estado = ENCONTRE
            hallazgos.append(f"{ruta} no arranca con un frontmatter --- ... --- cerrado")
            continue
        nombre = campos.get("name", "")
        descripcion = " ".join(campos.get("description", "").split())
        problemas = []
        if not nombre:
            problemas.append("le falta `name`")
        else:
            if nombre != carpeta:
                problemas.append(f"`name: {nombre}` no coincide con la carpeta `{carpeta}`")
            if not KEBAB.match(nombre):
                problemas.append(f"`name: {nombre}` no es kebab-case (minúsculas, números y guiones)")
            if len(nombre) > LARGO_NOMBRE:
                problemas.append(f"`name` tiene {len(nombre)} caracteres (máximo {LARGO_NOMBRE})")
        if not descripcion:
            problemas.append("le falta `description` o está vacía")
        else:
            if len(descripcion) > LARGO_DESCRIPCION:
                problemas.append(
                    f"`description` tiene {len(descripcion)} caracteres (máximo {LARGO_DESCRIPCION})"
                )
            if re.search(r"<[A-Za-z/!]", descripcion):
                problemas.append("`description` trae etiquetas <...>")
        if problemas:
            estado = ENCONTRE
            hallazgos += [f"{ruta}: {p}" for p in problemas]
    return estado, hallazgos


def _medir_novedades(raiz, publicados):
    if "NOVEDADES.md" not in publicados:
        return ENCONTRE, ["NOVEDADES.md no está publicado: la actualización no tiene qué contar"]
    texto = leer(raiz, "NOVEDADES.md")
    if texto is None:
        return NO_PUDE, ["no pude leer NOVEDADES.md"]
    versiones, hallazgos = [], []
    for n, linea in enumerate(texto.splitlines(), 1):
        if not linea.startswith("## "):
            continue
        m = VERSION.match(linea)
        if not m:
            hallazgos.append(f"NOVEDADES.md:{n} título de versión con otro formato: {linea.strip()}")
            continue
        versiones.append((n, tuple(int(x or 0) for x in m.groups())))
    if not versiones:
        hallazgos.append("NOVEDADES.md no tiene ninguna versión con título `## vX.Y — mes año`")
    for (n_ant, v_ant), (n, v) in zip(versiones, versiones[1:]):
        if v == v_ant:
            hallazgos.append(f"NOVEDADES.md:{n} repite la versión de la línea {n_ant}")
        elif v > v_ant:
            hallazgos.append(
                f"NOVEDADES.md:{n} está debajo de una versión más vieja (línea {n_ant}): "
                "la más nueva va arriba"
            )
    return (ENCONTRE if hallazgos else LIMPIO), hallazgos


def medir(raiz):
    publicados = archivos_publicados(raiz)
    if publicados is None:
        return NO_PUDE, ["no pude listar los archivos publicados (git ls-files falló)"]
    publicados = set(publicados)
    e1, h1 = _medir_skills(raiz, publicados)
    e2, h2 = _medir_novedades(raiz, publicados)
    return peor(e1, e2), h1 + h2


CONTROLES = [
    ("la instancia sana da limpio", sin_cambios, LIMPIO),
    ("el name no coincide con la carpeta",
     reemplazar("skills/eteros/SKILL.md", "name: eteros", "name: eteros-viejo"), ENCONTRE),
    ("el name no es kebab-case",
     reemplazar("skills/eteros/SKILL.md", "name: eteros", "name: EterOS"), ENCONTRE),
    ("sin description",
     reemplazar("skills/eteros/SKILL.md", "description: >\n  Skill de ejemplo para los controles negativos.\n", ""),
     ENCONTRE),
    ("una description de más de 1024 caracteres",
     reemplazar("skills/eteros/SKILL.md", "Skill de ejemplo", "palabra " * 130), ENCONTRE),
    ("una description con etiquetas",
     reemplazar("skills/eteros/SKILL.md", "Skill de ejemplo", "Skill <ejemplo>"), ENCONTRE),
    ("un frontmatter sin cerrar",
     reemplazar("skills/eteros/SKILL.md", "controles negativos.\n---\n", "controles negativos.\n"),
     ENCONTRE),
    ("una carpeta de skill sin SKILL.md",
     borrar("skills/eteros/SKILL.md"), ENCONTRE),
    ("NOVEDADES con la versión vieja arriba",
     reemplazar("NOVEDADES.md", "## v1.0 — agosto 2026", "## v1.5 — agosto 2026"), ENCONTRE),
    ("NOVEDADES con una versión repetida",
     reemplazar("NOVEDADES.md", "## v1.1 — septiembre 2026", "## v1.0 — septiembre 2026"), ENCONTRE),
    ("NOVEDADES con un título fuera de formato",
     reemplazar("NOVEDADES.md", "## v1.1 — septiembre 2026", "## Versión 1.1"), ENCONTRE),
    ("sin skills/ no hay qué mirar", borrar("skills"), NO_PUDE),
]

if __name__ == "__main__":
    correr(medir, CONTROLES)
