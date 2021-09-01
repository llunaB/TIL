import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) < len(B): # N < M , len(A) < len(B)
        repeat_cnt = M - N + 1
        max_total = 0
        for i in range(repeat_cnt):
            total = 0
            for j in range(N):
                total += A[j] * B[j]
            B.pop(0)

            if max_total < total:
                max_total = total

    else: # N > M, len(A) > len(B)
        repeat_cnt = N - M + 1
        max_total = 0
        for i in range(repeat_cnt):
            total = 0
            for j in range(M):
                total += A[j] * B[j]
            A.pop(0)

            if max_total < total:
                max_total = total

    print("#{} {}".format(tc, max_total))