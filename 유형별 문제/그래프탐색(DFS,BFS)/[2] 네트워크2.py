
def solution(n, computers):

    answer=0 # 정답 변수
    bfs=[] # 스택 준비
    visited=[0]*n # 방문여부 리스트

    while 0 in visited: # 방문이 다 되어질 때까지!(visited에 0 이 없을 때까지)
        bfs.append(visited.index(0)) # 방문하지 않은 노드 인덱스를 찾아서 추가
        while bfs: # bfs 리스트에 노드가 있을 때
            node=bfs.pop(0) # 앞에서부터 node pop!
            visited[node]=1

            for i in range(n): # 인접 노드를 방문하기
                if visited[i]==0 and computers[node][i]==1: # 아직 방문하지 않았고, 서로 연결되어 있을 때
                    bfs.append(i) # 연결된 i를 추가해주기

        # 연결되어 있는 노드의 방문이 끝났다면,
        answer+=1 # 카운트해주기
    return answer