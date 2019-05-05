# text-to-8x8-dot-matlix

## Requirements

- Python 3.x & pip
- virtualenv
- usable Misaki Gothic Font (美咲フォント ゴシック)
  - [Download Link(http://littlelimit.net/)](http://littlelimit.net/)

## Setup

```bash
... Setup virtualenv
$ git clone git@github.com:kobakazu0429/text-to-8x8-dot-matlix.git
$ cd text-to-8x8-dot-matlix
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
$ pip install -r requirements.txt

# if you using Max OS, do not overwrite below.
# but, you using Ubuntu, Windows and others, you have to overwrite Misaki Font PATH

# in editor:
generateJP.py line:5
export_8x8_dot_matlix_data.py line:6

from: `FONT = ImageFont.truetype('~/Library/Fonts/misaki_gothic.ttf', SIZE)`
to: `FONT = ImageFont.truetype('/path/to/misaki_gothic.ttf', SIZE)`
```

## Description Files

### generateJP.py

Generate Japanese Hiragana(ぁ〜ん) PNG files in current directory (dist by text/)

### export_8x8_dot_matlix_data.py

you type exporting word: Alphabet, Number, Japanese(Hiragana, Katakana, Kanji(ひらがな, カタカナ, 漢字))
So, export hex numbers.
