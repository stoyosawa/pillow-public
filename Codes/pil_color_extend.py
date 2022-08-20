from PIL import Image, ImageColor

# フォーマットは R G B ColorName[LF]
# ColorNameには複数単語のものもある
FILE = 'rgb.txt'

def read_colorfile(file=FILE):
    '''rgb.txtを読んで、colorname=#xxxxxx の辞書を作成する。'''
    extension = {}

    with open(file) as fp:
        _ = fp.readline()                           # コメントの先頭行は飛ばす
        for line in fp.readlines():
            r_txt, g_txt, b_txt, name = line.split(maxsplit=3)
            name = name.rstrip().lower()
            r, b, g = [int(c) for c in [r_txt, b_txt, g_txt]]
            hexcode = f'#{r:02x}{g:02x}{b:02x}'     # 小文字16進数
            extension[name] = hexcode

    # 空白入りの名前は重複なので省く
    extension = {k:v for k, v in extension.items() if ' ' not in k}
    # gray = grey の重複を省く (英綴りの方を省くのが妥当か...)
    extension = {k:v for k, v in extension.items() if 'grey' not in k}

    return extension


def extend_colormap(file=FILE):
    '''指定のrgb.txtファイルからImageColor.colormapを拡張する。'''
    extension = read_colorfile(file)
    ImageColor.colormap.update(extension)


if __name__ == '__main__':
    print(f'#colors extended from {len(ImageColor.colormap)} to ', end='')
    extend_colormap()
    print(f'{len(ImageColor.colormap)}')

    # カラー名テスト
    for c in ['green', 'rebeccapurple', 'gray20', 'X11Green']:
        print(f'Testing {c} = ', end='')
        try:
            print(ImageColor.getrgb(c))
        except Exception as e:
            print(f'Not found. {e}')
    