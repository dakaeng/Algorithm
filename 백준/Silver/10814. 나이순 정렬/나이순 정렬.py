N = int(input())
account = []
for n in range(N) :
    age, name = input().split()
    account.append([int(age), name])
account.sort(key = lambda x: x[0])
for age, name in account :
    print(age, name)