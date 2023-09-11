N, K = map(int, input().split())
A = []
for _ in range(N) :
    A.append(int(input()))
A.reverse()
count = 0
for a in A :
    if K >= a :
        count += K // a
        K %= a
print(count)