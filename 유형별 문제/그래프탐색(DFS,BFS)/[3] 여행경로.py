# 여행 경로 - https://programmers.co.kr/learn/courses/30/lessons/43164
# 항상 ICN 공항에서 출발 / 2차원 배열 tickets 매개변수 /방문하는 공항 경로?
# DFS/BFS -> DFS 사용하기


def dfs(n,answer,tickets,ic):

    end=tickets[n][1]
    answer.append(end)
    print(n)
    if len(ic)==len(tickets):
        return

    for i in range(0, len(tickets)):
        start=tickets[i][0]
        if start == end and ic.count(i)==0:
            ic.append(i)
            print(ic)
            dfs(i,answer,tickets,ic)


def solution(tickets):
    ic=[]
    tickets=sorted(tickets,key=lambda x:x[1])
    print(tickets)
    # ICN 알파벳 순서로 출발 리스트 정하기
    for i in range(0,len(tickets)):
        if tickets[i][0]=="ICN":
            answer = [tickets[i][0]]
            ic.append(i)
            dfs(i, answer, tickets, ic)
            return answer





print(solution(tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"],
                        ["ATL", "ICN"], ["ATL","SFO"]]))

# 답 : [ICN, ATL, ICN, SFO, ATL, SFO]