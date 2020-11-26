# 2진수로 변환했을 때 1의 갯수가 같다.

ans=0
key=0
def dfs(n):
    global ans
    global key
    if n==1:
        ans+=1
        return ans
    if n%2==1: # 나머지가 1일때 추가
        ans+=1
    return dfs(n//2)

def solution(n):
    global ans
    global key
    key = dfs(n)
    ans=0

    for n in range(n+1,1000000):
        temp=dfs(n)
        if temp==key:
            return n
        ans=0


print(solution(n=15))