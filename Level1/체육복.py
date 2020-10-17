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
    # 먼저는 여벌의 옷이 있으면서 도난당한 학생을 제외해준다.
    # 방법 : set 집합 연산자로 reserve와 lost의 공통 원소를 제거해준다.
    lost2 = set(lost) - set(reserve)
    reserve2 = set(reserve) - set(lost)

    # reserve2 에서 순차탐색한 index에서 앞뒤 index의 학생이 lost2라면 lost2에서 index를 제거해준다.
    # 이유 : reserve2 index 학생이 빌려줄 것이기 때문에
    for j in reserve2:
        if j - 1 in lost2:
            lost2.remove(j - 1)
        elif j + 1 in lost2:
            lost2.remove(j + 1)
    # 결국 체육복을 입을 수 있는 학생은
    # 전체 학생에서 앞뒤 학생에게 빌려받지 못하고 lost2에 남아있는 학생의 수를 뺀 수이다.
    answer = n - len(lost2)
    return answer

n=5
lost=[2,4]
reserve=[1,3,5]

print(solution(n,lost,reserve))



