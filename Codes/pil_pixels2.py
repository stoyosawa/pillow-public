from PIL import Image, ImageOps
from sys import argv

H_RANGE = [
    # 範囲       置き換えの値
    [(10, 20),   15],                               # オレンジっぽい部分
    [(190, 230), 210],                              # 青っぽい部分
    [(250, 350), 300]                               # 赤紫っぽい部分
]

def posterize(pix):
    pix_deg = pix * 359 / 255                       # 角度に直す
    deg = 45                                        # 指定の個所以外は黄色
    for window, replace in H_RANGE:
        if pix_deg >= window[0] and pix_deg < window[1]:
            deg = replace
            break
    p = deg * 255 // 359                            # [0, 255]に戻す

    return p


img = Image.open(argv[1])
h, s, v = img.convert('HSV').split()
h = Image.eval(h, posterize)
img = Image.merge('HSV', (h, s, v)).convert('RGB')
# empty = Image.new('L', img.size, color=255)
# img = Image.merge('HSV', (h, empty, empty)).convert('RGB')
img.show()
