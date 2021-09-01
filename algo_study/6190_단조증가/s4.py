import sys
sys.stdin = open("s_input.txt")

def check_mono_increase(num):
    """
    주어진 숫자가 단조 증가하는 수인지 확인한다.
    Args:
        num: 확인할 수 (int)
    Returns:
        주어진 수가 단조 증가하는 수면 True, 아니면 False
    """
    str_num = str(num)

    length = len(str_num)

    for i in range(length - 1):
        if str_num[i] > str_num[i + 1]:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = [int(x) for x in input().split()]
    print(numbers)

    max_result = -1

    for i in range(N - 1):
        for j in range(i + 1, N):
            current = numbers[i] * numbers[j]
            if check_mono_increase(current) and current > max_result:
                max_result = current

    print("#{} {}".format(tc, max_result))


