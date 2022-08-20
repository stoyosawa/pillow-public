from PIL import Image
from pil_supported_glob import GlobSupportedFiles
from sys import argv
import os

EXT = '.jpg'

read_dir = argv[1]                                  # 対象ファイルのあるディレクトリ
write_dir = os.path.join(read_dir, 'SAVE')          # 保存先
if os.path.isdir(write_dir) is True:
    raise Exception(f'{write_dir} exists. Quit for the time being.')
os.mkdir(write_dir)

files = GlobSupportedFiles(read_dir).get_paths()    # 2.3.1節
for file in files:
    basename = os.path.basename(file)
    new_file = os.path.splitext(basename)[0] + EXT
    new_path = os.path.join(write_dir, new_file)

    img = Image.open(file)
    img = img.convert('RGB')
    img.save(new_path)
    print(f'{file} {basename} => {new_path}')