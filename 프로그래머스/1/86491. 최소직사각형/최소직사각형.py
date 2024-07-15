def solution(sizes):
    # 가로 길이 중 최댓값, 세로 길이 중 최댓값
    # 단, 가로 세로를 바꿀 수 있음
    w_max = 0
    h_max = 0
    for s in sizes :
        w = s[0]
        h = s[1]
        if w < h :
            w, h = h, w
        w_max = max(w_max, w)
        h_max = max(h_max, h)
    return (w_max * h_max)