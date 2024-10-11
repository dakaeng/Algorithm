def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)) :
        if clothes[i][1] in dic :
            dic[clothes[i][1]] += 1
        else :
            dic[clothes[i][1]] = 1
    counts = list(dic.values())
    
    # 경우의 수 세기
    if len(counts) == 1 :
        answer = counts[0]
    else :
        for i in counts :
            answer *= (i+1)
        answer -= 1
        
    return answer