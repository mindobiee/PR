# 앞에서부터 더하기, limit가 넘을 때에는 새로운 보트에 추가하기 (안넘을 때엔 그 전 보트에 추가하기)
# 필요 : people 의 무게!
# 두 명 한정됨!!!!
# 접근법; 무거운 사람 + 가벼운 사람 -> 만약 limit보다 넘으면 계속 줄여나가기 (!)
from collections import deque


def solution(people, limit):

    alone, together=0,0 # 따로, 둘이 같이 타는 경우의 수 변수
    queue = deque(sorted(people)) # 오름차순으로 정렬
    lightest = queue.popleft()  # 가벼운 사람

    while lightest: # 먼저 pop한 lightest를 위해서
        print(queue)
        if not queue: # 큐가 더이상 존재하지 않으면,
            alone+=1
            break
        heaviest = queue.pop()  # 무거운 사람
        sum = lightest+heaviest # 두 사람의 무게
        if sum <= limit: # 같이 탈 조건 : limit보다 적을 때 같이 타기
            together+=1
            if not queue:
                break
            else:
                lightest = queue.popleft()
        else: # 무거운 사람 혼자 보트 타기
            alone+=1
    print(alone)
    print(together)
    answer=alone+together
    return answer



print(solution(people=[70, 50, 80,50],limit=100))