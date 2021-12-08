import sys
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
import os
import sys

args = sys.argv

char = "██"
colored = True

  


def rgb(red, green, blue):
  return f'\x1b[38;2;{red};{green};{blue}m'


def printPic(file, size, char="██"):
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
    os.system("cls")
    for y in pixels:
        for x in y:
            if colored:
                print(rgb(x[0], x[1], x[2]) + char, end="")
            else:
                avg = int(sum((x[0], x[1], x[2])) / 3)
                print(rgb(avg, avg, avg) + char, end="")
        print(rgb(255,255,255))
        
printPic(args[1], int(args[2]))
