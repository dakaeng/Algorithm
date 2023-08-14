N = int(input())
temp = set()
answer = 0
for _ in range(N) :
    a = input()
    if a == 'ENTER' :
        answer += len(temp)
        temp = set()
    else :
        temp.add(a)
answer += len(temp)
print(answer)