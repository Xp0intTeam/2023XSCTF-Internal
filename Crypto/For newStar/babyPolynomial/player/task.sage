from Crypto.Util.number import *
import uuid

def get_coeff(IDs, p):
    a = []
    R.<x> = Zmod(p)[]
    for x_i in IDs: 
        f_i = 1
        for x_j in IDs:
            if x_j != x_i:
                f_i *= (x-x_j)/(x_i-x_j)
        a.append(f_i.coefficients(sparse=False))
    return a

def myfunction(IDs, p):
    n = len(IDs)
    A = [bytes_to_long(str(uuid.uuid4()).encode()) for i in range(n)]
    a = get_coeff(IDs, p)
    Q = []
    for i in range(n):
        sums = 0
        for j in range(n):
            sums += a[j][i]*A[j]
        Q.append(sums)
    return Q, A[0]

## task1
p1 = getPrime(512)
IDs_1 = [getPrime(512) for i in range(10)]
Q1, m1 = myfunction(IDs_1, p1)
with open("IDs_1.txt", 'w') as f:
    print(IDs_1, file=f)
with open("Q1.txt", 'w') as f:
    print(Q1,file=f)
with open("p1.txt", 'w') as f:
    print(p1,file=f)

## task2
p2 = getPrime(512)
IDs_2 = [getPrime(512) for i in range(10)]
Q2, m2 = myfunction(IDs_2, p2)
with open("IDs_2.txt", 'w') as f:
    print(IDs_2[0],file=f)
with open("Q2.txt", 'w') as f:
    print(Q2,file=f)
with open("p2.txt", 'w') as f:
    print(p2,file=f)

flag = b"flag{" + long_to_bytes(m1)+long_to_bytes(m2) + b"}"
with open("flag.txt", 'w') as f:
    print(flag,file=f)