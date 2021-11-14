# Django RESTful Framework

# REST

Representational State Transfer

- API Server를 개발하기 위한 소프트웨서 설계 방법론으로 REST 원리르 따르는 시스템을 RESTful 이라고 한다.
- 정보(URI)와 행위(HTTP Method)를 통해 요청을 보내고, 응답은 JSON으로 표현된 데이터이다.

### JSON(Javascript Object Notation) 자바스크립트 객체 표기법

- 가벼운 데이터 교환 포맷으로 Javascript의 표기법을 따른 단순한 문자열.

# Restful API

- REST 원리를 따라 설계한 API
- 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성한다.

# Response

![image-20211114222044677](/Users/euijinpang/Desktop/DRF.assets/2.png)

### JsonResponse 오브젝트를 통해 Json 응답을 만든다.

### Serialization

- 데이터 구조나 객체를 저장하고 재구성할 수 있는 포맷으로 변환하는 과정

### Serializers in Django

- 쿼리셋, 모델 인스턴스 등 복잡한 데이터를 JSON, XML 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어준다.

# django 내장 HTTPResponse를 활용한 JSON 응답

```python
# django 내장 HTTPResponse를 활용한 JSON 응답
# articles/views.py

from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_json(request):
  articles = Article.objects.all()
	data = serializers.serialize('json', articles)
	return HttpResponse(data, content_type='application/json')
```

---

# django REST framework(DRF) 라이브러리를 사용한 JSON 응답

```python
# django REST framework(DRF) 라이브러리를 사용한 JSON 응답
# articles/serializers.py
# ModelSerializer는 Article 모델에 맞추어 자동으로 필드를 생성하고 serialize 해준다.

from rest_framework import serializers
from . import Article

class ArticleSerializer(serializers.Modelserializer):
  class Meta:
    model = Article
    fields = '__all__'
```

```python
# DRF의 Response()를 활용해 Serialize된 JSON 객체 응답
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view()
def article_json(request):
  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True) # 쿼리셋은 many=True 필수
  return Response(serializer.data) # json 응답
```

```python
# serialized 된 파일을 parsing

import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json/')
data = response.json() # list 타입으로 전송
pprint(data[0]) # 하나의 딕셔너리 객체 출력
```

# Django REST Framework(DRF)

- Web API 구축을 위한 라이브러리
- https://www.django-rest-framework.org/

# Single Model

- 단일 모델 조작하기
  - 쿼리셋일때는 `many=True` 필수, 단일 인스턴스인 경우는 불필요.

```python
# DRF의 Response()를 활용해 Serialize된 JSON 객체 응답
# articles/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

# serializer = ArticleSerializer()
@api_view()
def article_json(request):
  article = Article.objects.get(pk=1)
  serializer = ArticleSerializer(article)
  return Response(serializer.data) # json 응답
```



# Build RESTful API

두 개의 url로 5개의 API를 만들 수 있다.

1. articles/    전체 글을 조회하고(GET) 새 글을 작성(POST) 할 수 있다.
2. articles/1/  게시글을 조회하고(GET) 수정하고(PUT) 삭제(DELETE)할 수 있다.

![image-20211115004820357](/Users/euijinpang/Desktop/DRF.assets/image-20211115004820357.png)

```python
# urls.py
urlpatterns = [
  path('articles/', views.article_list),
  path('articles/<int:article_pk>', views.article_detail),
]
```

```python
@api_view(['GET', 'POST']) # api_view decorator 필수

def article_list(request):
  # 전체 글 조회하기
  if request.method === 'GET':
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
   # 새 글 작성하기 (성공시 201 Created)
  elif request.method == 'POST':
      serializer = ArticleSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True): # raise_exception으로 400 자동 반환
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # 유효성 검사 오류시
  # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
```

```python
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
	# 게시글 조회하기 (성공시 204 No Content)
  if request.method == 'GET':
      serializer = ArticleSerializer(article)
      return Response(serializer.data)
	# 게시글 삭제하기 (성공시 204 No Content)
  elif request.method == 'DELETE':
    	article.delete()
      data = {
        'delete': f'데이터 {article_pk} 번이 삭제되었습니다.'
      }
      return Response(data, status=status.HTTP_204_NO_CONTENT)
  # 게시글 수정하기
  elif request.method == 'PUT':
    	serializer = ArticleSerializer(article, data=request.data)
      if serializer.is_valid(raise_exception=True):
        	serializer.save()
          return Response(serializer.data)
```