import sys

T = int(sys.stdin.readline())
for _ in range(T) :
    test_data = list(sys.stdin.readline().rstrip())
    count = 0
    for i in test_data :
        if i == "(" :
            count += 1
        elif i == ")" :
            count -= 1
        if count < 0 :
            break
    if count == 0 :
        answer = "YES"
    else :
        answer = "NO"
    print(answer)