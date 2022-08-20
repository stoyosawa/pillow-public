from PIL import Image, ImageColor
import numpy as np
from sys import argv

def distance(source, target):
    '''Numpyを使ってsourceとtargetの色間の距離を計算する。'''
    arr_s = np.asarray(source)
    arr_t = np.asarray(target)
    d = np.linalg.norm(arr_s - arr_t)
    return d                                       # 戻り値はfloat


def swap_color(img, select='white', target='black', threshold=50.0):
    select = ImageColor.getrgb(select)              # 色名を(r, g, b)に直す
    target = ImageColor.getrgb(target)              # 同上

    palette = img.getpalette()                      # パレット取得
    palette_new = []                                # 入れ替え後のパレット

    for idx in range(0, len(palette), 3):
        p = palette[idx:idx+3]
        d = distance(p, select)
        if d <= threshold:
            print(f'Found {select} ({d:.3f}). Replacing {p} to {target}')
            p = target
        palette_new.extend(p)

    img_new = img.copy()
    img_new.putpalette(palette_new)                 # 画像にパレットを仕込む

    return img_new


if __name__ == '__main__':
    # 例によって、easy-goingな引数処理
    args = {idx:param for idx, param in enumerate(argv[1:])} 
    file = args.get(0)                              # デフォルトはなし
    select = args.get(1, 'sienna')                  # 変換する色
    target = args.get(2, 'red')                     # 変換先の色
    threshold = float(args.get(3, 50.0))            # 閾値

    img = Image.open(file)
    if img.mode != 'P':
        raise Exception('Not P.')

    img_new = swap_color(img, select=select, target=target, threshold=threshold)
    img_new.show()
