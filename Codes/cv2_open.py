import cv2                                          # OpenCVをインポート
from sys import argv

src = cv2.imread(argv[1])                           # 画像を開く
cv2.imshow(argv[1], src)                            # 表示する
cv2.waitKey(0)                                      # 必須!
