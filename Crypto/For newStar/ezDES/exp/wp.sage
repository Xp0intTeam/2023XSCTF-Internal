```python
from Crypto.Util.strxor import strxor as xor
from Crypto.Util.number import long_to_bytes,bytes_to_long
import hashlib

def easyF(s,k):
    md=hashlib.md5(xor(s,k)).hexdigest()[8:-8]
    return md.encode()

def round(s, k):
    l, r = s[:16], s[16::]
    l_, r_ = r,xor(easyF(r, k), l)
    return l_ + r_

def encode(s, k):
    t = s
    for i in range(8)[::-1]:
        t = round(t, k[i])
    return t

key=[332077028545244270654208585270175043190,304218346324378654027657974634344896716,148008784927924354861450977864026304718,36262161674211239794923953575626673545,187994020945533631241740623853988137720,316469430696194731281698556418822328334,183139517196433296622397023582947234006,258883318703806912808737065014789313672]
for i in range(len(key)):
    key[i]=long_to_bytes(key[i])

c=b'562>c6c;j0j17c22d0g36gh:k13m<cnc'

l,r=(c[0:16]),(c[16::])
c=r+l
m=encode(c,key)
l,r=m[16::],m[0:16]
f=l+r
print(f)
#按照UUID格式拼接
#b'XSCTF{6b2d76d8-a09c-1f80-15c5-039a8f1c361c}'
```

