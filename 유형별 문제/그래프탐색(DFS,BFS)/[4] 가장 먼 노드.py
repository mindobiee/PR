from collections import deque

def bfs(node,graph,visited):
    count=0
    q=deque([[node,count]])
    while q:
        value=q.popleft() # 가장 적은 값을 pop 시키는 deque의 성질 이용
        v,count=value[0],value[1]
        if visited[v]==-1: # 방문한 적이 없다면,
            visited[v]=count
            count+=1
            for e in graph[v]: # 연결된 노드에 대해서
                q.append([e,count])


def solution(n,edge):
    visited=[-1]*(n+1)

    # 서로 연결 관계 형성
    graph = [[] for i in range(n + 1)]
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])
    print(graph) # [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    bfs(1, graph,visited)

    # 최대 거리 갯수 계수
    max_distance=max(visited)
    count=0
    for val in visited:
        if val==max_distance:
            count+=1
    return count





print(solution(n=6, edge=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))