# 큰 것 -> 작은 순으로 정렬 : 새로운 문자열 리턴, 대문자는 뒤로

def solution(s):
    return "".join(sorted(list(s),reverse=True))

# list1.sort() 적용 x, sorted(list1) ok
# 문자열 -> 리스트로 : list({문자열})
# 리스트 -> 문자열로 : "".join({리스트})

str="AbcdrfPldk"
print(solution(str))