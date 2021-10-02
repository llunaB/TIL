# 1. 위치 매개변수
# 가장 기본적인 매개변수 

def my_func(a, b):
    print(a, b)

my_func(2, 3)

# 2. 기본 매개변수
# 매개변수의 기본값을 지정할 수 있다.
# 첫번째 매개변수로는 title, 두번째에 아무것도 들어오지 않으면 기본값을 주겠다.

def post_info(title, content='내용없음'):
    print('제목 :', title)
    print('내용 :', content)

post_info('출석합니다!')

# 3. 키워드 매개변수
# 함수 호출시에 키워드를 붙여서 호출
# 매개변수의 순서를 지키지 않아도 됩니다.

def post_info(title, content):
    print('제목 :', title)
    print('내용 :', content)

post_info(content='없어요', title='남자친구 만드는 법')

# 4. 위치 가변 매개변수: 튜플 형태로 출력된다.
# args = ('apple', 'orange', 'mango', 'grape')

def print_fruits(*args):
    print(args)
    for arg in args:
        print(arg)

print_fruits('apple', 'orange', 'mango', 'grape')

# 5. 키워드 가변 매개변수: 딕셔너리 형태로 출력된다.
# kwargs = {'name': '날씨가', 'content': '좋다.'}

def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

comment_info(name='날씨가', content='좋다.')

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변
def post_info(*tags, title, content):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')

# TypeError 발생
post_info('#파이썬', '#함수', '파이썬 함수 정리', '다양한 매개변수를 정리합니다.')
# 해결방법 1. 순서를 맞춘다.
post_info('파이썬 함수 정리', '다양한 매개변수를 정리합니다.', '#파이썬', '#함수')
# 해결방법 2. 키워드 인자로 설정한다.
post_info('#파이썬', '#함수', title='파이썬 함수 정리', content='다양한 매개변수를 정리')