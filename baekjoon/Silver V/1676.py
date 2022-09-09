number = int(input()) # 5

for i in range(number - 1, 0, -1): #(4, 0, -1)
    number *= i

str_num = list(str(number))
print(str_num)


cnt = 0
for i in range(len(str_num) - 1, 0, -1):
    if str_num[i] == '0':
        cnt += 1
        continue
    else:
        break
print(cnt)