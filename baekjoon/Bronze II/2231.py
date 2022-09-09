N = int(input())
boolean = False
if len(str(N)) >= 2:
    for i in range(abs(N - (len(str(N))) * 9), N):
        answer = i
        for j in range(len(str(i))):
            answer += int(str(i)[j])
        if answer == N:
            print(i)
            boolean = True
            break
    if not boolean:
        print(0)
else:
    if N % 2 == 0:
        print(N // 2)
    else:
        print(0)
