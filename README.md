# tiny-chess-entry

An original chess engine squeezed into 4 KB of Python: negamax search
with alpha-beta pruning, a transposition table, null-move pruning and
quiescence, run to a fixed node budget (fully deterministic). The
readable source is lzma-compressed and base85-armored across main.py
and payload.py behind a small self-extracting loader.

Run: MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 -P -s main.py
