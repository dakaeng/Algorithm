N, K = map(int, input().split())
number = list(input())
number = [int(i) for i in number]

answer = []  # 지우지 않을 숫자들 저장

for i in range(N) :
  while (answer and answer[-1] < number[i] and K > 0) :
    answer.pop()
    K -= 1
  answer.append(number[i])

if K == 0 :
  print(''.join(map(str, answer)))
else :
  print(''.join(map(str, answer[:-K])))