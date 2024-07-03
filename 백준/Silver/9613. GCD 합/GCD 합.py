def GCD(n1, n2) :
    rem = 1
    while(rem != 0) :
        rem = n1%n2
        n1 = n2
        n2 = rem
    return n1

t = int(input())
for _ in range(t) :
    n, *num = map(int, input().split())

    answer = 0
    for i in range(n-1) :
        for j in range(i+1, n) :
            answer += GCD(num[i], num[j])
    print(answer)