T = int(input())
for i in range(T):
    quiz = list(map(str, input()))
    total_point = 0
    point = 0
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            point += 1
            total_point += point
        else:
            point = 0
    print(total_point)