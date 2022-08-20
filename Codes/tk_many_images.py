from PIL import Image, ImageOps, ImageTk
import tkinter as tk
import math
from sys import argv

# とりあえずトッププオブジェクトだけは作る
root = tk.Tk()

# GIFを読む。個々のフレームは大きいのでscale倍する
gif = Image.open(argv[1])
scale = 0.2
size = [int(a*scale) for a in gif.size]

# ジオメトリマネージャで使う升目の数を計算する
n_cols = math.ceil(math.sqrt(gif.n_frames))
n_rows = math.ceil(gif.n_frames // n_cols)

# アニメーションGIFをばらしてPhotoImageのリストにする
imgs_tk = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    resized = ImageOps.scale(gif, scale)
    imgs_tk.append(ImageTk.PhotoImage(resized))

# 画像の数だけCanvasを作る
canvases = []
for frame in range(gif.n_frames):
    canvases.append(tk.Canvas(root, width=size[0], height=size[1]))
    canvases[frame].create_image(0, 0, anchor=tk.NW, image=imgs_tk[frame])

    col = frame % n_cols
    row = frame // n_cols
    canvases[frame].grid(column=col, row=row)

root.mainloop()
