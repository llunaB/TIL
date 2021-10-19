# Model Relationship

## Foreign Key

- Comment CREATE
- Comment READ
- Comment DELETE

## Customizing authentication in Django

- Substituting a custom User model
- Custom user & Built-in auth forms



# Foreign Key

- 참조하는 테이블의 키로, 참조되는 측 테이블의 기본키(Primary Key)를 가리킨다.

### 댓글(Comment) N - -((참조))- ->1 게시물(Article)

- 참조하는 모델(Comment)에서 외래 키는 참조되는 측 모델(Article)의 기본 키(Primary Key)를 가리킨다.
- 즉, 댓글 2번과 3번의 foreign key가 1이면 이는 1번 게시글의 댓글들이라는 뜻!
- 이 때, 참조하는 부모테이블 값은 유일한 값이어 한다. (참조 무결성)

### N:1 관계

- Article 앱 내에 comment 모델 정의
- 2개의 위치인자 필수
  - 참조하는 model class
  - on_delete 옵션 : 데이터 무결성 설정
- 추가 선택인자 'related_name'
  - 역참조시 사용할 이름을 변경 : `article.comment_set` 은 더 이상 사용할 수 없고, `article.comments` 로 대체됨.

```python
# comment 모델을 정의하였으므로 articles_comment 테이블이 생성된다.

class Comment(modes.Model):
  # CASCADE : 외래키가 참조하는 객체가 사라지면 외래 키를 가진 객체도 삭제한다.
  # articles_comment 테이블에 외래 키 컬럼 article_id 가 생성된다. (필드명_id)
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  
  
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.content
```

### articles_comment 테이블, article_id 컬럼(외래키)이 생성

# N:1 관계

### 역참조 : article.comment_set

- Comment(N) <- Article(1)
- `article.comment_set manager`
- article 의 모든 댓글 조회하기

```django
article.comment_set.all()
for comment in comments: ...
```



### 참조 : article.comment

- Comment(N) -> Article(1)
- `comment.article`
- comment의 입장에서 참조하는 게시글 조회하기

```django
comment = Comment.objects.get(pk=1)
comment.article
```



# Comment CREATE

댓글을 작성해보자!

1. 아까 만든 모델로부터 모델폼을 만들자.

```python
# articles/forms.py
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		# fields = '__all__'
    exclude = ('article', )
```

2. articles/views.py 에서 detail 뷰함수에 comment_form 을 추가하자.

```python
def comments_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

- save instace : 커밋하지 않는다. 생성만 하고 새 인스턴스를 저장하지는 않기 때문에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용한다.

2. articles/urls.py 로 comments_create 경로를 추가하자.

3. articles/detail.html 에서 comment_form 을 출력하자.

   이 때, 외래키 필드(article) 를 제외하고 출력하자.



# Comment READ

1. 특정 article에 있는 모든 댓글을 가져와서 추가하자.

```python
# articles/views.py

from .models import Article, Comment

def detail(request, pk):
  article = ...
  comment_form = CommentForm()
  comments = article.comment_set.all()
  context = {
    'article' : article,
    'comment_form' : comment_form,
    'comments' : comments,
  }
  return render(request, 'articles/detail.html', context)
```



2. detail 페이지에서 출력하자

```python
<ul>
	{% for comment in comments %}
  	 <li>{{ comment.content }}</li>
  {% endfor %}
</ul>
```



# Comment DELETE

1. url을 만들자.

```python
# articles/urls.py

app_name = 'article'
urlpatterns = [
path(
	'<int:article_pk>/comments/<int:comment_pk>/delete/', veiws.comments_delete, name='comments_delete'
),
]
```

   

2. comments_delete 함수를 만든다.

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```



2. detail 페이지에 삭제 버튼을 만들자.

```python
# articles/detail.html

<form action="{% url 'articles:comments_delete' article.pk comment.pk %}">
		{% csrf_token %}
  	<input type="submit" value="DELETE">
</form>
```



# Customizing authentication in Django

# Substituting a custom User model

- 기본 사용자 모델이 아닌 커스텀 유저모델 설정을 권장!
- 단, 프로젝트의 migrations 전에 작업을 마칠 것!

### AUTH_USER_MODEL

기본값 : auth.User

### Custom User 모델 정의하기

1. AbstractUser를 상속받아 새로운 User 모델 작성

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  	pass
```

2. 기존 AUTH_USER_MODEL 변경 : auth.User => accounts.User

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

3. admin 에 커스텀 유저모델 등록

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

4. 프로젝트 중간에 진행시 DB 초기화 후 마이그레이션 진행
   - db.sqlite3 삭제
   - migrations 내 숫자 파일 삭제

# Custom user & Built-in auth form

회원가입과 정보수정에서 에러가 발생하는데, 기존의 내장 User모델을 사용하고 있기 때문으로, 커스텀 User 모델로 대체해야 한다.

- UserCreationForm => 상속 =>  CustomUserCreationForm
- UserChangeForm => 상속 => CustomUserChangeForm

1. accounts/forms.py 수정
2. accounts/views.py 수정



![image-20211019090835408](/Users/euijinpang/TIL/relation.assets/image-20211019090835408.png)

위치만 다르고 똑같은 기능!!



Group-user 연결되어있으므로 설정을 바꿔주고 마이그레이션

![image-20211019091652716](/Users/euijinpang/TIL/relation.assets/image-20211019091652716.png)

article, user 연결

![image-20211019092513972](/Users/euijinpang/TIL/relation.assets/image-20211019092513972.png)

이건 비권장

오른쪽의 user 클래스는 여기저기 쓰이므로 변수화하는게 좋다

![image-20211019092740906](/Users/euijinpang/TIL/relation.assets/image-20211019092740906.png)

![image-20211019092755147](/Users/euijinpang/TIL/relation.assets/image-20211019092755147.png)



![image-20211019092908796](/Users/euijinpang/TIL/relation.assets/image-20211019092908796.png)

1번 유저를 기본유저로 설정

이후 다시 마이그레잍 



delete 문제발생

![image-20211019114453366](/Users/euijinpang/TIL/relation.assets/image-20211019114453366.png)



# 과정

1. articles 의 models에 유저 만듦.

   ​    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

2. 마이그레이션.

3. 1번유저 디폴트로 잡음.


