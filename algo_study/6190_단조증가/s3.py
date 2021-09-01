def check(number):
    temp_str = str(number)
    for k in range(len(temp_str) - 1):
        if temp_str[k] > temp_str[k + 1]:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    danjo = []
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            ij = num[i] * num[j]
            if ans < ij and check(ij):
                ans = ij
    print('#{} {}'.format(tc, ans))