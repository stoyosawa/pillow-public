from PIL import Image
from sys import argv

img = Image.open(argv[1])                           # ファイルを開く
img = img.rotate(90)                                # 画像を操作（詳細はあとで）
img.save('new.png')                                 # 保存
