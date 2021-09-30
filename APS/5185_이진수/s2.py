import sys
sys.stdin = open('input.txt')


T = int(input())

# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
# 단, 2진수의 앞자리 0도 반드시 출력한다.

for tc in range(1, T+1):
    N, h = input().split()
    # 16진수를 표현하기 위해 앞에 문자열을 추가한다.
    h = '0x' + h
    # 16진수를 10진수로 변환한다.
    octal = int(h, 16)
    # 10진수를 2진수로 변환한다.
    binary = bin(octal)
    # 2진수 맨 앞의 '0b'를 제거한다.
    binary_no_0b = binary[2:]
    # bin 내장함수는 2진수 맨 앞에 '0'을 추가한다.
    if len(binary_no_0b) % 4:
        binary_no_0b = '0'+ binary_no_0b

    print(f'#{tc} {binary_no_0b}')