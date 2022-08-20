from PIL import Image, ImageColor, ImageDraw, ImageFont
import cv2
import numpy as np
from sys import argv

# OpenCVで画像を開く
bgr = cv2.imread(argv[1])

# BGRからRGBに変換し、PillowのImageオブジェクトに変換する
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
img = Image.fromarray(rgb)

# Pillowで文字列描画
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', size=48)
draw.text((20, 10),'いい湯旅立ち', font=font, fill='DarkOrange')

# OpenCV画像（np.ndarray）に戻し、BGRにする
rgb = np.array(img)
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

# OpenCVで表示し、保存
cv2.imshow(argv[1], bgr)
cv2.imwrite('sample.png', bgr)
cv2.waitKey(0)
