from PIL import Image, ExifTags
from sys import argv

img = Image.open(argv[1])
exif = img.getexif()                                # 6.0以上

for num, value in exif.items():                     # ループできる（イテレーション可）
    if num in ExifTags.TAGS:
        name = ExifTags.TAGS[num]
    else:
        name = 'Undefined'
    print(f'{name}({num}): {value}')
