N, M = map(int, input().split())
A = []
B = []
for n in range(N) :
    a = list(map(int, input().split()))
    A.append(a)
for n in range(N) :
    b = list(map(int, input().split()))
    B.append(b)
for n in range(N) :
    for m in range(M) :
        print(A[n][m] + B[n][m], end = ' ')
    print()