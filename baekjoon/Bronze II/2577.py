A = int(input())
B = int(input())
C = int(input())
multiply = A * B * C
multiply_list = list(str(multiply))
for i in range(10):
    print(multiply_list.count(str(i)))
