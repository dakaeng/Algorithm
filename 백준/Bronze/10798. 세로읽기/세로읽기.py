words = []
for i in range(5) :
    words.append(list(input()))
length = max([len(i) for i in words])
for w in words :
    if len(w) < length :
        w.extend(['-'] * (length - len(w)))
for j in range(length) :
    for i in range(5) :
        if words[i][j] != '-' :
            print(words[i][j], end = '')