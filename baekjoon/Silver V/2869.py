A, B, V = map(int, input().split()) # 2 1 5
cnt = 0

day = A - B # 낮 밤 간에 이동한 양
num = V - B # 최종목적지 - 밤에 이동한 양 ->>> 낮에 이동을 하고 끝! 1 2 3 넷째날 낮 : 3+2 = 5
if num % day == 0:
    cnt += num //day
else:
    cnt += num // day + 1
print(cnt)