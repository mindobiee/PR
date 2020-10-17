def solution(seoul):
    # 반복문을 이용하여 "Kim"이 있는 인덱스를 저장한다.
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            location=i
    # 정답 문자열을 만들어 준다.
    answer="김서방은 "+str(location)+"에 있다"
    return answer