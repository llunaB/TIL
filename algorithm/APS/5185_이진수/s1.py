import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, hex = input().split() # hex = 16진수
    N = int(N) # N = 자리수

    ans = ''
    # 0. 16진수 표현으로 변환
    hex = '0x' + hex
    # 1. 16진수를 10진수로 변환
    octal_number = int(hex, 16)
    # 2. 10진수를 2진수로 변환
    binary_number_no_0b = bin(octal_number)[2:]
    ans += binary_number_no_0b
    # 길이가 4의 배수가 아닐경우 0 추가한다.
    if len(ans) % 4:
        ans = '0' + ans

    print('#{} {}'.format(tc+1, ans))