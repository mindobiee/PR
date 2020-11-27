# 1. 피보나치 수열

def solution(self, n):
    d = [0] * 100 # 처음에 80으로 사이징을 했더니 런타임 에러가 났다... 왜지 ㅎ
    # 다이나믹 프로그래밍을 이용하여
    # 기록된 값을 더해준다.
    for i in range(0, n + 1):
        if i == 0:
            d[0] = 0
        elif i == 1 or i == 2:
            d[i] = 1
        else:
            d[i] = d[i - 1] + d[i - 2]
    return d[n]

print(solution(self=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,],n=10))

# 2. dp (배낭 채우기 문제...) 다시보기 (24번째 예시 실패ㅜ)

def knapsack(w, v, k):
    n = len(w)
    array = [[0 for _ in range(k + 1)] for _ in range(n + 1)] # 2차원 배열 만들기
    for i in range(n + 1):
        for j in range(k + 1):
            if i == 0 or j == 0:
                array[i][j] = 0
            elif w[i - 1] <= j:
                array[i][j] = max(v[i-1] + array[i - 1][j - w[i - 1]], array[i - 1][j])
            else:
                array[i][j] = array[i - 1][j]

    return array[n][k]

w = [10,20,30] # 무게
v = [60,100,120] # 가치
k = 50
print(knapsack(w,v,k))


# 3. 금광 문제 (미완성)
from collections import deque


# idx와 idx2 사이에 있는 원소 2개(최댓값) 빼주기
def dfs(i,j,sum,q):
 #   for i in range(total_length):
    idx,val=q.pop()

    if not q:
        return
    dfs(i+1,j,sum,q)


def solution(goldValues):
    sum=0
    total_length=len(goldValues)
    q = deque()
    for i,val in enumerate(goldValues):
        q.append([1,val])
    idx, val = q.pop()
    sum += val
    idx2,val2 = q.pop()
    dfs(idx,idx2,sum,q)
    return

solution(goldValues= [2,1,4,1,2,1,8,1]) # 12