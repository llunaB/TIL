import sys
sys.stdin = open("input.txt")

T = int(input())

def check_row(arr):
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1

        for k in range(10):
            if count[k] >= 2:
                return False
    return True


def check_col(arr):
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[j][i]] += 1

        for k in range(10):
            if count[k] >= 2:
                return False
    return True

def check_squre(arr):
    for i in range(9):
        for j in range(9):
            count = [0] * 10
            for k in range(3*i, 3*i + 3):
                for l in range(3*i, 3*i + 3):
                    if 0 <= 3*i < 10 and 0 <= 3*i + 3 < 10:
                        count[arr[k][l]] += 1

            for s in range(10):
                if count[s] >= 2:
                    return False
    return True

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = check_row(arr) and check_col(arr) and check_squre(arr)

    if result == False:
        result = 0
    if result == True:
        result = 1

    print("#{} {}".format(tc, result))