# 코딩테스트에서 이진탐색을 쉽게 할 수 있게 해주는 bisect!
# https://docs.python.org/ko/3/library/bisect.html


from bisect import bisect_left,bisect_right

nums=[1,2,3,4,5,6,7]
n=4
print(bisect_right(nums,n)) #오른쪽 인덱스
print(bisect_left(nums,n)) #왼쪽 인덱스