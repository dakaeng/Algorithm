def solution(n, computers):
    
    def dfs(v) :
        for i in range(n) :
            if computers[v][i] == 1 :
                computers[v][i] = 0
                computers[i][v] = 0
                dfs(i)
    
    answer = 0

    # 탐색 시작
    for i in range(n) :
        if computers[i][i] == 1 :  # 방문하지 않은 경우
            dfs(i)
            answer += 1
        
    return answer