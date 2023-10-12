import gmpy2
import random

from flag import flag_list

n = 33

def makeKey():
    privacyKey = [random.randint(1, 2**7)]
    sUm = privacyKey[0]
    for i in range(1, 7):
        privacyKey.append(random.randint(sUm+2, 2**(7+i)))
        sUm += privacyKey[i]

    m = random.randint(2 * privacyKey[-1] + 1, 4 * privacyKey[-1])
    while gmpy2.gcd(n, m) != 1:
        m = random.randint(2 * privacyKey[-1] + 1, 4 * privacyKey[-1])

    print(privacyKey)
    print(m)
    publicKey = [(n * j) % m for j in privacyKey]
    return publicKey


def encrypt(flag_list, pubKey):
    cipher = [sum(int(bit) * pubKey[i] for i, bit in enumerate(flag)) for flag in flag_list]
    print(cipher)

encrypt(flag_list, makeKey())


'''
[80, 115, 237, 527, 1404, 3844, 7100]
16982
[34602, 14413, 27790, 48136, 36177, 24404, 44750, 24152, 44750, 14822, 14665, 40158, 44750, 34602, 25150, 27790, 48136, 40567]
'''


