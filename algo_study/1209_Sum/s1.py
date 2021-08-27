import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    num = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 최종 결괏값
    result = 0
    value_xx = 0
    value_xy = 0
    for x in range(100):
        value = 0
        value_col = 0
        value_xx += data[x][x]
        value_xy += data[x][99-x]
        for y in range(100):
            value += data[x][y]
            value_col += data[y][x]
        if result < value:
            result = value
        if result < value_col:
            result = value_col
    if result < value_xx:
        result = value_xx
    if result < value_xy:
        result = value_xy

    print("#{} {}".format(num, result))