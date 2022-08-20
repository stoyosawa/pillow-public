from PIL import Image, ImageOps
from sys import argv

B_RANGE = [0, 80]                                   # 黒の範囲
FLIP = True                                         # 白黒反転

def make_mask(pix):
    p = 255
    if pix >= B_RANGE[0] and pix < B_RANGE[1]:      # 暗いところは0
        p = 0
    if FLIP:
        p = 255 - p

    return p


fg = Image.open(argv[1])
bg = Image.open(argv[2]).resize(fg.size)

mask = ImageOps.grayscale(fg)
mask = Image.eval(mask, make_mask)
bg.paste(fg, mask=mask)
bg.show()
