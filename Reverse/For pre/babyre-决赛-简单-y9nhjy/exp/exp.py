s = '66072C3B7B1966A1315A2FFA365FC6CB5F1966B333196E994016'
flag = ''
for i in range(int(len(s) / 2)):
    x = int(s[i * 2:i * 2 + 2], 16)
    if (i % 4 == 0):
        flag += chr(((x) & 0xE7) ^ (x & 0x10 >> 1) ^ (x & 0x08 << 1))
    elif (i % 4 == 1):
        flag += chr(x ^ 107)
    elif (i % 4 == 2):
        flag += chr((x >> 5) | ((x << 3) & 0xff))
    elif (i % 4 == 3):
        flag += chr((x >> 3) | ((x << 5) & 0xff))
print(flag)
