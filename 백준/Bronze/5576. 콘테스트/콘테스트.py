Wscore = []
Kscore = []
for _ in range(10) :
    Wscore.append(int(input()))
for _ in range(10) :
    Kscore.append(int(input()))
Wscore.sort(reverse = True)
Kscore.sort(reverse = True)
print(sum(Wscore[0:3]), sum(Kscore[0:3]))