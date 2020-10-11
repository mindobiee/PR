
def solution(array, commands):
    answer = []
    # 2차원 배열인 commands에 대해 열의 길이만큼 반복해주어
    # 배열을 하나씩 처리해준다.
    for i in range(len(commands)):
        list= commands[i]
        start = list[0]
        end = list[1]
        order = list[2]
        # 리스트의 슬라이싱 기법을 이용해서 한번에 배열을 만들어준다.
        # 슬라이싱배열 [첫번째 인덱스:마지막 인덱스+1] 이므로
        # start 번째부터 end 번째까지의 원소를 가지는 배열을 만들고 싶으면 아래와 같이 작성한다.
        temp = array[start-1:end]
        # 배열을 오름차순으로 정렬한다.
        temp.sort()
        # list가 0번부터 시작하기 때문에 구하고자하는 인덱스 값에 -1해준다.
        answer.append(temp[order-1])

    return answer

if __name__ == "__main__":

    array=[1, 5, 2, 6, 3, 7, 4]
    commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = solution(array,commands)
    print(answer)