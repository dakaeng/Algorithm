def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : (x, len(x)))
    n = len(phone_book)
    
    # 이중 for문을 통한 완전탐색 -> 당연하게도 시간 초과 발생
    for i in range(1, n-1) : 
        length = len(phone_book[i])
        if phone_book[i-1] == phone_book[i][0:len(phone_book[i-1])] :
            answer = False
            break
        if phone_book[i+1][0:len(phone_book[i])] == phone_book[i] :
            answer = False
            break
            
    return answer