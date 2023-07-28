N, B = map(int, input().split())

answer = []
while N != 0 :
    r = N % B
    if r < 10 :
        answer.append(str(r))
    else :
        answer.append(chr(r+55))
    N = N // B
print(''.join(reversed(answer)))