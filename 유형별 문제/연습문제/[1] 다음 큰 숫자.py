# https://programmers.co.kr/learn/courses/30/lessons/12911
# 2진수로 변환했을 때 1의 갯수가 같다.
# 정확성, 효율성 - ok

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
    key = dfs(n) # 2진법 1의 갯수 세주기
    ans=0

    for n in range(n+1,1000000):
        temp=dfs(n)
        if temp==key:
            return n
        ans=0


print(solution(n=15))

# 다른 분 코드
# bin이란 아이를 사용

def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n