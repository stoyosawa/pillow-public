from PIL import Image
from sys import argv

# 9.1.0対応
#           NEAREST, BOX, BILINEAR, HAMMING, BICUBIC, LANCZOS
RESAMPLES = [0,      4,   2,        5,       3,       1]
SCALE = 4                                           # 4倍する
BOXES = (3, 2)                                      # 画像の貼り付け用の格子

img = Image.open(argv[1])

# 台紙画像の生成
size = [int(x*SCALE*box) for x, box in zip(img.size, BOXES)]
canvas = Image.new(img.mode, size, color=255)

# すべての再標本化方法を試す
new_size = [x*SCALE for x in img.size]
for idx, resample in enumerate(RESAMPLES):
    resized = img.resize(new_size, resample)
    x = new_size[0] * (idx % BOXES[0])
    y = new_size[1] * (idx // BOXES[0])
    canvas.paste(resized, (x, y))

canvas.show()
