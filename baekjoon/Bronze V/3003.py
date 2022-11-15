piece = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
new_list = []

for i in range(0, len(piece)):
    num = chess[i] - piece[i]
    print(num, end=" ")
