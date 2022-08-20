from PIL import Image
from sys import argv
import math

def entropy(img):
    hist = img.histogram()
    size = img.width * img.height * len(img.getbands())
    sigma = 0.0
    for h in hist:
        if h != 0:                                  # lim p log(p) = 0
            p = h / size
            sigma += p * math.log2(p)

    return -sigma


if __name__ == '__main__':
    img = Image.open(argv[1])
    lib_e = img.entropy()
    my_e = entropy(img)
    print(lib_e, my_e)
