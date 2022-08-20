from PIL import Image

class Supported:
    def __init__(self):
        # これをやらないと、EXTENSION も OPEN も SAVE もカラのまま
        Image.init()
        self.extensions = Image.EXTENSION.keys()
        self.formats_all = list(set(Image.EXTENSION.values()))
        self.formats_open = Image.OPEN.keys()
        self.formats_save = Image.SAVE.keys()
        self.formats_both = list(set(self.formats_open)
                                 .intersection(set(self.formats_save)))

    def get_extensions(self):
        return self.extensions

    def get_formats_all(self):
        return self.formats_all

    def get_formats_open(self):
        return self.formats_open

    def get_formats_save(self):
        return self.formats_save

    def get_formats_both(self):
        return self.formats_both


if __name__ == '__main__':
    supported = Supported()
    print('All extensions: ', supported.get_extensions())
    print('All formats: ', supported.get_formats_all())
    print('OPEN-able formats: ', supported.get_formats_open())
    print('SAVE-able formats: ', supported.get_formats_save())
    print('OPEN/SAVE formats: ', supported.get_formats_both())
