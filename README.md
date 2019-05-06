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
create_8x8_dot_matlix_data.py line:6

from: `FONT = ImageFont.truetype('~/Library/Fonts/misaki_gothic.ttf', SIZE)`
to: `FONT = ImageFont.truetype('/path/to/misaki_gothic.ttf', SIZE)`
```

## Description Files

### generateJP.py

Generate Japanese Hiragana(ぁ〜ん) PNG files in current directory (dist by text/)

### create_8x8_dot_matlix_data.py

you type creating word: Alphabet, Number, Japanese(Hiragana, Katakana, Kanji(ひらがな, カタカナ, 漢字))
So, create hex numbers.

## Examples

```bash
$ python create_8x8_dot_matlix_data.py
> こばたけ
>
> ['こ', 'ば', 'た', 'け']
> ['0x00', '0x02', '0x25', '0x21', '0x21', '0x21', '0x01', '0x00']
> ['0x7f', '0x00', '0x12', '0x15', '0x55', '0x3e', '0x51', '0x00']
> ['0x21', '0x2e', '0x70', '0x22', '0x15', '0x11', '0x11', '0x00']
> ['0x7e', '0x00', '0x10', '0x11', '0x7e', '0x10', '0x10', '0x00']
```

```bash
$ python create_8x8_dot_matlix_data.py
> 呉高専
>
> ['呉', '高', '専']
> ['0x35', '0x15', '0x74', '0x54', '0x5c', '0x75', '0x05', '0x00']
> ['0x27', '0x24', '0x3f', '0x6d', '0x3f', '0x24', '0x27', '0x00']
> ['0x24', '0x24', '0x3e', '0x7d', '0x3f', '0x24', '0x24', '0x00']
```
