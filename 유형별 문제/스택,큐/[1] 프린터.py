# location에 있는 문서가 몇번째로 인쇄되는지 리턴
# priorities가 높은 문서부터 인쇄한다.
from collections import deque


def solution(priorities, location):

    # 큐 구현을 위해 deque 라이브러리 사용
    queue=deque()

    for i in range(len(priorities)):
        queue.append([i, priorities[i]])

    stack=[]
    while queue:
        first=queue.popleft()
        if queue: # 뒤에 더 있을 때
            best=max(list(queue),key=lambda x:x[1]) # ValueError: max() arg is an empty sequence -> queue가 empty일 때 포착 필요
            if first[1]>=best[1]: # pop 한게 우선순위가 더 높으면
                if stack.count(first)==0: # 아직 first 원소가 안들어갔다면 (여기도 중복 방지)
                    stack.append(first)
            else: # 우선순위 높은게 뒤에 있으면
                queue.append(first)
                if stack.count(best)==0: # 아직 best 원소가 안들어갔다면 (중복 방지)
                    stack.append(best)
        else: # 마지막 요소일 때
            stack.append(first)
    print(stack)

    for i in range(len(stack)):
        if location == stack[i][0]:
            return (i+1)


print(solution(priorities=[1, 1, 9, 1, 1, 1],location=0))

#  if stack[i][1] < stack[j][1]: # TypeError: 'int' object is not subscriptable
#        stack.append(stack[i]) # stack[i][0]만 넣어서 생긴 오류였다!
#        stack.pop(i)