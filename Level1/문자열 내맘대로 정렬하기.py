def solution(strings, n):
    array=[]
    result=[]
    for word in strings:
        array.append((word[n],word))
    # 첫번째 원소인 인덱스 n을 기준으로 sort된다.
    array.sort()
    # word 만 저장해주기
    for i in array:
        result.append(i[1])
    return result