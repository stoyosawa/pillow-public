
from PIL import Image
from sys import argv

def get_mode(img):
    hist = img.histogram()                          # ヒストグラム生成

    mode = []
    for idx, band in enumerate(img.getbands()):     # R、G、B単位でループ
        h = hist[idx*256:(idx+1)*256]               # 各色のリストをスライス
        max_value = max(h)                          # 最大値を得る
        location = h.index(max_value)               # その最大値の位置を検索
        mode.append(location)
    return mode


if __name__ == '__main__':
    img = Image.open(argv[1])                       # ファイルを読む
    mode = get_mode(img)
    print(mode)
