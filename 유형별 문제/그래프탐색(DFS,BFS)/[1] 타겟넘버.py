# 주어진 numbers 배열을 적절히 +/-를 해서 target 숫자를 만들어주는 것!
# dfs 사용하기
answer=0


# dfs 함수
def dfs(numbers, target, sum, index):
    global answer
    if index>=len(numbers): # 길이가 다 될때까지 탐색하고, target과 같은지 확인하기
        if sum==target:
            answer=answer+1
        return
    # 재귀적이니 용법을 사용한다. (+)일때, (-)일때
    dfs(numbers,target,sum+numbers[index],index+1) # 하나는 +
    dfs(numbers,target,sum-numbers[index],index+1) # 하나는 -


def solution(numbers, target):
    global answer # 전역변수 사용하기 위한 global 키워드
    dfs(numbers, target,0,0) # 0번 인덱스부터 시작
    return answer



print(solution(numbers=[1, 1, 1, 1, 1], target=3))