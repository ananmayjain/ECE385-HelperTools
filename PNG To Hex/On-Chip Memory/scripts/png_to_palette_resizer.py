from PIL import Image
from collections import Counter
from scipy.spatial import KDTree
import numpy as np
import sys

def hex_to_rgb(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
def rgb_to_hex(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
filename = sys.argv[1]
new_w, new_h = map(int, input("What's the new height x width? Like 28 28. ").split(' '))
# new_w, new_h = 16, 20

palette_hex = ['0x800080', '0xF3F3F9', '0x817272', '0xD7D7D7', '0xD7D1D1', '0x898990',
'0x6A6A81', '0x5A5A6A', '0x895A5A', '0x9F7A7A', '0xC39F98',
'0xD1625A', '0xDE7A72', '0xEC907A', '0xEC9F81', '0x514940',
'0xDECAAD', '0xF9D198', '0x817251', '0x908149', '0x9F8951',
'0xB59F5A', '0xCAB57A', '0xD1BC7A', '0xF9CA81', '0xBCB551',
'0xD7CA90', '0xD7C37A', '0xDECA98', '0xECB551', '0xDED151',
'0xE5DEAD', '0xE5D75A', '0xECE598', '0xF3F3D1', '0xF3E590',
'0x496A1A', '0xB5EC7A', '0x7ACA62', '0x90D772', '0x89D772',
'0xC3E5AD', '0xC3F998', '0x5A8951', '0x499F40', '0x6AB55A',
'0x51BC98', '0x6AC398', '0x24AD7A', '0x81D1AD', '0x51A690',
'0x51D1A6', '0x98DEC3', '0xADE5CA', '0x518989', '0xDEE5E5',
'0xB5D7E5', '0x9FADBC', '0x4072AD', '0xCAD1D7', '0xB5C3D1',
'0x5A90CA', '0xDEE5EC', '0x72ADDE', '0xD1DEEC', '0x81C3F3',
'0xA6D7F9', '0x515A7A', '0x7A98D1', '0x6A4951', '0xB52E37',
'0xCA4051']

palette_rgb = [hex_to_rgb(color) for color in palette_hex]

pixel_tree = KDTree(palette_rgb)
im = Image.open("./sprite_originals/" + filename+ ".png") #Can be many different formats.
im = im.convert("RGBA")
layer = Image.new('RGBA',(new_w, new_h), (0,0,0,0))
layer.paste(im, (0, 0))
im = layer
#im = im.resize((new_w, new_h),Image.ANTIALIAS) # regular resize
pix = im.load()
pix_freqs = Counter([pix[x, y] for x in range(im.size[0]) for y in range(im.size[1])])
pix_freqs_sorted = sorted(pix_freqs.items(), key=lambda x: x[1])
pix_freqs_sorted.reverse()
# print(pix)
outImg = Image.new('RGB', im.size, color='white')
outFile = open("./sprite_bytes/" + filename + '.txt', 'w')
i = 0
for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixel = im.getpixel((x,y))
        # print(pixel)
        if(pixel[3] < 200):
            outImg.putpixel((x,y), palette_rgb[0])
            outFile.write("%x\n" %(0))
            # print(i)
        else:
            index = pixel_tree.query(pixel[:3])[1]
            outImg.putpixel((x,y), palette_rgb[index])
            outFile.write("%x\n" %(index))
        i += 1
outFile.close()
outImg.save("./sprite_converted/" + filename + ".png" )
