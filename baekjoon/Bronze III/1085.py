x, y, w, h = map(int, input().split())
right = w-x
left = x
up = h-y
down = y
print(min(right, left, up, down))