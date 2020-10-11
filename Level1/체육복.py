# 그리디 문제

# def solution(n, lost, reserve):
#     # lost -> reserve 에서 빌릴 수 있으면 reserve의 원소를 제거한다.
#     answer = 0
#     for j in lost:
#         if j in reserve:
#             reserve.remove(j)
#         elif j - 1 in reserve:
#             reserve.remove(j - 1)
#         elif j + 1 in reserve:
#             reserve.remove(j + 1)
#         else:
#             answer += 1
#     answer = n - answer
#     return answer

# 테스트 케이스 1개 오류
# 수정
def solution(n, lost, reserve):
    # reserve와 lost의 공통 원소를 제거해준다.(여벌+도난)
    lost2 = set(lost) - set(reserve)
    reserve2 = set(reserve) - set(lost)

    for j in reserve2:
        if j - 1 in lost2:
            lost2.remove(j - 1)
        elif j + 1 in lost2:
            lost2.remove(j + 1)

    answer = n - len(lost2)
    return answer

n=5
lost=[2,4]
reserve=[1,3,5]

print(solution(n,lost,reserve))



