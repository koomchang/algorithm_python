word = input()
alphabet = list(map(chr, range(97, 123)))
for i in alphabet:
    print(word.find(i), end=' ')
