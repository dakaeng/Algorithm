X = int(input())

n = 1
while True :
    sums = sum([i for i in range(1, n+1)])
    if X > sums :
        n += 1
    else :
        break

if n % 2 == 0 :
    nu = n-(sums-X)
    de = (n+1)-nu
    print(f'{nu}/{de}')

else :
    de = n-(sums-X)
    nu = (n+1)-de
    print(f'{nu}/{de}')