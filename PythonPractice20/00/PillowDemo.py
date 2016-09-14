from __future__ import print_function
from PIL import Image, ImageFilter



# im = Image.open("1.jpg")
# print(im.format, im.size, im.mode)
# im.show()
#
# im_sharp = im.filter(ImageFilter.SHARPEN)
#
# im_sharp.save('1_shape')

from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('1.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
# fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello",  fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World",  fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()