# 소요시간을 모두 분으로 바꾼다.
# 시간과 분이 모두 있는 경우
    # '시간' 앞의 문자열을 숫자로 변환 후 60을 곱한다.
    # '분' 앞의 문자열을 숫자로 변환
    # 두 결과를 더한다.
# 시간만 있는 경우
    # '시간' 앞의 문자열을 숫자로 변환 후 60을 곱한다.
# 분만 있는 경우
    # '분' 앞의 문자열을 숫자로 변환

timetake = ["1시간 30분", "2시간", "30분"]

for time in timetake:
    words = list(time) # ['1', '시', '간', ' ', '3', '0', '분']
    if '시' in words and '분' in words:
        h_idx = words.index('시')
        m_idx = words.index('분')
        hour_lst = words[:h_idx]
        min_lst = words[h_idx+3:m_idx]

        if len(hour_lst) == 1:
            hour = int(hour_lst[0])
        else:
            hour = int(hour_lst[0]) * 10 + int(hour_lst[1])

        if len(min_lst) == 1:
            min = int(min_lst[0])
        else:
            min = int(min_lst[0]) * 10 + int(min_lst[1])

        result = hour * 60 + min

    elif '시' in words and '분' not in words:
        h_idx = words.index('시')
        hour_lst = words[:h_idx]
        if len(hour_lst) == 1:
            hour = int(hour_lst[0])
        else:
            hour = int(hour_lst[0]) * 10 + int(hour_lst[1])
        result = hour * 60

    else:
        m_idx = words.index('분')
        min_lst = words[:m_idx]
        if len(min_lst) == 1:
            min = int(min_lst[0])
        else:
            min = int(min_lst[0]) * 10 + int(min_lst[1])
        result = min
    
    print(result)