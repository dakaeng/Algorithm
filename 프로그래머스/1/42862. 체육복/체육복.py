def solution(n, lost, reserve):
    # 여벌 체육복 가져온 학생이 체육복을 도난당한 경우 -> 두 리스트에서 모두 제거
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    new_reserve.sort()
    
    # 여벌 체육복이 있는 학생들이 체육복 빌려주기
    for i in new_reserve :
        if (i-1) in new_lost :  # 앞번호가 도난당했으면 빌려주기
            new_lost.remove(i-1)
        elif (i+1) in new_lost :  # 뒷번호가 도난당했으면 빌려주기
            new_lost.remove(i+1)
    
    return n - len(new_lost)