from PIL import Image
from sys import argv

mosaic = (32, 32)

# 第1引数は画像ファイル、第2～5引数がモザイク化する領域の矩形座標。
filename = argv[1]
from_box = [int(x) for x in argv[2:]]               # 第2以降の引数を整数化
from_size = (from_box[2]-from_box[0], from_box[3]-from_box[1])

# 画像を読み、指定領域を切り出す
img = Image.open(filename)
region = img.crop(from_box)

# 指定領域を次のサイズに縮小する
to_size = [a//b for a, b in zip(from_size, mosaic)]
region = region.resize(to_size) 

# NEAREST（直値0）でもとのサイズに戻して、もとの位置に貼り付ける。
region = region.resize(from_size, resample=0)
img.paste(region, from_box)

img.show()
