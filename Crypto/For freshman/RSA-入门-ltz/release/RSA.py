from Crypto.Util.number import *
from secret import flag

p = getPrime(128)
q = getPrime(128)
n=p*q
e = 65537
m = bytes_to_long(flag)
c = pow(m, e, n)
print(f"c={c}")
print(f"n={n}")

"""
c=34235083603255394631472769355891395597556301609076426725471325009186091570619
n=52325875250719834038466049947961388071650687620177969152235704766211385392939
"""