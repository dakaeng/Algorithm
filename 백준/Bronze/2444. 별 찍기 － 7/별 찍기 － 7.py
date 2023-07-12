N = int(input())

for i in range(2*N-1) :
    if i < N :
        space = N-1-i
        star = 1 + 2*i
    else :
        space = N-1-2*(N-1)+i
        star = 1 + 2*(2*(N-1)-i)
    print(' '*space + '*'*star)