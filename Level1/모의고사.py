def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    count=[0]*4
    for i in range(len(answers)):
        if answers[i]==a[i%5]:
            count[1]+=1
        if answers[i]==b[i%8]:
            count[2]+=1
        if answers[i]==c[i%10]:
            count[3]+=1
    answer = []
    max_num = 0
    if count[1]==0 and count[2]==0 and count[3]==0:
        return answer
    for i in range(1,4):
        if count[i]>max_num:
            max_num=count[i]
            answer = [i]
        elif count[i]==max_num:
            answer.append(i)
        else:
            pass
    return answer

