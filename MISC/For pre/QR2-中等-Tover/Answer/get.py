#!/usr/bin/env python3

import qrcode
from PIL import Image
from random import randint
from secret import flag

bias = 8
img = Image.open('./enc.png')
width, height = img.size

dec_img = Image.new(img.mode, (width//bias, height//bias), 1)

for w in range(width//bias):
    for h in range(height//bias):
        dec_img.putpixel((w, h), img.getpixel((bias*w, bias*h)))

dec_img.show()
