from PIL import Image, ImageDraw, ImageFont
from random import randrange
import math


mode = 'RGB'
side = 100
points = ((20, 20), (side-20, 20), (20, side-20), (side-20, side-20))
font = ImageFont.truetype('C:/Windows/Fonts/meiryo.ttc', size=12)


graphics = [
    ['ランダム点1000個',
    lambda d: d.point([(randrange(side), randrange(side))
                      for i in range(1000)], fill='white')],
    ['対角線',
    lambda d: d.line((0, 0, side-1, side-1), fill='LightBlue')],
    ['太い単一線',
    lambda d: d.line((0, 0, side-1, 0), fill='HotPink', width=side)],
    ['折れ線',
    lambda d: d.line(points, fill='GreenYellow', width=10)],
    ['折れ線（角丸め）',
    lambda d: d.line(points, fill='GreenYellow', width=10, joint='curve')],
    ['長方形',
    lambda d: d.rectangle((20, 20, side-20, side-20), fill='orchid',
                          outline='aquamarine', width=10)],
    ['長方形（角丸め）',
    lambda d: d.rounded_rectangle((20, 20, side-20, side-20), radius=10,
                                  fill='orchid', outline='aquamarine', width=5)],
    ['多角形（交差あり',
    lambda d: d.polygon(points, fill='tan', outline='SaddleBrown', width=4)],
    ['正6角形',
    lambda d: d.regular_polygon((side//2, side//2, side*2//5), n_sides=6,
                                rotation=30, fill='tan', outline='SaddleBrown')],
    ['楕円',
    lambda d: d.ellipse((10, 20, side-10, side-20), fill='YellowGreen',
                        outline='SeaGreen', width=6)],
    ['円弧',
    lambda d: d.arc((10, 10, side-10, side-10), start=20, end=340,
                    fill='tomato', width=10)],
    ['弦',
    lambda d: d.chord((10, 10, side-10,  side//2), start=60, end=250,
                      fill='DarkSalmon', outline='crimson', width=5)],
    ['パイ',
    lambda d: d.pieslice((10, 10, side-10, side-10), start=-30, end=30,
                         fill='DarkSalmon', outline='crimson', width=5)]
]


def make_canvas(imgs, space=20):
    '''すべて同じサイズと仮定'''
    n = len(imgs)
    n_width = math.ceil(math.sqrt(n))
    n_height = math.ceil(n / n_width)

    w, h = imgs[0].size
    width = space + n_width * (w + space)
    height = space + n_height * (h + space)

    canvas = Image.new(mode, (width, height), color='ivory')
    draw = ImageDraw.Draw(canvas)

    for idx, img in enumerate(imgs):
        x = space + (idx % n_width) * (w + space)
        y = space + (idx // n_width) * (h + space)
        canvas.paste(img, (x, y))
        draw.text((x, y+h+2), img.filename, font=font, fill='black')

    return canvas


if __name__ == '__main__':
    imgs = []
    for gra in graphics:
        comment, runme = gra
        img = Image.new(mode, (side, side), color=0)
        img.filename = comment
        draw = ImageDraw.Draw(img)
        runme(draw)
        imgs.append(img)

    canvas = make_canvas(imgs)
    canvas.show()
