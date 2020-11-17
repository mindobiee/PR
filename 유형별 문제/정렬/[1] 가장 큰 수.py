# 가장 큰 수
# 주어진 numbers에서 정수를 이어붙여서 만들 수 있는 가장 큰 수를 찾는다.
# 정수를 붙이는 순열 이용 => 그 중 가장 큰 수 찾기
from itertools import permutations


def solution(numbers):
    answer_list = []
    all_list=list(permutations(numbers,len(numbers)))
    for i in range(len(all_list)):
        temp=""
        for j in range(len(all_list[i])):
            temp = temp +str(all_list[i][j])
        answer_list.append(temp)
    print(answer_list)
    answer=max(answer_list)
    return answer


print(solution([6,10,2]))

# 결과 : 시간 초과!!!