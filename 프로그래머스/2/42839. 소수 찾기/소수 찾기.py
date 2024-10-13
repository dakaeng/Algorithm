import math

def solution(numbers):
    answer = 0
    
    # x가 소수인지 판단하는 함수
    def prime(x) :
        if x == 0 or x == 1 :
            return False
        for i in range(2, int(math.sqrt(x)) + 1) :
            if x % i == 0 :
                return False
        return True
    
    # numbers로 만들 수 있는 모든 수 구하고, 그게 소수인지 판단하면 됨
    def make_nums(n) :  # n : 몇 개의 종이 조각을 사용하는지
        if len(temp) == n :
            joins.append(int(''.join(temp)))
        
        for i in range(len(numbers)) :
            if visited[i] == False :
                temp.append(numbers[i])
                visited[i] = True
                make_nums(n)
                visited[i] = False
                temp.pop()
                
    joins = []
    for i in range(1, len(numbers)+1) :
        temp = []
        visited = [False] * len(numbers)
        make_nums(i)
    joins = list(set(joins))
    for i in range(len(joins)) :
        if prime(joins[i]) == True :
            answer += 1
    
    return answer