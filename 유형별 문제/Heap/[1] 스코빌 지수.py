# https://programmers.co.kr/learn/courses/30/lessons/42626
# 가장 작은 두 개의 지수->새로운 지수 + 원래 지수
# 1: test ok, but 런타임에러(데크의 pop 문제), 시간초과


from collections import deque


def solution1(scoville, K):
    answer = 0
    scoville = deque(sorted(scoville))
    while scoville:
        new = scoville.popleft() + scoville.popleft() * 2
        scoville.appendleft(new)
        answer += 1
        if min(scoville) >= K:
            break
        if not scoville:
            return -1
    return answer



# 2. Heapq 이용하기 => 한번에 최소(min) 값을 빠르게 pop할 수 있다.
# everything (정확성, 효율성) ok

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 리스트 -> 힙큐로 바꿔준다 :):)

    while scoville:
        answer += 1

        new = heapq.heappop(scoville)  # 가장 작은 값이 꺼내진다.(힙의 이름 명시하는 것 잊지 말기)
        if not scoville:
            return -1
        new += heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)
        smallest = heapq.heappop(scoville)
        if smallest >= K:
            break
        else:
            heapq.heappush(scoville, smallest)

    return answer



print(solution(scoville=[1, 2, 3, 9, 10, 12], K=7))
