def solution(s):
    answer = True
    count = [0, 0]  # 각각 p, y의 개수 저장
    s = s.lower()
    
    for i in s :
        if i == 'p' :
            count[0] += 1
        elif i == 'y' :
            count[1] += 1
    if count[0] == count[1] :
        answer = True
    else :
        answer = False

    return answer