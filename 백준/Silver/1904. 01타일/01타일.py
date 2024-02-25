N = int(input())

answer = [0] * 1000001
answer[1] = 1  # N = 1인 경우, 가능한 경우의 수는 1(1)
answer[2] = 2  # N = 2인 경우, 가능한 경우의 수는 2(00, 11)
for i in range(3, N+1) :
  answer[i] = (answer[i-1] + answer[i-2]) % 15746
print(answer[N])