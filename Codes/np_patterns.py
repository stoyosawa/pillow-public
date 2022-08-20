from PIL import Image
import numpy as np
from sys import argv


class ImgPatterns:
    SIZE = (160, 120)                               # 画像のサイズ
    SHAPE =  (SIZE[1], SIZE[0], 3)                  # 行列のシェイプ

    def bw_horizontal_gradation(shape=SHAPE):
        '''
        モノクロ水平グラデーション
        縦方向 (y) は同じ色で、横方向 (x) にだんだん色が薄くなる
        '''
        arr = np.empty(shape, dtype=np.uint8)
        ratio = 255 / shape[1]
        for i in range(shape[1]):                   # 横方向のループ
            arr[:, i, :] = int(ratio * i)           # x=iの位置の色
        return Image.fromarray(arr)


    def bw_vertical_gradation(shape=SHAPE):
        '''
        モノクロ垂直グラデーション
        横方向 (x) は同じ色で、縦方向 (y) にだんだん色が薄くなる
        '''
        arr = np.empty(shape, dtype=np.uint8)
        ratio = 255 / shape[0]
        for i in range(shape[0]):                   # 縦方向のループ
            arr[i, :, :] = int(ratio * i)           # y=iの位置の色
        return Image.fromarray(arr)


    def grid(shape=SHAPE, interval=10):
        '''
        縦横どちらにもinterval毎に白線を引いた格子のモノクロ画像
        '''
        arr = np.zeros(shape, dtype=np.uint8)       # 初期値はすべて0

        # ループをintervalから始めているのは、画像左端と上に白線が欲しくないから
        for i in range(interval, shape[0], interval):     
            arr[i, :, :] = 255
        for i in range(interval, shape[1], interval): 
            arr[:, i, :] = 255
        return Image.fromarray(arr)


    def bw_kujira_maku(shape=SHAPE, n=5):
        '''
        「鯨幕」とは、葬儀で使う幅広い白黒の縦帯。
        白、黒の順。nは白黒の繰り返しの数。
        '''
        obi = shape[1] // n                         # 白と黒の2本分の帯の幅
        w = obi // 2                                # 1本分の幅
        arr = np.zeros(shape, dtype=np.uint8)
        for col in range(0, shape[1], obi):
            arr[:, col:col+w, :] = 255              # 白くする
        return Image.fromarray(arr)


    def joushiki_maku(shape=SHAPE, n=3):
        '''
        「定式幕」は寄席や歌舞伎の舞台の幕。
        市村座では黒、緑、柿色のパターンがn回繰り返される。
        '''
        colors = [
            (255, 255, 255),                        # 黒
            (0, 108, 78),                           # 萌葱
            (180, 89, 52)                           # 柿色
        ]
        obi = shape[1] // n
        w = obi // 3
        arr = np.zeros(shape, dtype=np.uint8)
        for col in range(0, shape[1], obi):
            arr[:, col+w:col+2*w] = colors[1]
            arr[:, col+2*w:col+obi] = colors[2]
        return Image.fromarray(arr)


if __name__ == '__main__':
    img = getattr(ImgPatterns, argv[1])()
    img.show()
