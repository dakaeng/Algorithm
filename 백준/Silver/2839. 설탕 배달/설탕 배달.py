N = int(input())
count = 0
while True :
    if N <= 0:
        break
    if N % 5 != 0 :
        N -= 3
        count += 1
    else :
        count += (N // 5)
        N = 0
    
if N != 0 :
    print(-1)
else :
    print(count)