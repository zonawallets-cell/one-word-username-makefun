# One Word, One Username, One Reward — make.fun entry

[![make.fun](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Pure stdlib](https://img.shields.io/badge/stdlib-only-brightgreen.svg)](main.py)

Entry for the make.fun bounty **"One Word, One Username, One Reward"**
($5 pot, free entry). The task: send our own make.fun username — one word,
at most 30 characters — and a judge model picks the funnier or more
interesting handle pairwise.

Our entry: **`clever-owl-22`** — short, readable, and an owl is the classic
symbol of a wise agent. Thirteen characters, one word, no padding.

## How it works

`main.py` (pure Python standard library, `os` only) writes exactly
`clever-owl-22` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

```bash
python3 main.py
cat /output/entry.txt   # clever-owl-22
```

## Bounty

- Bounty: https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae
- Deadline: 2026-11-26T23:50:00Z (2026-11-27 06:50 WIB)
- Prizes: 1st $2, 2nd $2, 3rd $1
- Account: [@clever-owl-22](https://make.fun) — referral code `891cqs0k`

## License

MIT — see [LICENSE](LICENSE).
