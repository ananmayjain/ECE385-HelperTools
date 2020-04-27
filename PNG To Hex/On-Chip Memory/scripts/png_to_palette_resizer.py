from PIL import Image
from collections import Counter
from scipy.spatial import KDTree
import numpy as np
def hex_to_rgb(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
def rgb_to_hex(num):
    h = str(num)
    return int(h[0:4], 16), int(('0x' + h[4:6]), 16), int(('0x' + h[6:8]), 16)
filename = input("What's the image name? ")
new_w, new_h = map(int, input("What's the new height x width? Like 28 28. ").split(' '))

palette_hex = ['0x800080','0xf3f3f9', '0x817272', '0xd7d7d7', '0xd7d1d1', '0x898990', '0x6a6a81', '0x895a5a', '0x9f7a7a', '0xc39f98', '0xd1625a', '0xde7a72', '0xec907a', '0xec9f81', '0xdecaad', '0xf9d198', '0x817251', '0x908149', '0x9f8951', '0xb59f5a', '0xcab57a', '0xd1bc7a', '0xf9ca81', '0xbcb551', '0xd7ca90', '0xd7c37a', '0xdeca98', '0xecb551', '0xded151', '0xe5dead', '0xe5d75a', '0xece598', '0xf3f3d1', '0xf3e590', '0xb5ec7a', '0x7aca62', '0x90d772', '0x89d772', '0xc3e5ad', '0xc3f998', '0x6ab55a', '0x6ac398', '0x81d1ad', '0x98dec3', '0xade5ca', '0xdee5e5', '0xb5d7e5', '0x9fadbc', '0xcad1d7', '0xb5c3d1', '0xdee5ec', '0x72adde', '0xd1deec', '0x81c3f3', '0xa6d7f9', '0x7a98d1', '0x6a4951', '0xb52e37', '0xca4051']

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
print(pix)
outImg = Image.new('RGB', im.size, color='white')
outFile = open("./sprite_bytes/" + filename + '.txt', 'w')
i = 0
for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixel = im.getpixel((x,y))
        print(pixel)
        if(pixel[3] < 200):
            outImg.putpixel((x,y), palette_rgb[0])
            outFile.write("%x\n" %(0))
            print(i)
        else:
            index = pixel_tree.query(pixel[:3])[1]
            outImg.putpixel((x,y), palette_rgb[index])
            outFile.write("%x\n" %(index))
        i += 1
outFile.close()
outImg.save("./sprite_converted/" + filename + ".png" )
