import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(input()) for _ in range(N)]

    # 지도 순회
    for y in range(N):
        for x in range(N):

            # 만약 현재 위치가 기지국이라면,
            if mat[y][x] != 'X' and mat[y][x] != 'H':
                # 상하좌우 (1, 2, 3) 기지국이 커버할 크기 정하기
                delta = 0
                if mat[y][x] == 'A':
                    delta = 1
                elif mat[y][x] == 'B':
                    delta = 2
                elif mat[y][x] == 'C':
                    delta = 3

                # 기지국의 크기만큼 바꾸기
                # ex. B일 경우 k는 1, 2
                dy = (1, -1, 0, 0)
                dx = (0, 0, -1, 1)

                for k in range(1, delta+1):
                    for z in range(4):
                        ny = y + dy[z] * k
                        nx = x + dx[z] * k

                        # 지도 범위 안에 있는지 확인하고
                        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                            # (주의!) "집"이 아니면 바꾸지 말 것
                            if mat[ny][nx] == 'H':
                                mat[ny][nx] = 'X'

    # 지도 순회 끝!
    # 아직 남아있는 집이 있는지 확인하기
    result = 0
    for y in range(N):
        for x in range(N):
            if mat[y][x] == 'H':
                result += 1

    print('#{} {}'.format(tc, result))