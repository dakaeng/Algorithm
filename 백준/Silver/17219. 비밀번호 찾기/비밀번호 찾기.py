N, M = map(int, input().split())
pass_dict = {}
for _ in range(N) :
    site, password = input().split()
    pass_dict[site] = password
for _ in range(M) :
    site = input()
    print(pass_dict[site])