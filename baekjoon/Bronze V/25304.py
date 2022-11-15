total_price = int(input())
total_cnt = int(input())

sum = 0
for i in range(0, total_cnt):
    price, cnt = map(int, input().split())
    sum += price * cnt

if total_price == sum:
    print("Yes")
else:
    print("No")
