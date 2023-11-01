def handle(s, length):
    res = 0
    for i in range(length - 1, -1, -1):
        res <<= 4
        c = s[i]
        if 'A' <= c <= 'F':
            res += ord('F') - ord(c)
        elif '0' <= c <= '9':
            res += 0xF - int(c)
        else:
            return -1
    return res


def handle_re(s, length):
    res = ''
    for i in range(length - 1, -1, -1):
        c = s & 0xF
        s >>= 4
        res += hex(0xF - c)[2:].swapcase()
    return res


def check(s):
    key = s
    v1 = handle(key, 6)
    v2 = handle(key[6:], 2)
    v3 = handle(key[8:], 4)
    v4 = handle(key[12:], 4)

    if v1 == -1 or v2 == -1 or v3 == -1 or v4 == -1:
        print("输入错误")
        exit()

    low_4B = ((v2 << 24) + v1) ^ 0x12345678
    high_4B = ((v4 << 16) + v3) ^ 0x87654321
    combined = (high_4B << 32) + low_4B

    if CRC32_like(combined) == 0x5D477780:
        return True
    return False


def CRC32_like(n):
    res = 0
    for i in range(8):
        v2 = ((n >> (8 * i)) & 0xff) << 24
        if i:
            res ^= v2
        else:
            res = (~v2) & 0xffffffff
        for j in range(8):
            res *= 2
            if res >= 0xffffffff:
                res &= 0xffffffff
                res ^= 0x4C11DB7
    return res


low_4B = (0xFB6FD9F35C000000 ^ 0x8765432112345678) & 0xFFFFFFFF
high_4B = (0xFB6FD9F35C000000 ^ 0x8765432112345678) >> 32
key_6_16 = handle_re(low_4B >> 24, 2) + handle_re(high_4B & 0xFFFF, 4) + handle_re(high_4B >> 16, 4)
# 1BD2565F38

# 爆破前六位
di = "0123456789ABCDEF"
length = 6
begin = ''
end = key_6_16


def solve(s, idx, length):
    if 2 == idx:
        print("[!]爆破进度：" + s)
    if idx == length:
        if check(begin + s + end):
            print("[+]爆破成功：" + begin + s + end)
            exit()
        else:
            return 0

    for i in di:
        solve(s + i, idx + 1, length)


solve('', 0, length)
