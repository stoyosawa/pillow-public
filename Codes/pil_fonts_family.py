from PIL import Image, ImageDraw, ImageFont
import os

img = Image.new('RGB', size=(640, 405), color='white')
draw = ImageDraw.Draw(img)

y = 15
dy = 30

# テストするフォント
font_dir = 'C:/Windows/Fonts/'
fonts_ttf = [
    ['Arial.ttf', 'Arial Normal', 'Latin'],
    ['ARIALNI.TTF', 'Arial Narrow Italic', 'Latin'],
    ['CENTURY.TTF', 'Century Normal', 'Latin'],
    ['consolab.ttf', 'Consola Bold', 'Latin'],
    ['calibrili.ttf', 'Caribrili Narrow Italic', 'Latin'],
    ['GULIM.TTC', 'Gulim Normal', 'Korean'],
    ['HGRGY.TTC', 'HFS行書体ミディアム（リコー）', 'Japanese'],
    ['LTYPE.TTF', 'Lucia Sans Typewriter normal', 'Latin'],
    ['meiryo.ttc', 'メイリオ標準 (MS)', 'Japanese'],
    ['msyh.ttc', 'Microsoft YaHei Normal (簡体)', 'Chinese'],
    ['MINGLIU.TTC', 'MingLiu Normal (繁体)', 'Chinese'],
    ['msmincho.ttc', 'MS P 明朝 標準 (リコー)', 'Japanese'],
    ['UDDigiKyokashoN-R.ttc', 'UDデジタル教科書体NK-R標準 (モリサワ)', 'Japanese']
]

# 言語別の表示テキスト
texts = {
    'Latin': 'Hellow World',
    'Chinese': '你好世界',
    'Korean': '헬로월드',
    'Japanese': 'こんにちは世界',
}

for font in fonts_ttf:
    font_file = os.path.join(font_dir, font[0])
    f = ImageFont.truetype(font_file, size=18)
    draw.text(
        (10, y),
        f'{texts[font[2]]} ({font[1]})',
        font=f,
        fill='black'
    )
    y = y + dy

img.show()
