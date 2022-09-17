import sys
from string import ascii_lowercase

N = int(sys.stdin.readline())
L = input()

alphabet_dict = {}
num = 1

for i in ascii_lowercase:
    alphabet_dict[i] = num
    num += 1

hashed = 0
for i in range(N):
    hashed += alphabet_dict[list(L)[i]] * 31 ** i
print(hashed % 1234567891)