import sys
sys.stdin = open("s_input.txt")
# T = int(input())
#
# def result(numbers):
#     increasing = []
#     for k in range(len(numbers)):
#         if numbers[k] // 10 <= numbers[k] % 10:
#             increasing.append(numbers[k])
#         else:
#             pass
#
#     if len(increasing) == 0:
#         return -1
#     else:
#         return max(increasing)
#
# for tc in range(1, T+1):
#
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     numbers = []
#     for i in range(N):
#         for j in range(N):
#             if i < j:
#                 numbers.append(arr[i] * arr[j])
#
#     print("#{} {}".format(tc, result(numbers)))