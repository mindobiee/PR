from itertools import permutations
import math


def solution(numbers):
    answer = 0
    all_numbers = []
    # numbers 길이만큼 순열 구하기! 1<=n<=len(numbers)
    for n in range(1, len(numbers) + 1):
        all_numbers.append(list(permutations(numbers, n)))

    # list를 문자열로 바꾸어서 집합 set()에 넣기 (중복 x)
    set_numbers=set()
    for i in range(len(all_numbers)):
        for j in range(len(all_numbers[i])):
            temp='' # 각 순열 별로 문자열로 만들어주기
            for k in range(len(all_numbers[i][j])):
                temp = temp + all_numbers[i][j][k]
            # 저장한 문자열을 int형으로 set에 넣어주기 (0이 앞에 나오는 것 제거해줌)
            set_numbers.add(int(temp))

    # 소수 판별 및 count!
    # 인덱싱을 위해 set 데이터를 list로 옮겨주기
    last_list = sorted(set_numbers)
    # print(last_list)
    for n in last_list:
        if n==2:
            answer=answer+1
        elif n>2:
            point = True
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    point=False
                    break
            if point==True:
                answer=answer+1
    return answer

print(solution("110"))