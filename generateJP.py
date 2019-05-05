from PIL import Image, ImageDraw, ImageFont
import numpy as np

SIZE = 8
FONT = ImageFont.truetype('~/Library/Fonts/misaki_gothic.ttf', SIZE)
TEXT_COLOR = "white"

JP_LA = 12353 # ぁ
JP_NN = 12435 # ん

for i in range(JP_LA, JP_NN + 1):
    im = Image.new("L", (SIZE, SIZE), 0)
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), chr(i), font=FONT, fill=TEXT_COLOR)
    im.save("./text/%d.png" % i)

    # hoge = np.array(im)
