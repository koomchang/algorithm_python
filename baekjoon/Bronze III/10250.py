T = int(input())
while T:
    H, W, N = map(int, input().split())
    if N % H != 0:
        ho = N // H + 1
    else:
        ho = N // H
    if len(str(ho)) == 1:
        ho = '0'+str(ho)
    floor = N % H
    if floor == 0:
        floor = H
    print(str(floor) + str(ho))
    T -= 1