from PIL import Image
import numpy as np
import random
import math
from sys import argv

side = 256                                          # 一辺
size = (side, side)                                 # 正方形
area = side * side                                  # 面積
mode = 'L'                                          # [0, 255]のピクセル値
mu = 128                                            # 中央
sigma = 50

class Noise:

    def py_random_noise():
        '''Pythonのランダムノイズ'''
        buf = random.randbytes(area)
        return Image.frombytes(mode=mode, size=size, data=bytes(buf))

    def handmade_noise():
        '''手計算版のガウスノイズ'''
        buf = bytearray(area)
        for i in range(area):
            x = random.randint(0, 256)
            g = math.exp(-(x - mu)**2 / (2 * sigma**2))  # 優先順位は ** > *
            buf[i] = int(g * 255)
        return Image.frombytes(mode=mode, size=size, data=bytes(buf))

    def py_gaussian_noise():
        '''Pythonのガウスノイズ'''
        buf = bytearray(area)
        for i in range(area):
            buf[i] = int(random.gauss(mu, sigma)) % 256
        return Image.frombytes(mode=mode, size=size, data=bytes(buf))

    def np_random_noise():
        '''Numpyのランダムノイズ（離散一様分布）'''
        arr_random = np.random.randint(low=0, high=256, size=size, dtype=np.uint8)
        return Image.fromarray(arr_random, mode)

    def np_gaussian_noise():
        '''Numpyのガウスノイズ'''
        std = mu + sigma * np.random.standard_normal(size=size)
        arr_random = (std * 255).astype(np.uint8)
        return Image.fromarray(arr_random, mode)

if __name__ == '__main__':
    img = getattr(Noise, argv[1])()
    img.show()
