# 접근법; "가장" 무거운 사람 + "가장" 가벼운 사람 -> 만약 limit보다 넘으면 계속 줄여나가기

from collections import deque


def solution(people, limit):

    alone, together=0,0 # 따로, 둘이 같이 타는 경우의 수 변수
    queue = deque(sorted(people)) # 오름차순으로 정렬
    lightest = queue.popleft()  # 가벼운 사람

    while lightest:
        if not queue: # 큐가 (비교대상이) 더이상 존재하지 x
            alone+=1
            break
        heaviest = queue.pop()  # 무거운 사람
        sum = lightest+heaviest # 비교할 대상 : 두 사람의 무게 합
        if sum <= limit: # 같이 탈 조건 : limit보다 적을 때 같이 타기
            together+=1
            if not queue: # empty pop - 오류 방지
                break
            else:
                lightest = queue.popleft()
        else: # 무거운 사람 혼자 보트 타기
            alone+=1
    answer=alone+together
    return answer



print(solution(people=[70, 50, 80,50],limit=100))