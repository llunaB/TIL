import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)

    # result = 0

    # 파리채의 시작점
    # for i in range(N-M+1):
    #     for j in range(N-M+1):
    #         print(data[i][j], i, j)
    #         # 임시변수 초기화
    #         fly = 0
    #         # 파리채
    #         for k in range(i, M+i):
    #             for l in range(j, M+j):
    #                 fly += data[k][l]
    #         if result < fly:
    #             result = fly

    # while문으로 바꿔보기
    result = 0
    k, l = 0, 0

    i, j = 0, 0
    while i < N-M+1:
        while j < N-M+1:
            fly = 0
            k = i
            while k < M+i:
                l = j
                while l < M+j:
                    fly += data[k][l]
                    l = l+1
                k = k+1
            if result < fly:
                result = fly
            j = j + 1
        i = i+1
        j = 0


    print("#{} {}".format(tc, result))