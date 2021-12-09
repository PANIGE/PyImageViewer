import sys
from math import ceil
try:
    import pip
    try:
        __import__("PIL")
    except ImportError:
        pip.main(['install', "Pillow"])   
except ImportError:
    print("Please install pip3 for your version of python")
    sys.exit(0)
from PIL import Image

colored = False


def rgb(red, green, blue):
  return f'\x1b[38;2;{red};{green};{blue}m'


def printPic(file, size, char="███", colorQuality=256):
    print(rgb(255,255,255))
    file = args[1]
    file.strip("'")
    file.strip('"')

    img = Image.open(file)
    img.load()
    img.thumbnail((size, size))
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for y in pixels:
        for x in y:
            a = x[3] if len(x) > 3 else 255
            x = [x[0], x[1], x[2], a]
            x[0] = int((round((x[0] / 256)*colorQuality)/colorQuality)*x[3])
            x[1] = int((round((x[1] / 256)*colorQuality)/colorQuality)*x[3])
            x[2] = int((round((x[2] / 256)*colorQuality)/colorQuality)*x[3])
            if colored:
                print(rgb(x[0], x[1], x[2]) + char, end="")
            else:
                avg = int(sum((x[0], x[1], x[2])) / 3)
                
                print(rgb(avg, avg, avg) + char, end="")
        print(rgb(255,255,255))

if __name__ == "__main__":
    args = sys.argv
    qual = int(args[3]) if len(args) > 3 else 256
    printPic(args[1], int(args[2]), colorQuality=qual)
