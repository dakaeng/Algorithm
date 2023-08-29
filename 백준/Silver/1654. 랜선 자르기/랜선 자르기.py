K, N = map(int, input().split())
length = []
for _ in range(K) :
    length.append(int(input()))

start = 1
end = max(length)
while (start <= end) :
    mid = (start + end) // 2
    count = [(i // mid) for i in length]
    if sum(count) < N :
        end = mid - 1
    else :
        start = mid + 1
print(end)