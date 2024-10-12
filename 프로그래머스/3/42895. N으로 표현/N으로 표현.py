def solution(N, number):
    
    # 숫자 두 개로 가능한 모든 연산의 경우 return
    def operations(n1, n2) :
        if n2 != 0 :
            return [n1+n2, n1-n2, n1*n2, n1/n2]
        else :
            return [n1+n2, n1-n2, n1*n2]
        
    answer = 0
    Ns = [0] + [int(str(N)*i) for i in range(1, 9)]    # Ns[i] : N이 i번 반복되는 숫자 (ex. [5, 55, 555, ...])
    temp = [[i] for i in Ns]  # temp[i] : answer = i인 경우에 나올 수 있는 모든 연산의 결과 저장
    
    while (True) :
        
        answer += 1
        if answer == 9 :
            break
        
        if answer == 1 :  # N == number인 경우
            if Ns[1] == number :
                return answer
        else :
            # temp[answer] = operations(temp[answer - j], temp[j]). j = 1, ..., answer-1
            for j in range(1, answer) :
                for n1 in temp[answer-j] :
                    for n2 in temp[j] :
                        temp[answer].extend(operations(n1, n2))
            if number in temp[answer] :
                return answer
        
    return -1