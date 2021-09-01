import sys
sys.stdin = open("input_3.txt")

# rectangle

T = int(input())
for tc in range(1, T+1):
    R, C, M= map(int, input().split()) # R : 배열의 행 수, C : 배열의 열 수, M : 파리채의 크기
    arr = [list(map(int, input().split())) for _ in range(R)]

    max_result = 0
    for i in range(R-M+1):
        for j in range(C-M+1):
            fly = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    fly += arr[k][l]
            if max_result < fly:
                max_result = fly

    print("#{} {}".format(tc, max_result))

