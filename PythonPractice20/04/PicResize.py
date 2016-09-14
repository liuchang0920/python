# coding = utf-8

import os
from PIL import Image


def avatar_resize( pic_dir , x, y):
    # relative path
    picfolder = os.listdir(pic_dir)

    for pic in picfolder:
        if pic.endswith(('.jpg','.png')):
            img = Image.open(pic_dir+'/'+ pic)
            size = img.size
            new_size = []
            if (size[0]/size[1]) > (x/y) :
                new_size = [x, y/x *size[1]]
            else:
               new_size = [x/y * size[0], y]

            print new_size

        new_img = img.resize(new_size)
        new_img.show()
        new_img.save('new_pic/new-'+pic,format='PNG')










iphone_x = 1136
iphone_y = 640
print os.getcwd()
avatar_resize(os.getcwd()+'/pic', iphone_x, iphone_y)
