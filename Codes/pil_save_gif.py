from PIL import Image
from sys import argv

img = Image.open(argv[1])

imgs = []
for i in range(12):                                # 30°ずつ12回、回転
    deg = (i + 1) * 30
    imgs.append(img.rotate(deg))

img.save('new.gif', save_all=True, append_images=imgs, duration=500, loop=2)
