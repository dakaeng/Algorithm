N = int(input())

answer = 0
for n in range(1, N-1) :
    sum = n
    temp = n
    while (temp != 0) :
        sum += temp % 10
        temp = temp // 10
    if sum == N :
        answer = n
        break
print(answer)