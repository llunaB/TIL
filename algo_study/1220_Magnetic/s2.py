import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input()) # array row & col
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            # 행우선순회하다 1을 만나면
            if arr[i][j] == 1:
                # 열을 내리면서 체크한다
                for k in range(i+1, N):
                    # 만약 2를 만나면 => 카운트 +1, 두 숫자를 모두 3으로 치환한다.
                    if arr[k][j] == 2:
                        cnt += 1
                        arr[i][j] = 3
                        arr[k][j] =3
                        break

                    # 0, 3 을 만나면 패스한다
                    if arr[k][j] == 0 or arr[k][j] == 3:
                        pass

                    # 1을 만나면 => 그 자리에 대기한다.
                    if arr[k][j] == 1:
                        pass
                        break


    print("#{} {}".format(tc, cnt))