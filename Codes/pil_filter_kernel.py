from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
from sys import argv

FILTERS = {
    # 名称 
    'average':  {
        'kernel': (1, 1, 1, 1, 1, 1, 1, 1, 1),      # 3×3カーネル
        'scale': 9,                                 # スケール（割る数）
        'comment': '平均化フィルタ'                    # コメント
    },
    'gaussian': {
        'kernel': (1, 2, 1, 2, 4, 2, 1, 2, 1),
        'scale': 16,
        'comment': 'ガウシアンフィルタ（重み付け平均化）'
    },
    'prewitt': {
        'kernel': (-1, -1, -1, 0, 0, 0, 1, 1, 1),
        'scale': 1,
        'comment': 'Prewittフィルタ（縦方向）'
    },
    'sobel': {
        'kernel': (-1, 0, 1, -2, 0, 2, -1, 0, 1),
        'scale': 1,
        'comment': 'Sobelフィルタ（横方向）'
    }
}


img = Image.open(argv[1])                           # 元画像ファイル
img = ImageOps.grayscale(img)                       # モノクロ化

filtername = argv[2].lower()                        # 実行するフィルタの名称
kernel = ImageFilter.Kernel(
    size=(3, 3),                                    # サイズはここでは(3, 3)
    kernel=FILTERS[filtername]['kernel'],
    scale=FILTERS[filtername]['scale']
)
img = img.filter(kernel)

font = ImageFont.truetype('C:/Windows/Fonts/msgothic.ttc', size=16)
draw = ImageDraw.Draw(img)
draw.text((10, 10), text=FILTERS[filtername]['comment'],
          font=font, fill=255)

img.show()
