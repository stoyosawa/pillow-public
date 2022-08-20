from PIL import Image
from sys import argv

img = Image.open(argv[1])                           # 画像を開く
img.show()                                          # 画像を表示
