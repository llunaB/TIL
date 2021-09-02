# Views and templates

### VIEWS

특정 기능을 하는, 특정 템플릿의 웹페이지 타입.

장고에서, 웹페이지와 콘텐츠들은 뷰에 의해 deliver되고, 각각의 view는 파이썬 함수(또는 메소드)형태로 나타난다. 장고는 요청받은 URL(정확히는 domain name 뒤의 url) 을 받아 view 를 결정한다.

이때, URL Pattern을 허용하는데, view로 넘기기 위해 'URLconfs' 를 사용.

- URLconf maps URL patterns to views.
- 우리가 만들 4개의 페이지

```
* Question “index” page – displays the latest few questions.
* Question “detail” page – displays a question text, with no results but with a form to vote.
* Question “results” page – displays results for a particular question.
* Vote action – handles voting for a particular choice in a particular question.
```



### 1. 인자(argument) 가 있는 views 추가

```python
# polls/views.py

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```



### 2. view와 url 연결

- `/polls/34/` 가 들어온다면, `mysite.urls` 를 거쳐 `polls/` 를 떼어버리고 `34/` 만 남는다.
- `34/` 를 'polls.urls' 로 보내는데, `<int:question_id>/` 와 매칭된다.
- 그러므로 `detail()` view 를 호출한다.

```python
# polls/urls.py

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```



### 3. 무언가 하는 view 만들기

```python
# polls/views.py

from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```

- 보여지는 화면을 고치기 위해 파이썬 코드 일일이 수정하긴 어려우니까, view 가 사용할 수 있는 template 이라는 걸 만들자!!



### 4. templates 만들기

- 해당 app 앱 디렉토리에 `templates` 폴더를 만든다.
- 기본적으로 `DjangoTemplates` 를 찾는다- `APP_DIRS` 옵션이 `TRUE` 인 경우
- 보통 설치된 앱 하위 경로의 "templates"를 찾음

- 그 `templates` 하위에 app name 폴더를 만들고 그 안에 index.html을 만든다.

```bash
 polls/templates/polls/index.html
```
