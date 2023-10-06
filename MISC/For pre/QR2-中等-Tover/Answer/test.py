#!/usr/bin/env python3

import qrcode
from PIL import Image
from random import randint
from secret import flag

ox = {
0:[
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
],
1:[
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1]
]
}

img = qrcode.make(data=flag).get_image()
width, height = img.size

bias = 8
enc_img = Image.new(img.mode, (bias*width, bias*height), 1)

for w in range(width):
    for h in range(height):
        px = img.getpixel((w, h)) % 2
        for i in range(bias):
            for j in range(bias):
                enc_img.putpixel((bias*w+i, bias*h+j), ox[px][i][j])

with open('enc.png', 'wb') as f:
    enc_img.save(f)

