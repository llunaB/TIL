import sys
sys.stdin = open('input.txt')

cov_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(T):
    N, hexa_num = input().split()
    result = ''

    for num in hexa_num:
        tmp = ''
        # 숫자라면 정수로 변환한다.
        if num in '0123456789':
            tmp_num = int(num)
        # 알파벳이라면 해당 키에 대응되는 밸류값을 찾는다.
        else:
            # get(x) 함수는 x라는 Key에 대응되는 Value를 돌려준다.
            tmp_num = cov_dict.get(num)

        while True:
            # 빈 문자열에 10진수를 2로 나눈 나머지를 더해나간다. (2진수 만들기)
            tmp = str(tmp_num % 2) + tmp
            tmp_num = tmp_num // 2

            # 각 자리수를 4자리 이진수로 표현해야 하므로 4개가 다 차면 결과에 넣고 반복문을 종료한다.
            if len(tmp) == 4:
                result += tmp
                break

    print('#{} {}'.format(tc+1, result))