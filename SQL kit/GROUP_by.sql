-- 고양이와 개는 몇 마리 있을까

SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) AS count
from ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- result:
-- ANIMAL_TYPE	count
-- Cat	15
-- Dog	85