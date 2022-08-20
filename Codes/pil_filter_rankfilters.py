from PIL import Image, ImageFilter
from pil_draw import make_canvas                    # 6.8節
from sys import argv

SMOOTH = ['MinFilter', 'MedianFilter', 'MaxFilter', 'ModeFilter']

img = Image.open(argv[1])

imgs = [img]
for smooth in SMOOTH:
    filtered = img.filter(getattr(ImageFilter, smooth)(size=9))
    filtered.filename = smooth
    imgs.append(filtered)

canvas = make_canvas(imgs)
canvas.show()
