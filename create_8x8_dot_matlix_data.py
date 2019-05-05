from PIL import Image, ImageDraw, ImageFont
import numpy as np


SIZE = 8
FONT = ImageFont.truetype('~/Library/Fonts/misaki_gothic.ttf', SIZE)
TEXT_COLOR = "white"

HEX = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]


def main():
    text = list(input())
    print(text)
    length = len(text)

    for i in range(length):
        im = Image.new("L", (SIZE, SIZE), 0)
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), text[i], font=FONT, fill=TEXT_COLOR)

        np_image = np.array(im)
        np_rotated = np.rot90(np_image, k=-1)

        hex_matrix = toHex(np_rotated)
        print(totalMatrix(hex_matrix))


def toHex(matrix):
    np_hex = np.copy(matrix)
    np_text = np.where(matrix == 255)
    length = len(np_text[0])

    for i in range(length):
        x = np_text[0][i]
        y = np_text[1][i]

        np_hex[x][y] = HEX[y]

    return np_hex


def totalMatrix(hex_matrix):
    total_hex = np.sum(hex_matrix, axis=1)
    length = len(total_hex)

    hexed_array = []

    for i in range(length):
        hexed = hex(total_hex[i])

        if (len(hexed) < 4):
          hexed = "0x0" + hexed[2]

        hexed_array.append(hexed)

    return hexed_array


if __name__ == "__main__":
    main()
