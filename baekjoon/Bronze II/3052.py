numbers = []
for i in range(10):
    number = int(input())
    numbers.append(number)
mod = []
for i in numbers:
    mod.append(i % 42)
mod = set(mod)
print(len(mod))