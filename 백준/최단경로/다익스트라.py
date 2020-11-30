# 개선된 다익스트라 알고리즘에서는 우선순위 큐 (자료구조) heapq가 사용된다.
import heapq
INF=int(1e9)

n,m=map(int, input().split())
start=int(input()) # 출발 노드 선정
graph=[[]for i in range(n+1)] # 각 노드별 연결 정보
final=[INF]*(n+1) # 최단거리 테이블

# 간선의 갯수만큼 연결 정보 바로 입력 (입력도 처리해야 할 경우에)
for _ in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 비용을 첫번째 원소로 넣어준다. (최소 비용 pop)
    final[start]=0
    while q:
        distance, node = heapq.heappop(q)
        # 이미 방문한 경우
        if final[node]<distance:
            continue
        # 연결된 노드들의 최단거리 구해주기
        for linked in graph[node]:
            cost= distance+linked[1]
            if cost<final[linked[0]]:
                final[linked[0]]=cost
                heapq.heappush(q,(cost,linked[0]))