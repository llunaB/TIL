import sys
sys.stdin = open('input.txt')

## 암호비트
hiddenbit = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111',
]

passkey = ''
for i in list(input()):
    hex = '0x' + i
    # 1. 16진수를 10진수로 변환
    octal_number = int(hex, 16)
    # 2. 10진수를 2진수로 변환
    binary_number = bin(octal_number)
    binary_number_no_0b = binary_number.split('b')[1]
    if len(binary_number_no_0b) % 4:
        binary_number_no_0b = '0' + binary_number_no_0b
    passkey += binary_number_no_0b

result = ''
# 6개씩 끊어서 확인하고
i = 0
while i < len(passkey)-5:
    check = passkey[i:i+6]
    # 키가 일치한다면 해당 키 다음부터 검색한다.
    if check in hiddenbit:
        result += str(hiddenbit.index(check))
        i += 6
    # 일치하는 키가 없다면 한 단계 옮겨 검색한다.
    else:
        i += 1

print(f'{result}')