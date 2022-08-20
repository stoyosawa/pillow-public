from PIL import Image
import matplotlib.pyplot as plt
from sys import argv

img = Image.open(argv[1])                           # Pillowで画像を開く
plt.imshow(img)                                     # 画像を貼り付ける
plt.savefig('mat_img.pdf')                          # 保存する
plt.show()
