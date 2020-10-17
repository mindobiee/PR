def solution(x, n):
    answer = []
    temp=x
    # n번 반복하는 반복문
    for i in range(0,n):
        # x만큼 더해지는 temp를 리스트에 추가
        answer.append(temp)
        temp+=x
    return answer
