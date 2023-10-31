import os
import signal
from Crypto.PublicKey import RSA
from random import SystemRandom
from gmpy2 import powmod

signal.alarm(600)
LAMBDA = 2048


def KeyGen():
   if os.path.isfile("key.pem"):
       with open("key.pem", "rb") as f:
           key = RSA.importKey(f.read())
   else:
       key = RSA.generate(LAMBDA)
       with open("key.pem", "wb") as f:
           f.write(key.exportKey("PEM"))
   return key


if __name__ == "__main__":
    random = SystemRandom()
    key = KeyGen()
    n, e, d = key.n, key.e, key.d
    print("n=",n)
    print("e=",e)

    m0 = random.getrandbits(LAMBDA//2)
    m1 = random.getrandbits(LAMBDA//2)
    x0 = random.randrange(n-1)
    x1 = random.randrange(n-1)
    print("x0=",x0)
    print("x1=",x1)

    v = int(input(">>"))
    k0 = powmod(v - x0, d, n)
    k1 = powmod(v - x1, d, n)
    m0_ = m0 * k0
    m1_ = m1 * k1
    print("m0_=",m0_)
    print("m1_=",m1_)

    guess0 = int(input(">>"))
    guess1 = int(input(">>"))
    if guess0 == m0:
        print(open('flag1').read())
        if guess1 == m1:
            print(open('flag2').read())
    exit()

