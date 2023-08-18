N = int(input())
answer = 1
while True :
    if N == 0 :
        break
    answer *= N
    N -= 1
print(answer)