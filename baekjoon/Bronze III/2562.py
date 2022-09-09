num_list = []
for i in range(9):
    values = int(input())
    num_list.append(values)
print(max(num_list))
print(num_list.index(max(num_list)) + 1)