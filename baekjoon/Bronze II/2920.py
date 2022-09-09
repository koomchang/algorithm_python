major = list(map(int, input().split()))
if major == sorted(major):
    print('ascending')
elif major == sorted(major, reverse=True):
    print('descending')
else:
    print('mixed')