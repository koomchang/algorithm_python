from itertools import combinations
N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort()
sum_lst = []

c = list(combinations(num_lst, 3))

for i in range(0, len(c)):
    sum_lst.append(sum(c[i]))
sum_lst = list(set(sum_lst))
sum_lst.sort()
new_list = []

for i in sum_lst:
    if i <= M:
        new_list.append(i)
print(max(new_list))