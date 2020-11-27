
# 알파벳 소문자와 대문자 리스트 만들기
import string

lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
print(lower)
print(upper)

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Enumerate를 활용한 인덱스와 값 추출
array=["hi","rosie"]
for idx, value in enumerate(array):
    print(f'{idx}번째 요소: {value}입니다.')

# 0번째 요소: hi입니다.
# 1번째 요소: rosie입니다.



# 코딩테스트에서 이진탐색을 쉽게 할 수 있게 해주는 bisect!
# (https://docs.python.org/ko/3/library/bisect.html)

from bisect import bisect_left,bisect_right

nums=[1,2,3,4,5,6,7]
n=4
print(bisect_right(nums,n)) #오른쪽 인덱스 4
print(bisect_left(nums,n)) #왼쪽 인덱스 3
