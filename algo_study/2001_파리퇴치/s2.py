import sys
sys.stdin = open("input_2.txt")

# min

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채
            fly = 0
            for k in range(i, M+i):
                for l in range(j, M+j):
                    fly += data[k][l]
            result.append(fly)

    min_fly = result[0]
    for i in range(len(result)):
        if min_fly > result[i]:
            min_fly = result[i]

    print("#{} {}".format(tc,min_fly))