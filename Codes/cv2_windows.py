from PIL import Image
import cv2
import numpy as np

for color in ['black', 'grey', 'linen', 'olive', 'coral']:
    img = Image.new('RGB', (300, 300), color=color)

    # 変換
    src = np.array(img)
    src = cv2.cvtColor(src, cv2.COLOR_RGB2BGR)

    # 表示
    cv2.imshow(color, src)

cv2.waitKey(0)
