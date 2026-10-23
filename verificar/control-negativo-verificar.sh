#!/usr/bin/env bash
# El control negativo del agregador. verificar.sh junta estados, y un agregador que junta mal
# dice "está todo bien" cuando no vio. Este script lo corre contra gates de mentira, en una
# carpeta temporal, y exige el estado correcto en cada caso. Exit 0 si todos dan lo esperado.

set -u
origen="$(cd "$(dirname "$0")" && pwd)/verificar.sh"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/verificar/gates"
cp "$origen" "$tmp/verificar/"

gate() {  # gate <nombre> <exit normal> <exit de --controles>
  printf 'import sys\nsys.exit(%s if sys.argv[1:] == ["--controles"] else %s)\n' "$3" "$2" \
    > "$tmp/verificar/gates/$1.py"
}
limpiar() { rm -f "$tmp"/verificar/gates/*.py; }

fallas=0
esperar() {  # esperar <estado> <descripción>
  bash "$tmp/verificar/verificar.sh" >/dev/null 2>&1
  r=$?
  if [ "$r" -eq "$1" ]; then echo "  [ok ] $2: $r"
  else echo "  [MAL] $2: esperaba $1, dio $r"; fallas=1
  fi
}

limpiar; gate a 0 0;                       esperar 0 "todos limpios da limpio"
limpiar; gate a 0 0; gate b 1 0;           esperar 1 "un hallazgo y el resto limpio da 1"
limpiar; gate a 2 0; gate b 1 0; gate c 0 0; esperar 2 "el 2 pisa al 1 y al 0"
limpiar; gate a 1 0; gate z 2 0;           esperar 2 "el 2 pisa aunque llegue último"
limpiar; gate a 0 1;                       esperar 2 "un gate cuyos controles no fallan es un 2"
limpiar; gate a 7 0;                       esperar 2 "un exit raro no se lee como hallazgo"
limpiar; gate _ayuda 1 1; gate a 0 0;      esperar 0 "los archivos con _ no son gates"
limpiar;                                   esperar 2 "sin gates no hay verde"

exit "$fallas"
