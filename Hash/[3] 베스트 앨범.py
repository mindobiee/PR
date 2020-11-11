def solution(genres, plays):
    answer = []
    # 같은 장르끼리 dict에 plays 수만큼 저장하기
    dic = dict()
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] = dic.get(genres[i]) + plays[i]
    # plays수 (value값) 순으로 정렬하기
    res = sorted(dic, key=(lambda x: x[1]), reverse=True)
    print(res)
    # 각 genre에서 재생수가 많은 곡 두 개 정해서 list-up
    # 3번 항목도 고려할 대상 ! (재생 횟수가 같은 노래일 경우)
    for gen in res:
        temp = []
        for i in range(len(genres)):
            if gen == genres[i]:
                temp.append([plays[i],i])
        temp.sort(reverse=True) # 첫 번째 인수를 기준으로 정렬됨(plays수)
        print(temp)
        answer.append(temp[0][1])
        answer.append(temp[1][1])

    return answer


if __name__ == "__main__":
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plqys = [500, 600, 150, 800, 2500]
    print(solution(genres,plqys))