def solution(genres, plays):
    answer = []
    # 같은 장르끼리 dict에 plays 수만큼 저장하기
    dic = dict()
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] = dic.get(genres[i]) + plays[i]

    # 각각의 plays수를 저장하는 list 만들기
    songs = []
    for i in range(len(genres)):
        songs.append([i, genres[i], plays[i]])
    songs = sorted(songs, key=lambda x: (x[2],x[0]), reverse=True)  # plays 큰 순서대로
    # 3번) 재생 횟수가 같을 경우에는, 고유 번호가 낮은 노래먼저! -> 여러 개의 요소 인 경우 :튜플로 사용 가능
    print(songs)

    # plays수 (value값) 순으로 정렬하기
    dic = sorted(dic, reverse=True)

    # 각 genre에서 재생수가 많은 곡 두 개 정해서 list-up
    # 이미 정렬되어 있는 것을 기준으로 !
    for genre in dic:  # 1번 ) 가장 많이 재생된 장르 순서대로
        count = 0
        for i in range(len(songs)):  # 장르 내에서 많이 재생된 노래 먼저 수록
            if genre == songs[i][1] and count < 2:
                answer.append(songs[i][0])
                count += 1
            elif count >= 2:
                break
    return answer


if __name__ == "__main__":
    genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    plqys = [500, 600, 150, 800, 2500]
    print(solution(genres,plqys))