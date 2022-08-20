from PIL import Image, ImageDraw
from sys import argv
import math
from os.path import basename
from pil_supported_glob import GlobSupportedFiles   # 2.3.1節のファイルリスト


def thumbnail(imgs, side=100, space=20, landscape=False):

    n_width = math.floor(math.sqrt(len(imgs)))      # 横のサムネイルの個数
    n_height = math.ceil(len(imgs) / n_width)       # 縦のサムネイルの個数
    if landscape is True:
        n_width, n_height = n_height, n_width

    width = space + n_width * (side + space)        # 台紙横幅
    height = space + n_height * (side + space)      # 台紙高さ

    # 台紙用に背景が真っ白な画像を用意する
    canvas = Image.new('RGB', (width, height), color='white')

    for idx, thumb in enumerate(imgs):
        thumb.thumbnail((side, side), resample=1)   # Image.Resampling.LANCZOS
        # (side, side) の矩形の位置の決定
        x = space + (idx % n_width) * (side + space) 
        y = space + (idx // n_width) * (side + space)
        # 台紙にサムネイルを張り付け。縦横のスペースの分は補正する。
        canvas.paste(thumb, (x+(side-thumb.width)//2, y+(side-thumb.height)))
        # ファイル名を描画
        maxlen = side // 6                          # 最大文字数
        name = basename(thumb.filename)[:maxlen]
        draw = ImageDraw.Draw(canvas)
        draw.text((x, y+side), name, fill='DarkBlue')

    return canvas


if __name__ == '__main__':
    gsf = GlobSupportedFiles(argv[1])
    imgs = [Image.open(file) for file in gsf.get_paths()]
    contact_sheet = thumbnail(imgs, landscape=True)
    contact_sheet.show()
