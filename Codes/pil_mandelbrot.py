from PIL import Image

def MandelbrotByHand(size, extent, quality, mode='RGB'):
    imgx, imgy = size                               # 画像サイズ
    xa, ya, xb, yb = extent                         # 探索範囲の複素数
    x_coeff = (xb - xa) / (imgx - 1)                # 探索範囲を画面サイズに
    y_coeff = (yb - ya) / (imgy - 1)                # 合わせるための係数

    # 色（適当に決めています）
    color = {
        'L': lambda i: 255 - i*255//quality,
        'RGB': lambda i: (
            i % 4 * 64,                             # R
            i % 8 * 32,                             # G
            i % 16 * 16                             # B
        )
    }[mode]

    img = Image.new(mode, size, color='black')

    for y in range(imgy):                           # 画像縦方向のループ
        cy = y * y_coeff  + ya                      # 虚部の数値に直す
        for x in range(imgx):                       # 画像横方向のループ
            cx = x * x_coeff + xa                   # 実部の数値に直す
            c = complex(cx, cy)                     # 虚数cを生成
            z = 0                                   # z(0)は 0
            for i in range(quality):                # 品質でのループ
                if abs(z) > 2.0:                    # 発散する
                    break                           # ので、これは集合要素ではない
                z = z * z + c 
            img.putpixel((x, y), color(i))          # 集合要素である

    return img


if __name__ == '__main__':
    size = (400, 400)
    extent =  (-2.0, -1.5, 1.0, 1.5)              # 図1
    # extent =  (-1.38, 0.14, -0.91, 0.61)          # 図2
    # extent =  (-1.36, -0.18, -1.22, -0.02)        # 図3
    quality = 20

    img = MandelbrotByHand(size, extent, quality)
    img.show()
