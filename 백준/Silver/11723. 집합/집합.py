import sys
input = sys.stdin.readline

S = set([])
M = int(input())
for _ in range(M) :
    comm = list(input().split())
  
    if comm[0] == 'add' :
        S.add(int(comm[1]))
    elif comm[0] == 'remove' :
        S.discard(int(comm[1]))
    elif comm[0] == 'check' :
        if int(comm[1]) in S :
            print(1)
        else :
            print(0)
    elif comm[0] == 'toggle' :
        if int(comm[1]) in S :
            S.remove(int(comm[1]))
        else :
            S.add(int(comm[1]))
    elif comm[0] == 'all' :
        S = set([i for i in range(1, 21)])
    elif comm[0] == 'empty' :
        S = set([])