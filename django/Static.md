최상위에 static/images 파일 생성

settings.py 수정

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # 최상위 폴더명(static)과 일치하도록
```

model 수정



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

