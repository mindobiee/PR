dic=dict()
dic["a"]=1
dic["b"]=2
print(dic.get("a"))

keys = dic.keys() # key값들 리턴
values = dic.values() # value값들 리턴

for key in keys: # 반복문을 이용 가능
    print(key) # person, bird

if "c" in dic: # 해당 key 값이 있는지 확인
    print(True)
else:
    print(False) # False출력

array = [1, 2, 3, 4, 5]
temp = array[0:3] # 0번~2번 인덱스 값까지 슬라이싱
print(temp) # 1,2,3

from itertools import permutations
array=['A','B','C']

result=list(permutations(array, len(array)))
print(result)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

rresult=[]
for i in result: # 해당 문자열 리스트를 문자열로 바꾸기
    rresult.append(''.join(i))
print(rresult)
# ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
