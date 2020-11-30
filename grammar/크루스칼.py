# 유니온 파인드 (사이클 생성하는지 확인)

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
        return parent[x]
def union_parent(parent, a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 입력받기
v, e=map(int, input().split()) # 노드, 간선 갯수
parent=[0]*(v+1) # 노드의 갯수만큼 리스트 생성
edges=[]

# 자기 자신을 부모로 초기화하기
for i in range(1, v+1):
    parent[i]=i

# 간선 리스트에 노드와 비용 저장하기
for _ in range(e):
    a,b,cost=map(int, input().split())
    edges.append((cost,a,b))

edges.sort() # cost순으로 정렬하기 (!)

result=0
for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b): # 사이클을 형성하지 않는다면,
        union_parent(a,b)
        result+=cost

print(result)