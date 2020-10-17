def solution(strings, n):
    array=[]
    result=[]
    # 각 word의 n번째 원소와 word를 새 array에 저장한다. (word[n],word)
    for word in strings:
        array.append((word[n],word))

    # array에 저장된 첫번째 원소(word[n])를 기준으로 sort된다. a.sort()
    array.sort()

    # result는 array에서 두번째 원소인 (word)만 저장해주기
    for i in array:
        result.append(i[1])
    return result