from PIL import Image
import argparse

IMG = 'C:/Users/Gatesby23/Desktop/20160315213308689.png'
WIDTH =120
HEIGHT = 60
OUTPUT = 'C:/Users/Gatesby23/Desktop/test.txt'

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (255.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    print txt

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
       with open("output.txt",'w') as f:
            f.write(txt)