def solution(a, b):
    answer = 0
    # a가 b보다 크면 a와 b의 순서 바꿔주기
    if a>b:
        a,b = b,a

    # a에서 b 사이의 정수의 합 구하기
    for i in range(a,b+1):
        answer+=i
    return answer