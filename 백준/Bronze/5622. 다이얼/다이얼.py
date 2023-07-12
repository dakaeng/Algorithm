word = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for idx, alpha in enumerate(dial) :
    for w in word :
        if w in alpha :
            time += (idx+3)
print(time)