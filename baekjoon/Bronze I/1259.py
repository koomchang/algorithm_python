number = 1
boolean = True
while number != '0':
    number = input()
    if number == '0':
        break
    for i in range(len(number)):
        if number[i] != number[len(number) - 1 - i]:
            boolean = False
            break
        else:
            boolean = True
    if boolean:
        print('yes')
    else:
        print('no')
