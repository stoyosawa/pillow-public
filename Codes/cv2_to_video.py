from PIL import Image
import cv2
import numpy as np
from sys import argv

# 画像をPillow側で開く
img = Image.open(argv[1])

# OpenCVの動画書き出しオブジェクトを用意する
fourcc = cv2.VideoWriter_fourcc(*'MP42')
rec = cv2.VideoWriter('video.avi', fourcc, 2, img.size)

# GIFのフレーム単位に処理する
for fid in range(img.n_frames):
    img.seek(fid)
    frame = img.convert('RGB')                      # PからRGBへ

    # BGR形式の行列に変換
    frame = Image.merge('RGB', list(reversed(frame.split())))
    arr = np.array(frame)

    # 書き出し
    rec.write(arr)

# 必須!
rec.release()
