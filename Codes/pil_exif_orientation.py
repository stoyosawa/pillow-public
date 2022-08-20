from PIL import Image, ImageOps
from sys import argv

img = Image.open(argv[1])                           # 画像読み込み
img.show()

img_view = ImageOps.exif_transpose(img)             # 回転反転操作
img_view.show()
