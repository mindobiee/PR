-- 고양이와 개는 몇 마리 있을까

SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) AS count
from ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- result:
-- ANIMAL_TYPE	count
-- Cat	15
-- Dog	85

-- 동명 동물 수 찾기
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
-- 왜 틀렸지??

-- 연습문제
-- EMPLOYEES 테이블을 이용해 지점 별 총급여액이 얼마인지 조회하는 SQL문을 작성해주세요.
-- 단, 결과는 지점의 ID순으로 정렬되어야 합니다.
SELECT BRANCH_ID, SUM(SALARY) AS TOTAL
FROM EMPLOYEES
GROUP BY BRANCH_ID
ORDER BY BRANCH_ID ASC