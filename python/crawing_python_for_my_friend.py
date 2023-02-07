#친구를 위해 만든 간단한 파이썬 코드 중 일부
import requests
from bs4 import BeautifulSoup
import datetime

i = 2
try:
    for date in dates:
        for num in numbers:
            day = "2023" + str(date) + "500" + str(num)
            print(day)
            # day = "20230203500361"

            if day[:7] > "".join(str(datetime.date.today()).split('-')):
                print('이제끝~~~~~~')
                break
            
            BASE_URL = f"https://.../article/{day}"
            resp = requests.get(BASE_URL, params=params, headers=headers)
            if resp:
                t, d = get_title_date(resp)
                ws[f'A{i}'] = t
                ws[f'B{i}'] = d

                print('진행중' + str(i-1) + '번째~~~~~~~~~~~~~~~~~~~~~~~~저장!!!!!!!')

            else:
                print('넘어갑니다')
except:
    print('예외발생')