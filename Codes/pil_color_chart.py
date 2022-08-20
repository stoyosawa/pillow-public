from PIL import Image, ImageColor, ImageDraw

box_size = (130, 20)                                # 1色分の矩形スペース
box_num = (5, 30)                                   # 5×30個の矩形なので、150色分
img_size = [a*b for a, b in zip(box_size, box_num)] # 画像サイズ

# 描画文字関連
text_pos = (5, 4)                                   # 描画文字の左上の位置
text_color = ['white', 'black']                     # 文字色（背景色次第）

# 148色分の矩形を収容する画像
img = Image.new('RGB', img_size, color=(0, 0, 0))

# 全色の名前
colors = ImageColor.colormap.keys()

# 画像に色名の背景色の矩形を順に貼り付けていく。
for idx, c in enumerate(colors):
    box = Image.new('RGB', box_size, color=c)       # この色の矩形

    # 矩形に色名を書く。濃い色では白、薄い色では黒の文字。
    draw = ImageDraw.Draw(box)
    text_color_idx = ImageColor.getcolor(c, mode='L') // 128
    draw.text(text_pos, c, fill=text_color[text_color_idx])

    row = (idx % box_num[0]) * box_size[0]          # 矩形のx位置
    col = (idx // box_num[0]) * box_size[1]         # 矩形のy位置
    img.paste(box, (row, col))

img.show()

