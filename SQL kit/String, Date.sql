-- 이름에 el이 들어가는 동물 찾기
-- 문자열 존재하는지
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog"
ORDER BY NAME

-- 오랜 기간 보호한 동물
-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요.
-- 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A
LEFT JOIN ANIMAL_OUTS AS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NOT NULL
ORDER BY B.DATETIME - A.DATETIME DESC
LIMIT 2
