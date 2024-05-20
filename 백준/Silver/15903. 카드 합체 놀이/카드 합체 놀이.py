n, m = map(int, input().split())
a = list(map(int, input().split()))

# 그때그때 가장 작은 값 2개를 더하면 됨
for _ in range(m) :
  a.sort()
  temp = sum(a[0:2])
  a[0], a[1] = temp, temp
print(sum(a))