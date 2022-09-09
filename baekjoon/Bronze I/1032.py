N = int(input())
file_list = [] # config.as confff.as coafig.aa
while N:
    file_name = input()
    N -= 1
    file_list.append(file_name)

answer = list(file_list[0]) # = config.as

for i in file_list:d
    for j in range(0, len(file_list[0])):
        if answer[j] != i[j]:
            answer[j] = '?'

answer = ''.join(answer)
print(answer)