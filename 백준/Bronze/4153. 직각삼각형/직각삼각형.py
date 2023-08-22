while True :
    length = list(map(int, input().split()))
    if length.count(0) == 3 :
        break
    length.sort()
    c = length[-1]
    a, b = length[0], length[1]
    if (a**2 + b**2) == c**2 :
        print('right')
    else :
        print('wrong')