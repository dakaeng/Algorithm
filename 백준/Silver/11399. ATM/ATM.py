N = int(input())
P = list(map(int, input().split()))

P.sort()
time_sum = 0
time = 0
for p in P :
    time += p
    time_sum += time
print(time_sum)