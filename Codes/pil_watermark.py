from PIL import Image, ImageDraw, ImageFont
from sys import argv

FONT = 'C:/Windows/Fonts/arial.ttf'                 # フォントファイル
TEXT = 'From Pixabay'                               # 透かし文字

img = Image.open(argv[1]).convert('RGBA')

# ウォーターマークを描く画像を生成
bg = (255, 255, 255, 0)                             # 完全に透過な白い背景
fg = (0, 0, 0, 16)                                  # 1/16の透過率の黒い前景
overlay = Image.new('RGBA', img.size, color=bg)

# 描画とフォントのオブジェクトを用意
draw = ImageDraw.Draw(overlay)
font = ImageFont.truetype(FONT, size=16)

# 斜めに線を入れる
draw.line((0, 0, img.width-1, img.height-1), fill=fg)
draw.line((img.width-1, 0, 0, img.height-1), fill=fg)

# 文字を入れる
font_size = [a*4 for a in font.getbbox(TEXT)[2:]]   # 実寸の4倍の領域
font_grid = [a//b for a, b in zip(img.size, font_size)]
font_center = [a//2 for a in font_size]

for y in range(font_grid[1]):
    pos_y = y * font_size[1] + font_center[1]
    for x in range(font_grid[0]):
        pos_x = x * font_size[0] + font_center[0]
        draw.text((pos_x, pos_y), TEXT, font=font, fill=fg, anchor='mm')

# 画像にウォーターマーク画像を重ね、RGBに戻す
watermarked = Image.alpha_composite(img, overlay).convert('RGB')

watermarked.show()
