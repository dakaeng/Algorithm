N = int(input())

count = N
for n in range(N) :
    word = input()
    for i in range(len(word)-1) :
        if word[i] == word[i+1] :
            continue
        elif word[i] in word[(i+1):] :
            count -= 1
            break
print(count)