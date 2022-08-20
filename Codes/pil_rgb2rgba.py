from PIL import Image
import numpy as np
from sys import argv

def rgb2rgba(img):
    # 全体をやや透過 (80% = 204) の行列を生成
    alpha = np.ones((img.height, img.width), dtype=np.uint8) * 204
    # (419, 88,862, 676) の領域を不透過 (100% = 255) にする
    alpha[88:676, 419:862] = 255
    # Lモードの画像にする
    alpha_L = Image.fromarray(alpha, mode='L')

    # alpha_Lをimgに加える
    img.putalpha(alpha_L)
    img.filename = img.filename + '.alpha'
    return img


if __name__ == '__main__':
    rgb = Image.open('Images/Frame.png')
    print(f'{rgb.filename}: Mode {rgb.mode}.')
    rgba = rgb2rgba(rgb)
    print(f'{rgba.filename}: Mode {rgba.mode}.')
    rgba.save('Images/Frame-RGBA.png')
