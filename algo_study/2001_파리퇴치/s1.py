import sys
sys.stdin = open("input.txt")

# max

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 배열의 크기 M : 파리채의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(M):
                for l in range(M):
                    if 0 <= i < N - M + 1 and 0 <= j < N - M + 1:
                        total += arr[i+k][j+l]
            if max_total < total:
                max_total = total

    print("#{} {}".format(tc, max_total))