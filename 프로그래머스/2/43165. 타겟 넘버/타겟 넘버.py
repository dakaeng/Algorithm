import sys
sys.setrecursionlimit(10**3)

def solution(numbers, target):
    answer = 0
    
    # 백트래킹? 2개(+,-) 중에서 중복 포함해서 n개 뽑는 경우 체크 후, target 만족하는지 확인하기
    def dfs() :
        nonlocal answer
        
        if len(temp) == len(numbers) :
            sums = 0
            for i in range(len(temp)) :
                sums += int((temp[i] + str(numbers[i])))
            if sums == target :
                answer += 1
            return
        
        for i in ['+', '-'] :
            temp.append(i)
            dfs()
            temp.pop()
        
    temp = []
    dfs()
    
    return answer