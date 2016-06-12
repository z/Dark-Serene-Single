import base64
from os.path import splitext
import glob

class Image():

    def __init__(self, filename):
        with open(filename, 'rb') as image_file:
            self.base64 = base64.b64encode(image_file.read())
            self.name   = splitext(filename)[0]

class Stylesheet():

    def __init__(self, filename):
        with open(filename, 'r') as stylesheet:
            self.contents = stylesheet.read()


def main():

    css = Stylesheet('stylesheet.css')
    output_css = css.contents

    image_files = glob.glob('*.png')
    images = {}

    for image_file in image_files:
        img = Image(image_file)
        output_css = output_css.replace('%%' + img.name + '%%', '"data:image/png;base64,' + img.base64 + '"')

    print(output_css)


if __name__ == '__main__':
    main()

