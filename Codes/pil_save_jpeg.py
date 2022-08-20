from PIL import Image, JpegPresets
from sys import argv

img = Image.open(argv[1])
img.save('new.jpg', dpi=(300, 300), quality=5)
