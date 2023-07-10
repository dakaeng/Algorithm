N, M = map(int, input().split())
basket = [n for n in range(1, N+1)]

for m in range(M) :
    i, j = map(int, input().split())
    temp = basket[(i-1):j]
    temp.reverse()
    basket[(i-1):j] = temp
print(*basket)