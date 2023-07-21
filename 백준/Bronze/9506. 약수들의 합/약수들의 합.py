while True :
    n = int(input())
    if n == -1 :
        break
    nums = []
    for i in range(1, n) :
        if n % i == 0 :
            nums.append(i)
    if sum(nums) == n :
        answer = str(n)
        for i in nums :
            if i == 1 :
                answer += ' = ' + str(i)
            else :
                answer += ' + ' + str(i)
        print(answer)
    else :
        print(f'{n} is NOT perfect.')