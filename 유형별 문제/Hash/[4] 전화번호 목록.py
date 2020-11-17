# 전화번호 중, 다른 번호의 접두어와 일치하는 경우 false 리턴 or true 리턴
# 접두어 : 첫번째 단어 일치 + 그 단어가 있는지 확인하기!

# dict() : 사전 자료형 key-value
# set() : 집합 자료형 {set이름}=set({list이름})을 통해 선언 가능

def solution(phone_book):
    # 선택 정렬의 방법 이용
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i][0] == phone_book[j][0]: # 접두어가 같으면
                if phone_book[i] in phone_book[j] or phone_book[j] in phone_book[i]: # 서로 포함되어 있는지를 확인한다.
                    return False
    return True

print(solution(["119", "97674223", "1195524421"]))