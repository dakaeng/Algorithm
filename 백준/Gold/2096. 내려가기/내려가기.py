N = int(input())
max_sum = []
min_sum = []

a, b, c = map(int, input().split())
max_sum = [a, b, c]
min_sum = [a, b, c]

for i in range(1, N) :
  x, y, z = map(int, input().split())
  max_sum = [x + max(max_sum[0], max_sum[1]), y + max(max_sum), z + max(max_sum[1], max_sum[2])]
  min_sum = [x + min(min_sum[0], min_sum[1]), y + min(min_sum), z + min(min_sum[1], min_sum[2])]

print(max(max_sum), min(min_sum))