from PIL import Image
import cv2
import numpy as np
from sys import argv

# Pillowで読む
img = Image.open(argv[1]) 

# RGBをBGRにしてから、OpenCV画像（np.ndarray）に変換する
img = Image.merge('RGB', list(reversed(img.split())))
cols, rows = img.size
src = np.array(img)

# OpenCVで画像処理
dst = cv2.stylization(src)

# Pillow画像に戻し、BGRからRGBに変換
img = Image.fromarray(dst)
img = Image.merge('RGB', list(reversed(img.split())))

# Pillowで表示
img.show()
