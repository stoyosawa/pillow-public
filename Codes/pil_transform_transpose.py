from PIL import Image
from sys import argv
from pil_transform_thumbnail import thumbnail       # 7.1.5節

TRANSPOSES = ['FLIP_LEFT_RIGHT', 'FLIP_TOP_BOTTOM', 'ROTATE_90', 'ROTATE_180',
    'ROTATE_270', 'TRANSPOSE', 'TRANSVERSE']

imgs = []
imgs.append(Image.open(argv[1]))

# 9.1.0対応のため、直値を使う。
for method in range(len(TRANSPOSES)):
    img = imgs[0].transpose(method)
    img.filename = TRANSPOSES[method]
    imgs.append(img)

thumb = thumbnail(imgs, landscape=True)
thumb.show()
