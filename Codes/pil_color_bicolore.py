from PIL import Image
from sys import argv


def  make_twocolored(img, alpha=0.3):
    '''
    モードをCMYKに変換したのち、Yの情報をCとMにやや混ぜる。
    YとKには真っ白画像（0）を挿入する。
    '''
    cmyk = img.convert('CMYK')                      # CMYKに変換
    c, m, y, k = cmyk.split()                       # まずは分離
    
    c = Image.blend(c, y, alpha=alpha)              # CとYを混ぜる
    m = Image.blend(m, y, alpha=alpha)              # MとYを混ぜる
    zero = Image.new('L', img.size, color=0)        # YとKに挿入する0画像
    twocolor = Image.merge('CMYK', [c, m, zero, zero])
    return twocolor.convert('RGB')


if __name__ == '__main__':
    img = Image.open(argv[1])
    alpha = float(argv[2])
    twocolor = make_twocolored(img, alpha)
    twocolor.show()
