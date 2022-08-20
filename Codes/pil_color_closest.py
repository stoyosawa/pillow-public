from PIL import Image, ImageColor
import numpy as np
from sys import argv

def closest_color(rgb):
    '''
    引数に指定したrgbタプルに最も近い色名を探す。
    (距離, 色名) のタプルを返す。
    '''

    # 色名とターゲットrgbとの距離のタプルのリスト
    distances = []
    for c in ImageColor.colormap.keys():            # 色名のループ
        named_color = ImageColor.getrgb(c)          # 色名から(r, g, b)を取得
        d = np.linalg.norm(np.asarray(named_color) - np.asarray(rgb))
        distances.append((d, c))                    # (距離, 色名)タプルのリスト

    # 最も小さい距離の色
    distances.sort(key=lambda x:x[0])
    return distances[0]


if __name__ == '__main__':
    r, g, b = [int(c) for c in argv[1:]]
    closest = closest_color((r, g, b))
    print(closest)
