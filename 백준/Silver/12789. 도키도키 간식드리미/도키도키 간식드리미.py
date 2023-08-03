N = int(input())
numbers = list(map(int, input().split()))
stack = []
pos = 1

while numbers :
    n = numbers.pop(0)
    if n == pos :
        pos += 1
    else :
        stack.append(n)

    while stack :
        if stack[-1] == pos :
            stack.pop()
            pos += 1
        else :
            break

if stack :
    print('Sad')
else :
    print('Nice')