from PIL import Image, ImageGrab

print('Press [Enter] after you copied an image to the clipboard.', end='')
input()

filelist = ImageGrab.grabclipboard()
if filelist == None:
    raise Exception('No data in the clipboard.')

print(f'Files: {", ".join(filelist)}')
img = Image.open(filelist[0])
img.show()
