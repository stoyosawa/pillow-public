from PIL import Image, ImageFilter, ImageOps
from pil_draw import make_canvas                    # 6.8節
from os.path import basename
from sys import argv

img = Image.open(argv[1])
reduced = ImageOps.contain(img, (300, 300))         # 大きいと遅いので...
reduced.filename = basename(img.filename)

imgs = [reduced]
for size in range(3, 24, 5):
    print(size)
    mode_filter = ImageFilter.ModeFilter(size=size)
    filtered = reduced.filter(mode_filter)
    filtered.filename = str(size)
    imgs.append(filtered)

canvas = make_canvas(imgs)
canvas.show()
