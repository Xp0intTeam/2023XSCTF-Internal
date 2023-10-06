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

img = Image.open('./enc.png')
width, height = img.size

bias = 8
enc_img = Image.new(img.mode, (width, height), 1)

for w in range(width//bias):
    for h in range(height//bias):
        px = 0
        for i in range(bias):
            for j in range(bias):
                enc_img.putpixel((bias*w+i, bias*h+j), ox[px][i][j])

with open('bg.png', 'wb') as f:
    enc_img.save(f)

