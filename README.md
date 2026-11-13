# tiny-chess-entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/labibhanafi/tiny-chess-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/labibhanafi/tiny-chess-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine squeezed into 4 KB of Python. Negamax search with
alpha-beta pruning and PVS, a transposition table with seeded Zobrist keys,
null-move pruning, late-move reductions, check extensions, killer and history
move ordering, MVV-LVA capture ordering, and a quiescence search over captures
and promotions with evasions when in check. Evaluation is material plus
piece-square tables with a middlegame/endgame king blend, bishop-pair and
passed-pawn terms. The search runs to a fixed node budget (never a clock), so
play is fully deterministic. The readable source is lzma-compressed and packed
into `main.py` behind a small self-extracting loader to meet the size limit;
the engine itself is plain Python 3 standard library.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=daring-harbor-13&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
