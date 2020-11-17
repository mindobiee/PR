# 효율성 문제 해결 x
def solution(participant, completion):
    # 동명이인 처리
    # 참가자와 완주자 리스트를 비교해준다.
    for person in participant:
        # 완주자 리스트에 존재하지 않는 사람을 리턴
        if person not in completion:
            return person
        else:
            completion.remove(person)

# 사전 자료형을 이용해서 효율성 문제 해결하기!
def solution_final(participant, completion):
    # 사전형 집합 dict 사용하기
    dic = {}
    # 딕셔너리에 참가자의 이름을 대입한다.
    for person in participant:
        if person not in dic:
            dic[person] = 1
        else:
            dic[person] = dic.get(person) + 1

    # 완주자 명단에서 딕셔너리의 이름을 빼준다.
    for person in completion:
        dic[person] = dic.get(person) - 1

    # 값 데이터가 0이 아닌 key값을 리턴해준다.
    key_list = dic.keys()
    for key in key_list:
        if dic[key] != 0:
            return key