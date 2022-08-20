from PIL import Image, ImageDraw, ImageFont
import os

DIR = 'C:/Windows/Fonts'

FONTS = [
    ['BASKVILL.TTF', 'Barkerville', 1768],
    ['COPRGTL.TTF', 'Cooperplate Gothic', 1901],
    ['GARA.TTF', 'Garamond', 1919],
    ['COOPBL.TTF', 'Cooper Black', 1921],
    ['BAUHS93.TTF', 'Bauhaus 93', 1993],
    ['BRLNSR.TTF', 'Berlin Sans', 1994],            # Furtura 1927 の代わり
    ['ROCK.TTF', 'Rockwell', 1934],
    # Optima 1952
    ['arial.ttf', 'Arial', 1982],                   # Helvetica 1957 の代わり
    ['LCALLIG.TTF', 'Lucida Calligraphy', 1992],    # Lucida Blackletter 1985 
    # DIN 1987
    ['wingding.ttf', 'Wingdings', 1990],            # 謎の記号文字の代わり
    ['ITCEDSCR.TTF', 'ITC Edwardian Script', 1994], # Zapfino 1998 の代わり
    ['GOTHIC.TTF', 'Century Gothic', 1991],         # Gotham 2000 の代わり
    # テクネフォント 2012
]

TEXT = 'PYTHON PILLOW'
FONT_SIZES = [72, 48, 48]
POSITIONS =  [(640, 358), (640, 471), (640, 539)]   # タイトル、フォント名、年号の順


# フォントファイルのフルパスのリストを作成する。オブジェクトは第3要素の年号順に並べる。
# 数値の年号は描画のために文字列に変更する。
f_sorted = sorted(FONTS, key=lambda elem: elem[2]) 
fonts = [[os.path.join(DIR, elem[0]), elem[1], str(elem[2])] for elem in f_sorted]

# 台紙画像を用意
img = Image.open('Images/Desktop.jpg')

# フォント分のループ
imgs = []

for elem in fonts:
    img_draw = img.copy()                           # コピーを生成
    draw = ImageDraw.Draw(img_draw)
    filepath, fontname, year = elem
    text = [TEXT, fontname, year]

    # タイトル、フォント名、年号の順に異なるフォントサイズで描画する
    for idx in range(len(POSITIONS)):
        size = FONT_SIZES[idx]
        pos = POSITIONS[idx]
        txt = text[idx]
        font = ImageFont.truetype(filepath, size=size)
        draw.text(pos, txt, font=font, fill='black', anchor='mm')

    imgs.append(img_draw)

# 保存
imgs[0].save(
    'FontHistory.gif',
    save_all=True,
    append_images=imgs[1:],
    duration=500,                                   # ミリ秒
    loop=1,                                         # ループ回数
    comment='Font history'
)
