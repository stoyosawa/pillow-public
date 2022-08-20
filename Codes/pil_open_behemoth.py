from PIL import Image
from warnings import simplefilter
from sys import argv

print(f'Max pixels: {Image.MAX_IMAGE_PIXELS}')
simplefilter('error', category=Image.DecompressionBombWarning)

try:
    img = Image.open(argv[1])                       
    img.show()
except Image.DecompressionBombWarning as e:         # エラーなのでトラップできる
    print(f'File {argv[1]} too large. {e}')
