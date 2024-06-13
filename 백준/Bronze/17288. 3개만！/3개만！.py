S = input()
answer = 0
count = 1  # 연속된 숫자 개수
temp = int(S[0])
for s in S[1:] :
    if (temp + 1) == int(s) :
        count += 1
    else :
        if count == 3 :
            answer += 1
        count = 1
    temp = int(s)
if count == 3 :
  answer += 1
print(answer)
        