from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deque = deque([])
for _ in range(N) :
    comm = list(input().split())

    if comm[0] == '1' :
        deque.appendleft(int(comm[1]))

    elif comm[0] == '2' :
        deque.append(int(comm[1]))

    elif comm[0] == '3' :
        if deque :
            print(deque.popleft())
        else :
            print(-1)

    elif comm[0] == '4' :
        if deque :
            print(deque.pop())
        else :
            print(-1)

    elif comm[0] == '5' :
        print(len(deque))

    elif comm[0] == '6' :
        if deque :
            print(0)
        else :
            print(1)

    elif comm[0] == '7' :
        if deque :
            print(deque[0])
        else :
            print(-1)

    elif comm[0] == '8' :
        if deque :
            print(deque[-1])
        else :
            print(-1)