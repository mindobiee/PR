# 파이썬 기본 문법 정리
# 괄호 대신 ':'와 인덴트 이용

# 반복문
# 1부터 9까지의 합을 구하기
sum = 0
for index in range(1, 10):
    sum += index
print(sum)

# range(start,end+1) : start~end 의 범위

# 리스트
array = [1, 2, 3, 4, 5]
# 리스트 슬라이싱 arr[start, end+1]
temp = array[1:3]
print(temp)

# 리스트의 원소에 한 개씩 접근
for a in array:
    print(a)

# 리스트 관련 메서드
# 원소 삽입
array.append(1)
# 오름/내림차순 정렬
array.sort(reverse=True)
# 원소 뒤집기
array.reverse()
# 특정 인덱스에 데이터 추가 (인덱스번호, 원소값)
array.insert(3, 10)
# 특정 값 갯수 세기
array.count(1)
# 특정 값 데이터 삭제 - 1개 밖에 안됨
array.remove(1)
print(array)



# 집합 자료형
# 중복 x, 순서 x : 이미 원소가 존재하는지 판별 시 좋음
s1 = {1, 3, 4, 6, 7}
s2 = {1, 2, 3, 4, 5}
print(s1-s2) # 차집합
print(s1 | s2) # 합집합
print(s1 & s2) # 교집합

# 사전 자료형
d = dict()
d['a'] = 100
print(d)