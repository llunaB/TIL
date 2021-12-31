# 소요시간을 모두 분으로 바꾼다.

time = input()
# 1. 분만 있는 경우 "30분" => 30
# 2. 시간만 있는 경우 "2시간" => 120
# 3. 분과 시간이 모두 있는 경우 "1시간 30분" => 90

if time.find('시간') == -1:
    result = int(time.split('분')[0])        # ['30', '']

elif time.find('분') == -1:
    result = int(time.split('시간')[0]) * 60  # ['2', '']

else:
    sub = time.split('시간')                  # ['1', '30분']
    result = int(sub[0]) * 60 + int(sub[1].split('분')[0])

print(result)