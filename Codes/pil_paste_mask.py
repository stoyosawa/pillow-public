from PIL import Image
from sys import argv

def crop(img, size):
    bbox = img.getbbox()
    img = img.crop(bbox)
    img = img.resize(size)
    return img


# 温泉サル画像 ... 顔の領域データは手作業で入手。
dst = Image.open('MonkeyBath.jpg')
dst_face_size = (158, 158)                          # サル顔領域
dst_face_corner = (518, 497)                        # サル顔領域の左上座標

# スマイリー画像とそのマスク画像
src = crop(Image.open('Smily.png'), dst_face_size)
mask = crop(Image.open('SmilyMask.png'), dst_face_size)

# マスク付きで貼り付け
dst.paste(src, box=dst_face_corner, mask=mask)
dst.show()
