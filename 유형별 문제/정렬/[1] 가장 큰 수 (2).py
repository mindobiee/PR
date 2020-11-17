# permutation 모든 경우의 수를 구하려고 하니 시간 초과 오류가 났다.
# 다른 방식으로 접근하는 것이 필요하다.

# 문자열을 내림차순으로 정렬한 다음, join 해주는 방식이다!
# 주의 : 처음에는 문자열로 비교할 것 !!(가장 큰 자릿수부터 비교 가능)


def solution(numbers):
    # 정수 type을 문자열 type으로 변경해주기 (map을 통한 형변환!)
    arr = list(map(str, numbers))
    print(arr) # ['6', '10', '2']

    # 문자열 크기대로 sorting하기
    # lambda : 1000이하의 정수이므로, x를 세 번 곱해주어 비교한다.
    array=sorted(arr, key=lambda x:x*3, reverse=True)
    print(array) # ['6', '2', '10']

    # join으로 각각의 문자열들을 빈틈없이 붙여주기
    # int로 바꾸어주고, 다시 str으로 바꿔주기
    return str(int("".join(array)))


print(solution([6,10,2]))