N = int(input())
As = list(set(map(int, input().split())))
As.sort()
M = int(input())
nums = list(map(int, input().split()))

for num in nums :
    answer = 0
    l = 0
    u = len(As) - 1
    while l <= u :
        mid = (l+u) // 2
        if num == As[mid] :
            answer = 1
            break
        elif num < As[mid] :
            u = mid - 1
        else :
            l = mid + 1
    print(answer)