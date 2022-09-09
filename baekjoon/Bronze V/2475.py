numbers = list(map(int, input().split()))
verification_num = 0
for i in range(len(numbers)):
    verification_num += numbers[i] ** 2
    verification_num %= 10
print(verification_num)