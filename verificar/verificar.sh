#!/usr/bin/env bash
# La verificación pública de eterOS: la que puede correr cualquiera que clone el repo, y la que
# corre GitHub en cada PR.
#
# Corre cada gate de verificar/gates/ dos veces: contra el repo, y con --controles (contra casos
# malos fabricados, donde TIENE que dar rojo). Devuelve un solo estado:
#   0 limpio · 1 encontré algo · 2 no pude medir
# El 2 pisa al 1 y al 0. Un gate cuyos controles no dan lo esperado cuenta como 2: si no falla
# contra el caso malo conocido, su verde no dice nada.
#
# Los gates se descubren solos: cualquier verificar/gates/*.py que no empiece con _ entra.

set -u
export PYTHONDONTWRITEBYTECODE=1
shopt -s nullglob
cd "$(dirname "$0")/.." || exit 2

estado=0
peor() {
  if [ "$1" -eq 2 ] || [ "$estado" -eq 2 ]; then estado=2
  elif [ "$1" -gt "$estado" ]; then estado=$1
  fi
}

gates=()
for g in verificar/gates/*.py; do
  case "$(basename "$g")" in _*) continue ;; esac
  gates+=("$g")
done

if [ "${#gates[@]}" -eq 0 ]; then
  echo "no encontré ningún gate en verificar/gates/: no pude medir"
  exit 2
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "no hay python3: no pude medir"
  exit 2
fi

for g in "${gates[@]}"; do
  nombre=$(basename "$g" .py)

  echo "▸ $nombre"
  python3 "$g" .
  r=$?
  [ "$r" -gt 2 ] && r=2
  peor "$r"

  echo "▸ $nombre --controles"
  python3 "$g" --controles
  c=$?
  [ "$c" -ne 0 ] && c=2
  peor "$c"
  echo
done

case "$estado" in
  0) echo "== limpio: miré todo y no encontré nada" ;;
  1) echo "== encontré algo: está listado arriba" ;;
  *) echo "== no pude medir: una parte no se pudo mirar (o un gate no falla contra su caso malo)" ;;
esac
exit "$estado"
