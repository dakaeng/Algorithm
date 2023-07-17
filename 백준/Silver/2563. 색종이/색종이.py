N = int(input())
paper = [[0]*100 for i in range(100)]
for n in range(N) :
    x, y = map(int, input().split())
    for i in range(10) :
        for j in range(10) :
            paper[x-1+i][y-1+j] = 1
sums = 0
for i in paper :
    sums += sum(i)
print(sums)