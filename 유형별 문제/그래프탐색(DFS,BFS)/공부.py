# dfs 예시 (1) - DFS 알고리즘 강의 (youtube)
# https://www.youtube.com/watch?v=RNU2j-l6mCM
# 이해하는 방법 : 트리를 생각하자.

arr=[[]for _ in range(11)]

def dfs(depth):
    global n, arr # 전역변수를 함수로 가져와주기
    if depth > n: # 반복하는 깊이가 n보다 크다면,
        # 문제마다 다른 구간(1)
        for i in range(1,n+1): # 1~n 인덱스까지의 배열값 출력
            print(arr[i],end=',')
        print('')
        return # 더 이상 탐색할 필요 없으므로 반드시 리턴해줄 것.
    # 문제마다 다른 구간(2)
    for i in range(1,7): # 1번부터 6번(노드)까지 (가로길이) 탐색
        arr[depth]=i # i를 대입해주기
        dfs(depth+1) #재귀적 용법 (+1번의 노드 탐색)

n= int(input()) # 사용자에게 input으로 받는 int값
dfs(1) #노드 1에서부터 시작

# 트리모양
#            1 2 3 4 5 6
#       1 2 3 4 5 6
# 1 2 3 4 5 6
# ....
