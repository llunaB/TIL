import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())  # array row & col
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        flag = False
        for j in range(N):
                if arr[i][j] == 1:
                    flag = True
                    for k in range(i+1, N):
                        if arr[k][j] ==1:
                            flag = False
                            break
                        if arr[k][j] == 2:
                            flag = False
                            cnt += 1
                            break
                else:
                    flag = False


    print("#{} {}".format(tc, cnt))
