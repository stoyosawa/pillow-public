from PIL import Image, ImageDraw, ImageFont

fontfile = 'C:/Windows/Fonts/msgothic.ttc'              # MS UI Gothic 標準
text = 'Windows でコンピュータの世界がひろがります。1234567890'

# 同じファミリで異なるサイズのフォントオブジェクトを生成する
fonts = []
for points in range(8, 37, 4):
    font = ImageFont.truetype(fontfile, points)
    t = f'{points} {text}'
    _, _, width, height = font.getbbox(t)
    fonts.append({
        'font': font,
        'text': t,
        'width': width,
        'height': height
    })

# 行間スペース
space = 10

# 画像幅は最大フォント（最長）に合わせる。左右のマージンも忘れずに。
width = fonts[-1]['width'] + space * 2
# 高さは全フォント分の和プラス行間スペース
height = sum([f.get('height') for f in fonts]) + space*(len(fonts) + 1)

# 画像を用意
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

x, y = (space, space)
for font in fonts:
    draw.text((x, y), font.get('text'), font=font.get('font'), fill='black')
    y += (font.get('height') + space)

img.show()
