# https://programmers.co.kr/learn/courses/30/lessons/42883
# number 에서 k개 만큼이 숫자를 뺀 수 중에 가장 큰 수 구하기

from collections import deque

# 스택
# 앞전의 숫자랑 비교했을 때 큰 값으로 채택하기
def solution(number,k): #1924, 2
    list=[number[0]] #제일 앞에 있는 숫자
    # print(list)
    for i in number[1:]: #두 번째~끝까지의 숫자
        # print(list[-1],end=', i=')
        # print(i)
        while len(list)>0 and list[-1]<i and k>0:
            # 제거의 조건 : 아직 제거할 숫자가 남아있고, 가장 마지막에 들어온 값보다 클 때
            k-=1
            list.pop()
        list.append(i) #원소는 계속적으로 추가해준다.
    if k!=0:
        list=list[:-k] #길이 조절
    return ''.join(list)

# 큐
def solution(number, k):
    del_num,stack,queue=0,[],deque(number)

    while queue and del_num<k:
        stack.append(queue.popleft())

        while stack and stack[-1]<queue[0]:
            stack.pop()
            del_num+=1
            if del_num ==k:
                break
    stack=stack[:-k] if del_num !=k else stack + list(queue)
    return ''.join(stack)


number="1924"
k=2
print(solution(number,k))
