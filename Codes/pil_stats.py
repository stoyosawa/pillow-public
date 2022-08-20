from PIL import Image, ImageStat
from sys import argv

img = Image.open(argv[1])                           # ファイルを読む
stat = ImageStat.Stat(img)                          # Statオブジェクトを生成

for s in ['extrema', 'count', 'sum', 'sum2', 'mean', 
          'median', 'rms', 'var', 'stddev']:
    print(f'{s}: {getattr(stat, s)}')

# extreama は関数版もある
print(f'Image.getextreama: {img.getextrema()}')
