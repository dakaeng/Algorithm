N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

for i in range(N)[::-1] :
    if A[i] == 1 :
        del B[i]
    
if len(B) > 0 :
    BC = list(reversed(B))
    BC.extend(C)
    for i in range(M) :
        print(BC[i], end = ' ')
else :
    print(*C)