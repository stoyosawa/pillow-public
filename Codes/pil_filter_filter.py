from PIL import Image, ImageFilter
from pil_draw import make_canvas                    # 6.8節
from sys import argv


# 10種類のImageFilterフィルタ名を取得
FILTERS = [attr for attr in dir(ImageFilter) if attr.isupper()]

img = Image.open(argv[1])

imgs = [img]
for filtername in FILTERS:
    filtered = img.filter(getattr(ImageFilter, filtername))
    filtered.filename = filtername
    imgs.append(filtered)

canvas = make_canvas(imgs)
canvas.show()
