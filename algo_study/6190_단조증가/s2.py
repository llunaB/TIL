T = int(input())

for TC in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_value = -1
    for i in range(N - 1):
        for j in range(i + 1, N):
            check = str(arr[i] * arr[j])
            answer = 1
            for k in range(len(check) - 1):
                if check[k] > check[k + 1]:
                    answer = -1
                    break
            if answer == 1 and int(check) > max_value:
                max_value = int(check)

    print('#{} {}'.format(TC, max_value))