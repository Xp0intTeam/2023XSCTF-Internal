import itertools
from Crypto.Util.number import inverse

'''
[80, 115, 237, 527, 1404, 3844, 7100]
16982
[34602, 14413, 27790, 48136, 36177, 24404, 44750, 24152, 44750, 14822, 14665, 40158, 44750, 34602, 25150, 27790, 48136, 40567]
'''

def decrypt():
    privacyKey = [80, 115, 237, 527, 1404, 3844, 7100]
    m = 16982
    n = 33
    cipher = [34602, 14413, 27790, 48136, 36177, 24404, 44750, 24152, 44750, 14822, 14665, 40158, 44750, 34602, 25150, 27790, 48136, 40567]
    capacity = []
    binary_list = ""
    for i in cipher:
        capacity.append(int((i * (inverse(n, m))) % m))

    print(capacity)
    for constant in capacity:
        possible_solutions = list(itertools.product([0, 1], repeat=len(privacyKey)))
        for solution in possible_solutions:
            left_side = sum(privacyKey[i] * solution[i] for i in range(len(privacyKey)))
            if left_side == constant:
                for i in solution:
                    binary_list += str(i)
                binary_list += " "

    decoded_text = ''.join(chr(int(byte, 2)) for byte in binary_list.split())
    print(decoded_text)



decrypt()