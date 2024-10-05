def solution(nums):
    answer = 0
    N = len(nums)
    set_nums = list(set(nums))
    if (N//2) > len(set_nums) :
        answer = len(set_nums)
    else :
        answer = (N//2)
    
    return answer