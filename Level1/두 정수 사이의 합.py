def solution(a, b):
    answer = 0
    # a가 b보다 크면 a와 b의 순서 바꿔주기
    if a>b:
        a,b = b,a
    for i in range(a,b+1):
        answer+=i
    return answer