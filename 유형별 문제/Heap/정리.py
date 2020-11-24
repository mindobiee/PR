import heapq # min-priority-queue 구조!

testheap=[4,8,2,0,3,1,5,9]
heapq.heapify(testheap) # heapify({list명}) : heap 구조로 만들어준다.
print(testheap) # [0, 3, 1, 8, 4, 2, 5, 9]

testheap=[]
heapq.heappush(testheap,3) # heappush : 힙에 요소 추가하기
heapq.heappush(testheap,5)
heapq.heappush(testheap,1)
heapq.heappush(testheap,-3)
print(testheap) # [-3, 1, 3, 5]

first=heapq.heappop(testheap) # heappop (첫번째 원소부터 pop)
print(first)

# maxheap 구현하기 (-)를 붙여주며 push, pop
a=[3,5,2,4,1]
testheap=[]
for i in a:
    heapq.heappush(testheap,-i)
for i in range(5):
    print(-heapq.heappop(testheap))
# 5
# 4
# 3
# 2
# 1

