
## 1. 문자열 메서드
"be proud".upper()
"BE PROUD".lower()

"오늘 날씨는 흐림입니다.".replace("흐림", "맑음")
# >>> 오늘 날씨는 맑음입니다.

'Hello World'.find("World")
# >>> 6

'cat is my cat'.count("cat")
# >>> 2

'나이키신발 265'.split()
# >>> ['나이키신발', '265']
'나이키신발:265'.split(':')
# >>> ['나이키신발', '265']
''.join()

'     hi'.lstrip()
# >>> 'hi'
'     hi'.rstrip()
# >>> 'hi'
'     hi     '.strip()
# >>> 'hi'

## 2. 문자열 포매팅
# format method
'Hello{0}{1}{2}'.format('hi', 'my', 'friend')
# f-string
name1 = 'hi'
name2 = 'my'
name3 = 'friend'
f'Hello{name1} {name2} {name3}'