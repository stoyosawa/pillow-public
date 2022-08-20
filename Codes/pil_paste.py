from PIL import Image
from sys import argv

# 温泉サル画像 ... 顔の領域データは手作業で入手。
dst = Image.open('MonkeyBath.jpg')
dst_face_size = (158, 158)                          # サル顔領域
dst_face_corner = (518, 497)                        # サル顔領域の左上座標

# スマイリー画像 ... バウンディングボックスに従ってトリムし、上記のサイズに合わせる
src_orig = Image.open('Smily.png')
src_bbox = src_orig.getbbox()
src_box = src_orig.crop(src_bbox)
src = src_box.resize(dst_face_size)
src.show()

# 貼り付け
dst.paste(src, box=dst_face_corner)                 # in-place操作
dst.show()
