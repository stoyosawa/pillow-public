from PIL import Image, features
from sys import argv

if features.check('webp_anim') is not True:
    raise Exception(f'WebP not supported on this Pillow version.')

img = Image.open(argv[1])
if img.format != 'GIF' or img.is_animated is not True:
    raise Exception('Input file must be an animated GIF.')

imgs = []
for frame in range(img.n_frames):
    img.seek(frame)
    imgs.append(img.copy())

imgs[0].save('out.webp', save_all=True, append_images=imgs[1:],
             duration=100, loop=2)
