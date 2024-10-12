def solution(priorities, location):
    answer = 0
    max_rank = max(priorities)  # 남아 있는 프로세스 중 가장 높은 우선순위 저장
    n = len(priorities)
    
    for i in range(n) :
        for j in range(n) :
            if priorities[j] == max_rank :
                answer += 1
                priorities[j] = 0
                max_rank = max(priorities)
                if j == location :
                    return answer
            
    return answer