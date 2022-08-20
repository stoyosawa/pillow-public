from PIL import Image, ImageShow
from sys import argv

class MsPaint(ImageShow.Viewer):                    # ベースクラスを継承
    format = 'JPEG'                                 # ペイントにはJPEGが必要

    def get_command(self, file, **options):         # コマンドシーケンスの定義
        return (
            f'mspaint.exe "{file}" '                # ペイントを上げる
            "&& ping -n 2 127.0.0.1 >NUL "          # 2秒待つ
            f'&& del /f "{file}"'                   # 一時ファイルを削除する
        )            


class XnView(ImageShow.Viewer):
    format = 'PNG'

    def get_command(self, file, **options):
        return (
            f'C:\\tools\\XnView\\xnview.exe "{file}" '
            "&& ping -n 2 127.0.0.1 >NUL "
            f'&& del /f "{file}"'
        )            


ImageShow.register(MsPaint, 0)
#ImageShow.register(XnView, 0)

img = Image.open(argv[1])
img.show()
