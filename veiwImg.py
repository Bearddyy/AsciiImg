from PIL import Image
import numpy as np
import sys

LUT = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
LUT = "  .:-~=+!1&£23948YV$X@#"
LUT_INT = np.array([x for x in LUT])


def Print_Ascii(arr):
    print('\n'.join(''.join(str(cell) for cell in row) for row in LUT_INT[arr]))

def resize(img, Sizex,Sizey):
    return img.resize((Sizex,Sizey))


def ConvertNP(img):
    pic = np.array(img)
    #pic = (pic-np.min(pic))/np.max(pic)
    pic = (pic/255)
    return np.int_(pic * len(LUT))

def Grey(img):
    return img.convert('L')


np.set_printoptions(threshold=np.inf,linewidth = np.inf)

try:
    Width = int(sys.argv[2])
except:
    Width = 40


print("Opening :", sys.argv[1])
with Image.open(sys.argv[1]) as img:
    tW , tH = img.size
    Height = (tH/tW) * Width
    Height = int(Height * (5/10))
    print("Opened, size(", tW, "," ,tH, ") -> (", Width,",", Height,")" )
    img = resize(img, Width, Height)
    print(img.size)
    img = Grey(img)
    img = ConvertNP(img)
    Print_Ascii(img)

