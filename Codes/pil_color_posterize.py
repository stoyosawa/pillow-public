from PIL import Image
from sys import argv

def posterize(img, colors=64):
    conv = 256 // colors                            # 1区間の数
    hsv = img.convert('HSV')                        # HSVに変換

    # バンド単位に、区間内のピクセル値を区間先頭の値に変換する
    hsv_bands = hsv.split()
    pixels = [bytearray(img.width * img.height), ] * 3
    for b, band in enumerate(hsv_bands):
        for idx, p in enumerate(band.tobytes()):
            pixels[b][idx] = (p // conv) * conv
        pixels[b] = Image.frombytes('L', size=img.size, data=bytes(pixels[b]))

    hsv = Image.merge('HSV', pixels)
    return hsv.convert('RGB')


if __name__ == '__main__':
    args = {idx:v for idx, v in enumerate(argv[1:])}
    file = args.get(0)                              # ファイル名
    colors = int(args.get(1, 64))                   # 色数（デフォルト64）

    img = Image.open(argv[1])
    poster = posterize(img, colors=colors)
    poster.show()
