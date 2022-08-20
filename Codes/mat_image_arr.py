import matplotlib.pyplot as plt
import numpy as np

# 垂直グラデーションをNumpyで生成
shape = (200, 200, 3)                               # RGBカラー
arr = np.empty(shape, dtype=np.uint8)
ratio = 255 / shape[0]
for i in range(shape[0]):                           # 縦方向のループ
    arr[i, :, :] = int(ratio * i)                   # y=iの位置の色
  
plt.imshow(arr)                                     # np.ndarrayをそのまま貼り付け
plt.savefig('mat_img_arr.png')
plt.show()
