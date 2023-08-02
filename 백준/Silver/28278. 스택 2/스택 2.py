import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N) :
    comm = list(input().split())
    if comm[0] == '1' :
        stack.append(int(comm[1]))
    elif comm[0] == '2' :
        if len(stack) > 0 :
            print(stack.pop())
        else :
            print(-1)
    elif comm[0] == '3' :
        print(len(stack))
    elif comm[0] == '4' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    else :
        if len(stack) > 0 :
            print(stack[-1])
        else :
            print(-1)