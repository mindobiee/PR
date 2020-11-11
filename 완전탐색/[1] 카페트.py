import math


def solution(brown, yellow):
    total = brown + yellow
    # 2 초과인 수 중에서 소인수 분해
    # 제곱근의 약수 구하기
    list = []
    # 리스트에 [가로,세로] 후보들 저장
    for i in range(3, int(math.sqrt(total)+1)):
        if total % i == 0:
            list.append([int(total / i), i])
    # 갈색 = 노란색 + 4
    # 갈색의 특성을 이용해서 진짜 [가로,세로] 찾기 : brown=2*(x+y)-4
    for i in range(len(list)):
        if brown== 2*(list[i][0]+list[i][1])-4:
            answer=[[list[i][0], list[i][1]]]
            return answer

solution(24,24)