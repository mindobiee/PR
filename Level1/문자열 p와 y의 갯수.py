def solution(s):
    # 알파벳을 모두 소문자로 만든다.
    s = s.lower()

    # "p"와 "y"의 count가 같으면 True 리턴
    if s.count("p") == s.count("y"):
        return True
    else:
        return False
