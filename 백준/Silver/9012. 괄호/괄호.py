T = int(input())

for _ in range(T) :
    count = 0
    string = list(input())
    for i in string :
        if i == '(' :
            count += 1
        else :
            count -= 1
        if count < 0 :
            break
    if count == 0 :
        print('YES')
    else :
        print('NO')