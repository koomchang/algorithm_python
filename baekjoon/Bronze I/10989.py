import sys

N = int(sys.stdin.readline())
lst = [0] * 10001

for i in range(0, N):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(0, 10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)

# list append 로 푸는 방식은 메모리 초과 때문에 풀지 못하였고 배열을 초기화 시킨 후 index 에 값을 넣어 출력 해주었다.