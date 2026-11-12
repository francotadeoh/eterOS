#!/usr/bin/env bash
# Arma el archivo de eterOS (.zip) que se entrega sin GitHub.
# Uso: bash empaquetar/armar-archivo.sh [carpeta-de-salida]
# Sale: eteros-v<version>.zip con skills/, NOVEDADES.md e INSTALAR.md.
# Solo empaqueta lo que está versionado en git: nada de _build/, ni .env, ni archivos sueltos.
set -euo pipefail

raiz="$(cd "$(dirname "$0")/.." && pwd)"
salida="${1:-$raiz}"
cd "$raiz"

version="$(grep -m1 -o 'Versión de este método: v[0-9.]*' skills/eteros/SKILL.md | sed 's/.*: //')"
novedades="$(grep -m1 -o '^## v[0-9.]*' NOVEDADES.md | sed 's/## //')"
if [ -z "$version" ] || [ "$version" != "$novedades" ]; then
  echo "ROJO: la versión del skill ($version) no coincide con NOVEDADES.md ($novedades)." >&2
  exit 1
fi
if [ -n "$(git status --porcelain -- skills NOVEDADES.md empaquetar)" ]; then
  echo "ROJO: hay cambios sin commitear en skills/, NOVEDADES.md o empaquetar/. Commiteá antes de armar." >&2
  exit 1
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
dest="$tmp/eteros"
mkdir -p "$dest"
git archive HEAD skills NOVEDADES.md | tar -x -C "$dest"
cp empaquetar/INSTALAR.md "$dest/INSTALAR.md"

archivo="$salida/eteros-$version.zip"
rm -f "$archivo"
(cd "$tmp" && zip -qr "$archivo" eteros)
echo "listo: $archivo"
