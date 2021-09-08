# Static files

> 개발자가 사용하는 리소스와, 사용자로부터 받아온 리소스를 관리한다.



### Static file 

- 응답시 서버단에서 별도의 처리 없이 그대로 보여주면 되는 정적 파일



### 구성 4단계

1. `django.contrib.staticfiles 가 INSTALLED_APPS` 에 포함되어있는지 확인한다.

2. settings.py 에서 STATIC_URL을 정의한다.

```python
STATIC_URL = '/static/' # 기본 적용
STATICFILES_DIRS = [BASE_DIR / 'static'] # 최상위 폴더명(static)과 일치하도록
```

3. 템플릿에서 static template tag를 사용하여 지정된 상대경로에 대한 URL을 빌드한다.

- 기본 경로는 앞의 my_app/static 이 생략된 그 이후의 경로로 작성한다.

```python
{% load static %}
<img src="{% static 'my_app/example.jpg %'}" alt="my image">
```

4. 앱의 static 폴더에 정적 파일을 저장한다.

- my_app/static/my_app/example.jpg



### Django template tag

- load : 사용자 정의 템플릿 태그세트를 로드한다.

```python
{% load static %}
```

- static : STATIC_ROOT 에 저장된 정적 파일에 연결한다.

```python
<img src="{% static 'my_app/example.jpg %'}" alt="my image">
```



### STATICFILES_APP

##### STATIC_ROOT

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- settings.py의 DEBUG 값이 True 로 설정시 작동하지 않음
  - 직접 작성하지 않으면 장고프로젝트에서는 셋팅에 작성되어 있지 않음
- 추후 배포시 사용

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'

$ python manage.py collectstatic
```



##### STATIC_URL

- STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL
  - 기본 경로(app/static/경로) 및 STATICFILES_DIRS에 정의된 추가 경로를 선택
- 실제 파일이나 디렉토리가 아니며, URL로만 존재한다.



##### STATICFILES_DIRS

- 기본경로 외 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성



### 정적파일 사용하기 - 기본경로

- 정적 파일 경로 : app/static/app
- 템플릿에서 경로 참조 : app/static 까지가 기본 경로이므로 그 이후를 써준다.

```python
{% load static %}
...
<img src="{% static 'app/example.jpg'%}"alt="img">
```

- 이미지 주소는 `/static/app/example.jpg `이며, 이 요청주소를 static tag가 만들어주는 것이다.

> http:// ...8000/static/app/example.jpg



### 정적파일 사용하기 - 추가경로

- 정적 파일 위치: 프로젝트 폴더와 동일선상에서 static/images
- 추가 경로 작성

```python
STATICFILES_DIRS = [
  BASE_DIR / 'static'
]
```

- 템플릿에서 경로 참조 - base.html

```python
{% load static %}
...
<img src="{% static 'images/example.jpg'%}"alt="img">
```



---

(미정리)





form.html

글자 외의 다른 파일을 받는 서비스일 경우

다른 파일을 넣을 예정이다 => 인코딩 방식을 바꿔주는 코드를 넣어야

```django
<form action="" method="POST" class="col-4 offset-4" enctype="multipart/form-data">
```



![image-20210908131033691](/Users/euijinpang/Library/Application Support/typora-user-images/image-20210908131033691.png)

### create

view.py 를 보면, 장고가 이미지를 받지 못함

request.POST 가 아닌 request.FILES에 있기 때문



저장하면

최상위에 image 폴더가 생성



장고가 주는 이미지가 다시 크롬으로 갈때 경로를 설정

```python
# settings.py

MEDIA_URL = '/media/' # url 경로의 이름
MEDIA_ROOT =  BASE_DIR / 'media' # 실제로 파일이 저장되는 공간
```



urls.py 에 경로 잡아주기

![image-20210908133039734](/Users/euijinpang/Library/Application Support/typora-user-images/image-20210908133039734.png)

Index.html

![image-20210908133141195](/Users/euijinpang/Library/Application Support/typora-user-images/image-20210908133141195.png)

media root 를 설정했기 때문에 최상위 미디어 안에 사진이 저장된다.





큰 이미지의 경우 => 불러오는데도 데이터를 쓴다.

크게 받아서 작게 만드는게 아닌, 원본 데이터를 작게 하는 방법

