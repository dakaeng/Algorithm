N = int(input())
dance = set()
for _ in range(N) :
    name = input().split()
    if 'ChongChong' in name :
        dance.add(name[0])
        dance.add(name[1])
    if (name[0] in dance) or (name[1] in dance) :
        dance.add(name[0])
        dance.add(name[1])
print(len(dance))