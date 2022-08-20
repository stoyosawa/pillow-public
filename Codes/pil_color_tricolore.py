from PIL import Image, ImageOps
from sys import argv

def tricolore(img):
    # RGBモードでなければ変換する
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # 合成用の黒画像
    black = Image.new('L', img.size, color=0)

    # 分解し、それぞれ1モードだけ元画像から採り、あとは黒画像を挟んでRGBを生成する
    r, g, b = img.split()
    rgb = [img]
    rgb.append(Image.merge('RGB', [r, black, black]))
    rgb.append(Image.merge('RGB', [black, g, black]))
    rgb.append(Image.merge('RGB', [black, black, b]))

    # 元画像も含めて4枚の画像を収容する台紙画像
    canvas = Image.new('RGB', (img.width*2, img.height*2))
    for idx, x in enumerate(rgb):
        canvas.paste(x, ((idx%2)*img.width, (idx//2)*img.height))

    # あまりに大きいと見にくいので、limitを限度に縮小する
    limit = 1280
    if canvas.width > limit or canvas.height > limit:
        canvas = ImageOps.contain(canvas, (limit, limit))

    return canvas


if __name__ == '__main__':
    img = Image.open(argv[1])
    canvas = tricolore(img)
    canvas.show()