from PIL import Image, ImageOps
from sys import argv

def outer(b_range=[0, 80], flip=True):

    def make_mask(pix):
        p = 255
        if pix >= b_range[0] and pix < b_range[1]:  # 暗いところは0
            p = 0
        if flip:
            p = 255 - p
        return p

    return make_mask


fg = Image.open(argv[1])
bg = Image.open(argv[2]).resize(fg.size)

mask = ImageOps.grayscale(fg)
mask = Image.eval(mask, outer([10, 100], False))
bg.paste(fg, mask=mask)
bg.show()
