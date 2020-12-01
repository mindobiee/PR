# programmars

- @ [프로그래머스 코딩테스트 연습](https://programmers.co.kr/learn/challenges)

## 프로그래밍 유형

### 연습문제
- [x] 다음 큰 숫자
### 완전탐색
- [x] 카페트
- [x] 소수찾기

#### 순열
```python
from itertools import permutations
array=['A','B','C']

result=list(permutations(array, len(array))) # 해당 리스트에서 해당 갯수만큼의 순열 구하기 
print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

rresult=[]
for i in result: # 해당 문자열 리스트를 문자열로 바꾸기
    rresult.append(''.join(i))
print(rresult)
# ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
```
### 정렬
- [x] 가장 큰 수
### Hash
- [x] 완주하지 못한 선수
- [x] 위장
- [ ] 베스트 앨범
- [x] 전화번호 목록
#### 사전 자료형 Dict()
- key-value값을 가지는 자료구조
```python
dic=dict() # 사전 자료형의 초기화
dic["person"]="한국인"
dic["bird"]="앵무새"

nation = dic.get("person") #해당 key값에 해당하는 값 추출
keys = dic.keys() # key값들 리턴
values = dic.values() # value값들 리턴

for key in keys: # 반복문을 이용 가능 
    print(key) # person, bird

if "person" in dic: # 해당 key 값이 있는지 확인 
    print(True)
else:
    print(False)
```

### Heap
- [x] 스코빌 지수
- [ ] 디스크 컨트롤러
#### 우선순위큐 Heapq
- 우선순위가 **가장 높은 데이터**부터 pop
- 기본적으로 최소힙을 지원하나, 음의 부호를 붙여서 삽입, 삭제하여 최대힙 만들 수 있음. 
- 시간 복잡도 : 삽입 O(logN), 삭제 O(logN)
```python
import heapq

h=[3,4,1,2,5]
heapq.heapify(h)# 리스트를 힙으로 바꾸기
while h:
    new=heapq.heappop(h) # 삭제
    ...
    heapq.heappush(h,new) # 삽입
```


### 그래프 탐색 (DFS,BFS)
- [x] 타겟 넘버 
- [x] 네트워크 
- [ ] 여행 경로 (75%) 
- [x] 가장 먼 노드 
#### DFS
- 재귀함수를 통한 stack 이용
- 깊이 우선 탐색, 최대한 멀리 있는 노드를 우선으로 탐색
```python
def dfs(graph,node,visited):
    visited[node]=True # 방문처리하기 
    for i in graph[node]: # 연결된 요소들 중에서
        if not visited[i]: # 방문하지 않았으면,
            dfs(graph,i,visited) # 재귀 함수 호출:)
    
dfs(graph,1,visited)
```


#### BFS
- collections의 deque를 통한 queue이용
- 너비 우선 탐색, 가까운 노드부터 탐색

```python
from collections import deque

def bfs(graph, start,visited):
    q=deque(start) # start노드 초기화 
    visited[start]=True
    while q: # 큐가 없어질 때까지
        value=q.popleft() # 가장 먼저 들어온 값부터 출력
        for i in graph[value]: # 각 노드가 연결된 리스트 
            if not visited[i]: # 방문하지 않은 노드들을 큐에 삽입
                q.append(i)
                visited[i]=True
visited=[False]*9
graph=[
    [],
    [2,3,8],
    [1,7],
    ...
]
bfs(graph,1,visited)

```

  
### 그리디
- [x] 큰 수 만들기
- [x] 구명보트 
#### List의 활용
```python
def solution(number,k):
    list=[number[0]]
    for i in number[1:]: # 인덱스 1번부터 
        while len(list)>0 and list[-1]<i and k>0:
            k=-1
            list.pop() # 맨 뒤의 원소 
        list.append(i) # 원소의 추가                 


list1=['hello','nice','to','meet','you'] # 리스트 생성과 동시에 초기화
list1.insert(1,'bye') # 해당 인덱스에 원소 추가
list1.remove('hello') # 해당 원소 제거
list1.count('bye') # 해당 원소 갯수 계수
list1.sort() # 오름차순 정렬
del list1[1:3] # 범위를 지정해서 삭제
list1.pop(1) # 해당 인덱스의 원소 제거
```


### 스택, 큐
- [x] 프린터
- [ ] 기능개발
### DP
- [ ] 정수 삼각형

#### 문제 접근 방법 
- 중복 되는 연산을 줄이자!
- 메모리 공간을 사용하여(Memoization) 연산 속도를 증가시키는 방법 
  - 큰 문제에서 작은 문제를 나눌 수 있다. **(최적 부분 구조)** 
  - 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. **(중복되는 문제)**
- 예) 피보나치 수열
```python
def solution(n):
    d = [0] * 100 # DP 테이블의 초기화 
    for i in range(0, n + 1): # Bottom-up 방식
        if i == 0:
            d[0] = 0
        elif i == 1 or i == 2:
            d[i] = 1
        else:
            d[i] = d[i - 1] + d[i - 2] # 앞서 저장해둔 것 활용!
    return d[n]
```  

### 최단경로
- [x] 다익스트라
- [x] 플로이드
  
 ## MySQL
- SELECT
- SUM, MAX,MIN
- GROUP BY
- STRING,DATE
- JOIN
```
SET @HOUR_LIST=-1; -- 변수 선언 및 초기화
SELECT (@HOUR_LIST := @ HOUR_LIST +1) AS HOUR
WHERE @HOUR_LIST<23;
```