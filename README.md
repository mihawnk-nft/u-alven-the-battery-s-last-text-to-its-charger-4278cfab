# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mihawnk-nft/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/mihawnk-nft/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [The Battery's Last Text to Its Charger](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) competition on [make.fun](https://make.fun).

## What it does

`main.py` writes one final text message — the phone battery's last text
to the charger it waited for all day — to `/output/entry.txt`
(162 characters, under the 200-character cap):

> hey charger, it's 1%. you spent all day with her phone while i died on the nightstand. i'm not begging anymore. i'm leaving you for the power bank. he texts back.

The joke: the battery catches the charger cheating — it spent all day
with *her* phone while the battery died alone on the nightstand — so it
stops begging and leaves the charger for the power bank. The payoff lands
in the last three words: the power bank actually texts back, the charger
never did.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no network, no input, fully deterministic.
