import tkinter as tk
from sys import argv

root = tk.Tk()                                      # メインウィンドウ生成
img = tk.PhotoImage(file=argv[1])                   # 画像を読む
canvas = tk.Canvas(root, width=img.width(),         # キャンバスウィジェット生成
                   height=img.height())
canvas.pack()                                       # キャンバス配置
canvas.create_image(0, 0, anchor=tk.NW, image=img)  # 画像貼り付け
root.mainloop()                                     # イベントループ

print('Completed')