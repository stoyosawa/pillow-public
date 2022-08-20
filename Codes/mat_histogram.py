from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from sys import argv


COLORS = ['red', 'green', 'blue']

def hist_graph(img):
    # ヒストグラムを生成し、RGB単位に分ける
    hist = img.histogram()
    n_bands = len(img.getbands())                   # ループ用。ここでは3。
    hist_rgb = [hist[256*i:256*(i+1)] for i in range(n_bands)]
    x = range(256)

    # ヒストグラムをnmaplotlibで描く
    fig, ax = plt.subplots()
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.title(img.filename)
    for idx in range(n_bands):
        ax.plot(x, hist_rgb[idx], color=COLORS[idx])

    # 画像をImageにエキスポートする
    fig.canvas.draw()
    arr = fig.canvas.buffer_rgba()
    hist_img = Image.fromarray(np.array(arr))

    return hist_img


if __name__ == '__main__':
    img = Image.open(argv[1])
    hist_img = hist_graph(img)
    hist_img.show()
    hist_img.save('mat_hist.png')
