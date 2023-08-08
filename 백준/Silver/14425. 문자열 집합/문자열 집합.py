N, M = map(int, input().split())
S = []
answer = 0
for _ in range(N) :
    S.append(input())
for _ in range(M) :
    string = input()
    if string in S :
        answer += 1
print(answer)