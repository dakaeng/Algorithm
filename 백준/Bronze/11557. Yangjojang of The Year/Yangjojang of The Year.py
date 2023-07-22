T = int(input())
for _ in range(T) :
    N = int(input())
    name = []
    for _ in range(N) :
        S, al = input().split()
        al = int(al)
        name.append([S, al])
    name.sort(key = lambda x: x[1], reverse = True)
    print(name[0][0])