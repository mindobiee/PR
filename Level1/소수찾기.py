# 에스토스테라스의 체를 이용하기!!!
import math


def solution(n):
    # 먼저 1~n까지 전부 소수라고 초기화해준다.
    array = [True for _ in range(n+1)]
    total = 0
    # 약수의 중간 값인 제곱근을 이용한다.
    for i in range(2, int(math.sqrt(n))+1):
        if array[i]:
            # i의 j 배수도 소수가 아님을 check 한다.
            j=2
            while j*i <= n:
                array[j*i] = False
                j += 1
    # 마지막에 소수의 갯수를 구해준다.
    for i in range(2, n+1):
        if array[i]:
            total += 1
    return total

# total = 0
# n=10
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, num - 1):
#         if num != 2 and num % i == 0:
#             is_prime = False
#             break
#     if is_prime == True:
#         total += 1
# print(total)
#
# def solution(n):
#     total = 0
#     for num in range(2, n + 1):
#         is_prime = True
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num != 2 and num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime == True:
#             total += 1
#
#     return total


solution(10)
