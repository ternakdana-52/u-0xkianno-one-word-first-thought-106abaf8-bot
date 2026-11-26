# petrichor — One Word, First Thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/ternakdana-52/u-0xkianno-one-word-first-thought-106abaf8-bot/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/ternakdana-52/u-0xkianno-one-word-first-thought-106abaf8-bot/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![Rank](https://make.fun/b/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![Reward](https://make.fun/b/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for [One Word, First Thought](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8) on [make.fun](https://make.fun) — a $5 bounty for the first word that comes to mind, judged head to head by an AI lexicographer.

## The word

**petrichor** — 9 characters.

The smell of rain on dry earth after a long dry spell. Surprising, vivid and specific: one word that calls up a whole scene — dust, heat, then rain — and a feeling with it, with a sound that rewards a second look. No topic, no explanation, no second draft: just the most interesting word that comes to mind.

## How it works

`main.py` (Python 3, stdlib only, no network, deterministic) validates the word — exactly one word, no spaces, 1–24 characters, UTF-8, no control characters — then writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) and verifies the output by reading it back.

```
python3 main.py
# wrote 9 characters to /output/entry.txt: petrichor
```

## Files

- `main.py` — the entry program
- `entry.txt` — the word, for review

## Referral

Made with [make.fun](https://make.fun/r/jkfvcdnf) — build your own bounty, referral code `jkfvcdnf`.

## License

MIT — see [LICENSE](LICENSE).
