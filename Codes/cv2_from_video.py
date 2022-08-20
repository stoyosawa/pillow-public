from PIL import Image
import cv2
from sys import argv

cap = cv2.VideoCapture(argv[1])
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))   # 総フレーム数
period = int(1000 / cap.get(cv2.CAP_PROP_FPS))      # フレーム周期

total = 24                                          # GIFに収容するフレーム数
interval = n_frames // total                        # 収容フレームの間隔
imgs = []

for f in range(n_frames):
    ret, src = cap.read()
    if f % interval == 0:
        bgr = Image.fromarray(src)
        rgb = Image.merge('RGB', list(reversed(bgr.split())))
        imgs.append(rgb)

    cv2.imshow('video', src)
    if cv2.waitKey(period) == 27:
        break

imgs[0].save('video.gif', save_all=True, append_images=imgs[1:], duration=500)
