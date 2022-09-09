T = int(input())
for i in range(T):
    S, R = map(str, input().split())
    for j in range(len(R)):
        print(int(S) * R[j], end='')
    print()