"""Lo que comparten los gates públicos. No es un gate: el agregador saltea los que empiezan con _.

Cada gate define:
  medir(raiz)  -> (estado, hallazgos)   estado: LIMPIO, ENCONTRE o NO_PUDE
  CONTROLES    -> [(nombre, fabricar, esperado)]
                  fabricar(raiz) rompe (o no) una copia de la instancia sana de ejemplo,
                  y esperado es el estado que el gate TIENE que devolver contra esa copia.

Y termina con `correr(medir, CONTROLES)`, que resuelve los argumentos:
  gate.py [ruta]      mide el repo (por defecto, el repo donde vive este archivo)
  gate.py --controles corre los controles: exit 0 si todos dieron lo esperado, 2 si alguno no
"""

import os
import re
import subprocess
import sys
import tempfile

LIMPIO, ENCONTRE, NO_PUDE = 0, 1, 2
NOMBRE_ESTADO = {LIMPIO: "limpio", ENCONTRE: "encontré algo", NO_PUDE: "no pude medir"}

RAIZ_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

NUMEROS = {
    "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5, "seis": 6,
    "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
}


def numero(texto):
    """'tres' -> 3, '8' -> 8, cualquier otra cosa -> None."""
    t = texto.lower()
    if t.isdigit():
        return int(t)
    return NUMEROS.get(t)


def peor(a, b):
    """El 2 pisa al 1 y al 0. No es el máximo por casualidad: es la regla."""
    if NO_PUDE in (a, b):
        return NO_PUDE
    return max(a, b)


def archivos_publicados(raiz):
    """Los archivos que ve quien clona el repo, no los que hay en el disco.

    Con git, es `git ls-files`: un archivo que existe en tu máquina pero no pasa el whitelist
    del .gitignore no existe para nadie más. Sin git (las instancias de ejemplo de los
    controles), es lo que hay en el disco, sin _build/ ni .git/.
    """
    if os.path.isdir(os.path.join(raiz, ".git")):
        try:
            salida = subprocess.run(
                ["git", "-C", raiz, "ls-files", "-z"],
                check=True, capture_output=True,
            ).stdout.decode("utf-8")
            return sorted(p for p in salida.split("\0") if p)
        except (OSError, subprocess.CalledProcessError, UnicodeDecodeError):
            return None
    rutas = []
    for base, dirs, nombres in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in (".git", "_build")]
        for n in nombres:
            rutas.append(os.path.relpath(os.path.join(base, n), raiz).replace(os.sep, "/"))
    return sorted(rutas)


