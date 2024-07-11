def solution(friends, gifts):
    len_ = len(friends)
    table = [[0 for _ in range(len_)] for _ in range(len_)]  # 주고받은 선물 현황 저장
    num = [[0, 0, 0] for _ in range(len_)]  # 준 선물, 받은 선물, 선물 지수 저장
    answer = [0] * (len_)  # 각 사람별 다음 달에 받을 선물 개수
    
    name_idx = {}
    for i, n in enumerate(friends) :
        name_idx[n] = i
    
    # 주고받은 선물 계산
    for i in gifts :
        a, b = i.split()
        a_idx = name_idx[a]
        b_idx = name_idx[b]
        table[a_idx][b_idx] += 1
    # 준 선물 계산
    for i in range(len_) :
        num[i][0] += sum(table[i])
    # 받은 선물 계산
    for i in range(len_) :
        for j in range(len_) :
            num[i][1] += table[j][i]
    # 선물 지수 계산
    for i in range(len_) :
        num[i][2] = (num[i][0] - num[i][1])
    
    # 다음 달에 받을 선물 계산
    for i in range(len_-1) :
        for j in range(i+1, len_) :
            if table[i][j] == 0 and table[j][i] == 0 :  # 두 사람이 선물 주고받지 않음
                if num[i][2] > num[j][2] :
                    answer[i] += 1
                elif num[i][2] < num[j][2] :
                    answer[j] += 1
            else :  # 선물 주고받은 전적 있음
                if table[i][j] > table[j][i] :
                    answer[i] += 1
                elif table[i][j] < table[j][i] :
                    answer[j] += 1
                else :  # 선물 주고받은 횟수가 동일함
                    if num[i][2] > num[j][2] :
                        answer[i] += 1
                    elif num[i][2] < num[j][2] :
                        answer[j] += 1
        
    return max(answer)