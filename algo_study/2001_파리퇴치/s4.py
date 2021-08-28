import sys
sys.stdin = open("input_4.txt")

# cross

T = int(input())
for tc in range(1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    print(data)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    result = 0

    for i in range(N):
        for j in range(N):
            # 파리채
            fly = 0
            for s in range(i, M+i):
                for l in range(j, M+j):
                    k = 0
                    while k < 4:
                        ns = s + di[k]
                        nl = l + dj[k]
                        if 0 <= ns < N and 0 <= nl < N:
                            fly += data[ns][nl]
                        k = k+1
            if result < fly:
                result = fly

    print("#{} {}".format(tc,result))