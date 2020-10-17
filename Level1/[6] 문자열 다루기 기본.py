def solution(s):
    # 문자열의 길이가 4나 6일 때
    if len(s)!=4 and len(s)!=6:
        return False
    # 숫자로만 구성되어 있는지 확인
    # 알파벳이 있으면 거짓을 리턴
    for i in s:
        if i.isalpha():
            return False
    return True
