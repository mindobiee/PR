def solution(clothes):
    answer = 1
    dic = {}
    # 딕셔너리로 key - value 저장
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] = dic.get(cloth[1]) + 1
    # 정답을 구하는 로직 (경우의 수)
    for one in dic:
        answer = answer * (dic[one]+1)
    # 1을 빼는 이유는 아무 것도 안 입었을 경우
    return answer-1

    # 아래 오류 난 것 : TypeError: 'dict_values' object is not subscriptable
    # 원인 : dic_value는 인덱스로 접근 불가
    # values = dic.values()
    # # 항목이 한 개이면 그 value의 값
    # if len(values) == 1:
    #     return values[0]
    # else:
    #     # 두 개 이상이면 각 (count+1)씩 곱하기
    #     for val in values:
    #         answer = answer * (val + 1)
    #     return (answer-1)


if __name__ == "__main__":
    print(solution(clothes=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'],
                      ['green_turban', 'headgear']]))