import tkinter as tk
from PIL import Image, ImageTk
from sys import argv

root = tk.Tk()

img_pil = Image.open(argv[1])                       # Pillowで画像を読み込む
img_tk = ImageTk.PhotoImage(img_pil)                # PhotoImageに変換

canvas = tk.Canvas(root, width=img_pil.width, height=img_pil.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
root.mainloop()
