from PIL import Image
from sys import argv

img1 = Image.open(argv[1])                          # 1枚目
img1.show()                                         # ここで停止

img2 = Image.open(argv[2])                          # 1枚目を閉じないと実行されない
img2.show()

