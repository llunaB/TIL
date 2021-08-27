import sys
sys.stdin = open("input.txt")

T = int(input())

# 4 3

for tc in range(1, T+1):
    N = int(input()) # N * N 배열
    arr = [list(input()) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0

    pass_list = ['X', 'A', 'B', 'C', 'DD']

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                # 네방향 돈다 + 'X' 와 'B', 'C', ' ' 는 그냥 두고 'H'이면 'H'를 공백으로 치환
                while k < 4:
                        ni, nj = i+di[k], j+dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] in pass_list:
                                pass
                            elif arr[ni][nj] == 'H':
                                arr[ni][nj] = arr[ni][nj].replace('H','DD')
                            k = k+1

            if arr[i][j] == 'B':
                # 네 방향을 두 번 돈다 + 'X' 와 'B', 'C', ' ' 는 그냥 두고 'H'이면 'H'를 공백으로 치환
                while k < 4:
                    for t in range(2):
                        ni, nj = i + di[k], j + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                                if arr[ni][nj] in pass_list:
                                    pass
                                elif arr[ni][nj] == 'H':
                                    arr[ni][nj].replace('H','DD')
                                k = k+1

            if arr[i][j] == 'C':
                # 네 방향을 세 번 돈다 + 'X' 와 'B', 'C' , ' ' 는 그냥 두고 'H'이면 'H'를 공백으로 치환
                while k < 4:
                    for t in range(3):
                        ni, nj = i+di[k], j+dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] in pass_list:
                                pass
                            elif arr[ni][nj] == 'H':
                                arr[ni][nj].replace('H','DD')
                            k = k+1


    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(cnt)
