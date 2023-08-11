N, M = map(int, input().split())
list1 = []
list2 = []
for _ in range(N) :
    list1.append(input())
for _ in range(M) :
    list2.append(input())
names = list(set(list1) & set(list2))
names.sort()
print(len(names))
for n in names :
    print(n)