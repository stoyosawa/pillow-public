from PIL import Image, ImageDraw, ImageFont
from sys import argv


def anchor_demo(font, text, anchor='la', space=10):
    # 画像サイズを決定して、画像オブジェクトを生成する
    text_size = font.getbbox(text)[2:]
    img_size = [(a+space)*2 for a in text_size]
    img = Image.new('RGB', img_size, color='black')

    # 中央を通る軸を描く
    center = [a//2 for a in img_size]
    draw = ImageDraw.Draw(img)
    draw.line((0, center[1], img.width-1, center[1]), fill='white', width=1)
    draw.line((center[0], 0, center[0], img.height-1), fill='white', width=1)

    # 中央にアンカーポイントを描く
    draw.ellipse((center[0]-2, center[1]-2, center[0]+2, center[1]+2),
                 fill='orange')

    # 文字を描く
    draw.text(center, text, font=font, anchor=anchor)

    return img

if __name__ == '__main__':
    from sys import argv

    font = ImageFont.truetype('C:/Windows/Fonts/BASKVILL.TTF', size=72)
    text = 'Quick'

    img = anchor_demo(font, text, anchor=argv[1])
    img.show()
