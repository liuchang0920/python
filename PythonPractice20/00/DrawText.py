# coding = utf-8
#

from PIL import Image, ImageDraw, ImageFont


color = (0,0,0)
number = str(10)
file = '1.jpg'


def draw_text(text, color, file):
    img = Image.open(file)
    x, y = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 20)
    draw.text((x-50, 10), text, color, font)


    img.show()

    img.save(file.split(".")[0]+"new.jpg")


draw_text(number, color, file)

