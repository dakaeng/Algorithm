def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, n in enumerate(name) :
        # 각 알파벳을 만들려면 몇 번 눌러야 하는지 체크
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
    
        # 커서 이동 횟수 추가하기
        next = i + 1
        while next < len(name) and name[next] == 'A' :
            next += 1
        
        # 오른쪽으로 가다가 왼쪽으로 다시 돌아가는 것, 모두 A인 경우도 고려
        min_move = min(min_move, i*2 + len(name) - next, 2*(len(name) - next) + i)
    answer += min_move    
    
    return answer