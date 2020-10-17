def solution(answers):
    # 1~3번 학생이 모의고사를 찍는 방법
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]

    # 1~3번 학생이 정답을 맞춘 갯수를 저장하는 리스트
    count=[0]*4

    # answer 리스트의 완전탐색
    for i in range(len(answers)):
        # 정답이 학생들이 찍은 답과 일치할 때마다 카운트 증가
        # n%m은 n을 m으로 나눈 나머지를 의미함.
        if answers[i]==a[i%5]:
            count[1]+=1
        if answers[i]==b[i%8]:
            count[2]+=1
        if answers[i]==c[i%10]:
            count[3]+=1
    # 1~3번 카운트를 비교해서 가장 큰 수를 리스트에 추가해준다.
    answer = []
    max_num = 0
    # 1~3번 학생 중 맞춘 정답이 하나도 없을 경우
    if count[1]==0 and count[2]==0 and count[3]==0:
        return answer

    # 1~3번의 반복문 속에서 max_num과 비교하여
    for i in range(1,4):
        # max_num보다 클 경우에는 max_num을 바꾸어준다.
        if count[i]>max_num:
            max_num=count[i]
            answer = [i]
        # max_num과 같을 경우에는 리스트에 추가해준다.
        elif count[i]==max_num:
            answer.append(i)
        # max_num보다 작은 경우에는 아무 것도 하지 않는다.
        else:
            pass
    return answer