def leer(raiz, ruta):
    """Devuelve el texto, o None si no se pudo leer (y eso es un 2, no un 0)."""
    try:
        with open(os.path.join(raiz, ruta), encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None


def sin_bloques_de_codigo(texto):
    """Las líneas de un markdown con los bloques ``` vaciados (se conserva la numeración)."""
    lineas, adentro = [], False
    for linea in texto.splitlines():
        if linea.lstrip().startswith("```"):
            adentro = not adentro
            lineas.append("")
            continue
        lineas.append("" if adentro else linea)
    return lineas


TITULO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")


def titulos(lineas):
    """[(indice_de_linea, nivel, texto)] de los títulos markdown."""
    salida = []
    for i, linea in enumerate(lineas):
        m = TITULO.match(linea)
        if m:
            salida.append((i, len(m.group(1)), m.group(2)))
    return salida


def seccion(lineas, indice, nivel):
    """Las líneas que siguen a un título hasta el próximo título de su nivel o más alto."""
    fin = len(lineas)
    for j in range(indice + 1, len(lineas)):
        m = TITULO.match(lineas[j])
        if m and len(m.group(1)) <= nivel:
            fin = j
            break
    return lineas[indice + 1:fin], indice + 1


# --- la instancia sana de ejemplo, contra la que corren los controles ---------------------

INSTANCIA_SANA = {
    ".gitignore": "/*\n!/.gitignore\n!/README.md\n!/AGENTS.md\n!/NOVEDADES.md\n!/skills/\n",
    "README.md": (
        "# Ejemplo\n\n"
        "## Las tres reglas\n\n"
        "1. **Primero se escribe el listo.** Antes de arrancar.\n"
        "2. **Toda comprobación falla contra el caso malo.**\n"
        "3. **Un solo dueño por dato.**\n\n"
        "Están en [`referencias/las-tres-reglas.md`](skills/eteros/referencias/las-tres-reglas.md).\n"
    ),
    "AGENTS.md": (
        "# Para quien edita\n\n"
        "El método recorre 2 pasos. Vive en `skills/eteros/SKILL.md`.\n"
    ),
    "NOVEDADES.md": (
        "# Novedades\n\n"
        "## v1.1 — septiembre 2026\n\nAlgo nuevo.\n\n"
        "## v1.0 — agosto 2026\n\nLo primero.\n"
    ),
    "skills/eteros/SKILL.md": (
        "---\n"
        "name: eteros\n"
        "description: >\n"
        "  Skill de ejemplo para los controles negativos.\n"
        "---\n\n"
        "# Ejemplo\n\n"
        "## Paso 0 · Elegir\n\n"
        "## Paso 1 · Arrancar\n\nLeé `referencias/las-tres-reglas.md`.\n\n"
        "## Paso 2 · Cerrar\n"
    ),
    "skills/eteros/referencias/las-tres-reglas.md": (
        "# Las tres reglas\n\n"
        "## 1 · Primero se escribe el listo\n\n"
        "## 2 · Toda comprobación falla contra el caso malo\n\n"
        "## 3 · Un solo dueño por dato\n"
    ),
}


def fabricar_instancia_sana(raiz):
    for ruta, contenido in INSTANCIA_SANA.items():
        destino = os.path.join(raiz, ruta)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(contenido)


def reemplazar(ruta, viejo, nuevo):
    """Devuelve un fabricar() que cambia `viejo` por `nuevo` en `ruta` de la instancia sana."""
    def fabricar(raiz):
        p = os.path.join(raiz, ruta)
        with open(p, encoding="utf-8") as f:
            texto = f.read()
        if viejo not in texto:
            raise RuntimeError(f"el control no encontró qué romper en {ruta}: {viejo!r}")
        with open(p, "w", encoding="utf-8") as f:
            f.write(texto.replace(viejo, nuevo, 1))
    return fabricar


def borrar(ruta):
    def fabricar(raiz):
        p = os.path.join(raiz, ruta)
        if os.path.isdir(p):
            import shutil
            shutil.rmtree(p)
        else:
            os.remove(p)
    return fabricar


def sin_cambios(raiz):
    pass


def correr_controles(medir, controles):
    todo_bien = True
    for nombre, fabricar, esperado in controles:
        with tempfile.TemporaryDirectory() as tmp:
            fabricar_instancia_sana(tmp)
            try:
                fabricar(tmp)
                estado, hallazgos = medir(tmp)
            except Exception as e:  # un control que no pudo armarse es un control que no corrió
                estado, hallazgos = None, [f"el control se rompió: {e}"]
        ok = estado == esperado
        todo_bien &= ok
        marca = "ok " if ok else "MAL"
        obtenido = NOMBRE_ESTADO.get(estado, "nada")
        print(f"  [{marca}] {nombre}: esperaba «{NOMBRE_ESTADO[esperado]}», dio «{obtenido}»")
        if not ok:
            for h in hallazgos:
                print(f"        {h}")
    return LIMPIO if todo_bien else NO_PUDE


def correr(medir, controles):
    args = sys.argv[1:]
    if args and args[0] == "--controles":
        sys.exit(correr_controles(medir, controles))
    raiz = os.path.abspath(args[0]) if args else RAIZ_REPO
    try:
        estado, hallazgos = medir(raiz)
    except Exception as e:  # un traceback sale con 1, y se leería como un hallazgo: es un 2
        estado, hallazgos = NO_PUDE, [f"el gate se rompió midiendo: {e!r}"]
    for h in hallazgos:
        print(f"  - {h}")
    print(f"  => {NOMBRE_ESTADO[estado]}")
    sys.exit(estado)
