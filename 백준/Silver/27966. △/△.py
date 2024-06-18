N = int(input())

# 1번이 가운데 있고, 나머지는 모두 1번과 연결된 형태가 되어야 함
print((N-1)**2)
for i in range(2, N+1) :
  print(1, i)