from collections import Counter
import sys


# 최빈값 구하는 함수
def mode_(lst):
    freq = dict(Counter(lst).most_common())
    # freq = {x: lst.count(x) for x in set(lst)}
    new_lst = sorted([x for x in freq.keys() if freq[x] == max(freq.values())])
    if len(new_lst) == 1:
        return new_lst[0]
    return new_lst[1]


N = int(sys.stdin.readline())
lst = []

# 산술 평균, 중앙값, 최빈값, 범위
avg, median, mode, range_ = 0, 0, 0, 0

sum_ = 0
# 입력받은 숫자들 list 에 저장
for i in range(0, N):
    num = int(sys.stdin.readline())
    lst.append(num)
    sum_ += num
lst.sort()

avg = round(sum_ / len(lst))
median = lst[len(lst) // 2]
range_ = max(lst) - min(lst)

print(avg)
print(median)
print(mode_(lst))
print(range_)


"""
1. count 함수가 시간이 오래 걸려서 collections의 counter를 사용. 하지만 이게 왜 더 빠른지는 모르겠음.
2. input() 대신 sys.stdin.readline()을 사용하여 시간을 줄임. 마찬가지로 이게 왜 더 빠른지는 모르겠음.
"""