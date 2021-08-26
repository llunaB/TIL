import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    result = 0

    # 파리채의 시작점
    for i in range(N-M+1):
        for j in range(N-M+1):
            # print(data[i][j], i, j)
            # 임시변수 초기화
            fly = 0
            # 파리채
            for k in range(i, M+i):
                for l in range(j, M+j):
                    fly += data[k][l]
            if result < fly:
                result = fly

    # while문으로 바꿔보기

    print("#{} {}".format(tc, result))