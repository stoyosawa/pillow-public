from PIL import Image, ImageChops, ImageDraw


class ColorMix():
    '''各カラーモデル模式図を生成。座標はあらかじめ計算したものを使用。'''
    def __init__(self):
        self.size = (640, 586)
        self.cordinates = [
            (53, 53, 373, 373),                     # 左上の円
            (266, 53, 586, 373),                    # 右上の円
            (160, 213, 480, 533),                   # 中央下の円
            (86, 59, 554, 527)                      # 中央の円 (HSV用)
        ]
        self.pane_rgb = self.rgb_mix()
        self.pane_hsv = self.hsv_circle()
        self.pane_cmyk = self.cmyk_mix()

        # 混合図を生成
        self.targets = [self.pane_rgb, self.pane_hsv, self.pane_cmyk]
        self.img = self.make_image()


    def rgb_mix(self):
        ''' RGBの3色混合 '''
        rgb = Image.new('RGB', self.size, color='black')

        # 円を3つ描く
        for idx, cord in enumerate(self.cordinates[:3]):
            band = Image.new('RGB', self.size, color='black')
            draw = ImageDraw.Draw(band)
            color = [0, 0, 0]                      # 色は全部0にしておいてから、
            color[idx] = 255                       # 特定のところだけ255にする
            draw.ellipse(cord, fill=tuple(color))
            rgb = ImageChops.add(rgb, band)

        return rgb


    def hsv_circle(self):
        ''' HSV の円環 '''
        # 背景白
        img = Image.new('HSV', self.size, color=(0, 0, 255)) 
        draw = ImageDraw.Draw(img)
        for deg in range(360):
            draw.pieslice(self.cordinates[3], start=deg-90, end=deg-89,
                          fill=(deg*255//359, 255, 255))

        return img.convert('RGB')


    def cmyk_mix(self):
        '''CMYK (4バンド) の、Kを除いた3色混合'''
        cmy = Image.new('CMYK', self.size, color=0)

        for idx, cord in enumerate(self.cordinates[:3]):
            band = Image.new('CMYK', self.size, color=0)
            draw = ImageDraw.Draw(band)
            color = [0, 0, 0, 0]
            color[idx] = 255
            draw.ellipse(cord, fill=tuple(color))
            cmy = ImageChops.add(cmy, band)

        return cmy.convert('RGB')


    def make_image(self):
        count = len(self.targets)
        size = (self.size[0]*count, self.size[1])   # 横一列に画像を並べる
        img = Image.new('RGB', size, color='white')
        for idx, pane in enumerate(self.targets):
            img.paste(pane, (self.size[0]*idx, 0))

        return img


    def get_image(self):
        return self.img


if __name__ == '__main__':
    color_mix = ColorMix()
    img = color_mix.get_image()
    img.show()
