# Form & ModelForm

## Form

### 장고의 form

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

## Form Class

form 내의 field, field 배치, 디스플레이, label, 초기값, 유효하지 않은 필드에 대한 에러메세지 결정

## Form 선언

forms 라이브러리에서 파생된 Form 클래스를 상속받는다.

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField(max_length=100)
```

## Form 사용

```python
# articles/views.py
from .forms import ArticleForm

def new(request):
  form = ArticleForm()
  context = {
    'form' : form,
  }
  return render(request, 'articles/new.html', context)
```

```python
# new.html
<form...>
	{{ form.as_p }}
  <input>
</form>
```



---



## ModelForm

Article 모델이 있고, 사용자가 게시글을 제출할 수 있는 양식을 만들고 싶은 경우

## ModelForm Class

Model 을 통해 Form Class를 만들 수 있는 헬퍼

## ModelForm 선언

forms 라이브러리에서 파생된 ModelForm 클래스를 상속받는다.

정의한 클래스 안에 메타클래스를 선언하고, 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 메타 클래스에 지정한다.

```python
# articles/forms.py
from django import forms
from .models import Article => 모델 가져오기!!

# 모델폼
class ArticleForm(forms.ModelForm):
  # 위젯 적용
  title = forms.CharField(
  	label='제목',
    widget=forms.TextInput(
    	attrs={
        # 부트스트랩 Form 의 핵심 class 'form-control'
        'class' : 'my-title form-control',
        'placeholder' : 'Enter the title',
      }
    ),
  )
  class Meta:
    model = Article
    fields = '__all__'
    exclude = ('title',)

# 참고) 일반 폼
# articles/forms.py
class ArticleForm(forms.Form):
  title = forms.CharField(max_length=10)
  content = forms.CharField(max_length=100)
  
# 참고) 모델선언
# articles/models.py
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```

```python
# articles/views.py

def create(request):
  if request.method == "POST":
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
    	return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm()
  context = {
    'form' : form,
  }
  return render(request, 'articles/create.html', context)
```



## save() method

- ModelForm 의 하위 클래스는 기존 모델 인스턴스를 **키워드 인자** `instance`로 받아들일 수 있다. 
- `instance`가 제공되면 `save()`는 해당 인스턴스를 업데이트한다. `update`
- 미제공시 `save()`는 지정된 모델의 새 인스턴스를 만든다. `create`

```python
form = AritlceForm(request.POST)
# CREATE
new_article = f.save()
# UPDATE
article = Article.objects.get(pk=1)
form = ArticleForm(request.POST, instance=article) 
# 기존 모델(ArticleForm은 기존 모델(article) 인스턴스를 키워드 인자 instance로 받아들임)
form.save()
```



## Form & ModelForm

- Form
  - 어떤 model에 저장해야 하는지 알 수 없으므로 유효성 검사 후 `cleaned_data` 딕셔리를 생성한다.
    - `cleaned_data` 딕셔너리에서 데이터를 가져온 후  `.save()`를 호출해야 함.
    - model 에 연관되지 않은 데이터를 받을 때 사용한다.

- ModelForm
  - 장고가 해당 model 양식에 필요한 대부분의 정보를 이미 정의하고 있다.
  - 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 `.save()`호출이 가능하다.



## 뷰함수 구조변경(분기처리) 연습

### create view 함수 구조 변경

```python
# 2. create
# 빈 종이를 보여주던 new.html 과 new 함수는 사라진다. form이 대체한다.
def create(request):
    # 5. create 경로로 요청이 들어옴(POST) => 잘못된 데이터를 담아서 저장해달라고 요청
    # 10. create 경로로 요청이 들어옴(POST) => 올바른 데이터를 담아서 저장해달라고 요청

        # 6. ArticleForm을 인스턴스화한다. (사용자가 입력한 정보를 담아서) => 데이터가 입력된 종이를 생성한다.
        # 11. ArticleForm을 인스턴스화한다. (사용자가 입력한 정보를 담아서) => 데이터가 입력된 종이를 생성한다.

        # 7. 데이터가 유효한지 검증한다. (잘못된 데이터를 넣었기 때문에 실패)
        # 12. 데이터가 유효한지 검증한다. (올바른 데이터를 넣었기 때문에 성공)

            # 13. 데이터를 저장한다.
            # 14. index로 리다이렉트한다.

    # 1. create 경로로 요청이 들어옴(GET) => 빈종이를 달라고 하는 요청
        # 2. ArticleForm을 인스턴스화한다. => 빈 종이를 생성한다.

    # 3. 사용자에게 빈 종이를 주기 위해 context에 담는다.
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 담는다.

    # 4. 사용자에게 빈 종이를 넘겨준다.
    # 9. 사용자에게 올바른 데이터가 있는 종이를 넘겨준다.
```

### update view 함수 구조 변경 

```python
# 3. update
# 기존 정보를 보여주는 종이였던 edit.html과 edit 함수는 사라진다. form이 대체한다.
def update(request, pk):
    # 0. 기존 정보를 하나 가져온다.

    # 5. update 요청이 들어옴(POST) => 잘못된 데이터를 담아서 수정해달라고 요청
    # 10. update 요청이 들어옴(POST) => 올바른 데이터를 담아서 수정해달라고 요청

        # 6. ArticleForm을 인스턴스화한다. (사용자가 수정한 정보 + 기존정보)
        # 11. ArticleForm을 인스턴스화한다. (사용자가 수정한 정보 + 기존정보)

        # 7. 데이터가 유효한지 검증한다. (잘못된 정보가 들어옴)
        # 12. 데이터가 유효한지 검증한다. (올바른 정보가 들어옴)

            # 13. 데이터를 수정한다.
            # 14. index로 리다이렉트 시켜준다.


    # 1. update 요청이 들어옴(GET) => 기존의 정보를 담은 종이를 요청

        # 2. 기존의 정보를 담은 종이를 생성

    # 3. 사용자에게 보여주기 위해 context에 저장한다.
    # 8. 유효한 데이터만 들어있는 종이를 다시 돌려주기 위해 context에 저장

    # 4. 사용자에게 종이를 보낸다.
    # 9. 사용자에게 올바른 데이터가 있는 종이를 넘겨준다.
```



## MODELFORM 분기처리 함수 질문

##### ![image-20210908002951045](/Users/euijinpang/TIL/django/Form & ModelForm.assets/image-20210908002951045.png)

1. context 가 if else 문과 동일 레벨이어야 "form.is_valid()" 유효성 검사를 통과하지 못한 경우, 사용자가 입력한 올바른 부분까지 데이터를 담아, 그것을 다시 돌려줄 수 있다.
2. http method에는 POST, GET 방식 외에도 PUT, PATCH 등 다양한 방식이 존재하는데, POST 만 데이터베이스를 건드리기 때문에 POST 외의 방식을 예외처리 해주는 것이 효율적이다.
