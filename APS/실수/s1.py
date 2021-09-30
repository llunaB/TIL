## 암호비트
hiddenbit = {
    '0' : '001101',
    '1' : '010011',
    '2' : '111011',
    '3' : '110001',
    '4' : '100011',
    '5' : '110111',
    '6' : '001011',
    '7' : '111101',
    '8' : '011001',
    '9' : '101111',
}

import sys
sys.stdin = open('input.txt')

passkey = ''
for i in list(input()):
    hex = '0x0' + i
    # 1. 16진수를 10진수로 변환
    octal_number = int(hex, 16)
    # 2. 10진수를 2진수로 변환 
    binary_number = bin(octal_number) # 앞에 0 붙이기!!
    binary_number_no_0b = binary_number.split('b')[1]
    passkey += binary_number_no_0b

result = []
# huddenbit 암호비트 딕셔너리 및 passkey 탐색, 일치시 암호반환

passkey = '0000001001101001111110101100100110100000'
## 수정:
i = 0
while i < len(passkey)-5:
    check = passkey[i:i+6]
    for items in hiddenbit.items():
        if items[1] == check:
            result.append(items[0])
            i += 6
    else:
        i += 1

print(f'{result}')

# passkey = 0101101001111110101100100110100
# result = 01178