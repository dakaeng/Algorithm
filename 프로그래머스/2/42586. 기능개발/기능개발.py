import math

def solution(progresses, speeds):
    answer = []
    days = []  # 각 작업별로 남은 작업기간 저장
    for i in range(len(progresses)) :
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    temp = [days[0]]
    for d in days[1:] :
        if temp[0] < d :
            answer.append(len(temp))
            temp = [d]
        else :
            temp.append(d)
    answer.append(len(temp))
    
    return answer