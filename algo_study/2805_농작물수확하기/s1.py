import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    total = 0
    # 가장 중간 열을 기준으로 한 행씩 내린다.
    for i in range(N): # i = 1
        # 중앙에 닿기 전~ 중앙
        if i <= N // 2:
            total += sum(arr[i][N//2-i : N//2+i+1])
        # 중앙을 지난 후
        if i > N // 2:
            total += sum(arr[i][N//2-(N-i-1) : N//2+(N-i-1)+1])

    print("#{} {}".format(tc, total))