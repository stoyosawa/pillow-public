from PIL import Image
from glob import glob
import os
from pil_supported import Supported

class GlobSupportedFiles():
    def __init__(self, directory='.', recurse=False):
        # Pillow がサポートしている画像フォーマットの拡張子リスト（小文字。ドット付き）
        exts = [ext.lower() for ext in Supported().get_extensions()]

        # ディレクトリ下の通常ファイルのリスト
        files = [file for file in glob(f'{directory}/**', recursive=recurse)
            if os.path.isfile(file)]

        # そのうちでも拡張子が含まれるもの
        self.files = [file for file in files
            if os.path.splitext(file)[1].lower() in exts]

    def __len__(self):
        return len(self.files)

    def get_paths(self):
        return self.files


if __name__ == '__main__':
    from sys import argv

    args = {idx:param for idx, param in enumerate(argv[1:])}
    directory = args.get(0, '.')                    # ディレクトリ
    recurse = args.get(1, 'False') == 'True'        # 再帰するか否か

    gsf = GlobSupportedFiles(directory=directory, recurse=recurse)
    print(f'{len(gsf)} files: {gsf.get_paths()}')
