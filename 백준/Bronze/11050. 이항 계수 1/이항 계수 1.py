N, K = map(int, input().split())
if (N-K) < K :
    K = (N-K)
a = 1
b = 1
for i in range(K) :
    a *= N
    N -= 1
while True :
    if K == 0 :
        break
    b *= K
    K -= 1
print(int(a/b))