import sys

N = int(input())
num_list = []
for i in range(0, N):
    num_list.append(int(sys.stdin.readline()))

for i in sorted(num_list):
    print(i)