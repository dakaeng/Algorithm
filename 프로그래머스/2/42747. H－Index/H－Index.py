def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    
    count = 0
    for i in range(n-1, -1, -1) :
        count += 1
        if citations[i] <= count :
            answer = max(citations[i], count-1)
            break
        elif count == n :
            answer = n
            
    return answer