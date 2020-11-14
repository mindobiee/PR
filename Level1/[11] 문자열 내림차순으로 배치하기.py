# 큰 것 -> 작은 순으로 정렬 : 새로운 문자열 리턴, 대문자는 뒤로

from functools import cmp_to_key
# def cmp_to_key(mycmp):
#     class K:
#         def __init__(self, obj, *args):
#             self.obj = self
# key=cmp_to_key(reverse_numeric)
#
# 처음 시도한 것 : 실행 ok, test fail
def solution0(s):
    answer = ''
    # str -> list
    list1=[]
    for i in s:
        list1.append(i)

    # list1.sort() 적용 x, sorted(list1) ok
    sorted(list1, reverse=True)

    # list -> string
    for i in list1:
        answer=i+answer

    return answer


def solution(s):
    return "".join(sorted(list(s),reverse=True))

# list1.sort() 적용 x, sorted(list1) ok
# 문자열 -> 리스트로 : list({문자열})
# 리스트 -> 문자열로 : "".join({리스트})


str="AbcdrfPldk"
sr2="Zbcdefg"
print(solution(str))