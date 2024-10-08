N, K = map(int, input().split())
num = input()

num = [int(i) for i in num]
stack = []
count = 0  # 제거한 숫자의 개수

for i in range(N) :
  while (stack and stack[-1] < num[i] and count < K) :
    stack.pop()
    count += 1
  stack.append(num[i])

if count == K :
  print(''.join([str(i) for i in stack]))
else :
  print(''.join([str(i) for i in stack[:-(K-count)]]))