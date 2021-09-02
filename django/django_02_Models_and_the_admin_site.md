# DB and MODELS

### 1. DB SETUP

##### default

- python 내장 `SQLite` 사용 (유저가입 없이도 사용가능)
- `<projectname>/settings.py`  내의 **"INSTALLED_APPS"** 에 필요한 데이터베이스를 생성

```python
python manage.py migrate
```



### 2. model class 제작

- model : a database layout, with additional metadata
- **Question** 및 **Choice** model class 제작 (python `classes` 형태)

```python
# polls/modes.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

```
여기에서 각 모델은 django.db.models.Model를 하위 클래스로 가지는 클래스입니다.

question_text, pub_date => database field
각 모델에는 여러 클래스 변수(class variables)가 있으며 각각은 모델의 database field를 나타냅니다.

각 필드는 Field class의 instances로 표시된다. (예: 문자 필드의 경우 CharField, 날짜/시간의 경우 DateTimeField). 이것은 Django에게 각 field가 어떤 유형의 data를 보유하는지 알려줍니다.

각 Field instance의 이름(question_text 또는 pub_date)은 machine-friendly format 이름입니다. Python 코드에서 이 값을 사용하고 데이터베이스는 이 값을 column name 으로 사용합니다.

일부 Field class에는 필수 인수(required arguments)가 있습니다. 예를 들어 CharField는 max_length를 지정해야 합니다. 이것은 데이터베이스 스키마뿐만 아니라 곧 보게 될 유효성 검사(validation)서도 사용됩니다.

Field는 또한 다양한 선택적 인수(optional arguments)를 가질 수 있습니다. 이 경우 투표의 기본값을 0으로 설정했습니다.

마지막으로 ForeignKey를 사용하여 관계를 정의합니다. 이는 Django에게 각 Choice가 단일 질문과 관련되어 있음을 알려줍니다. Django는 다대일, 다대다, 일대일과 같은 모든 공통 데이터베이스 관계를 지원합니다.
```



### 3. model 실행

#### 3-1. 앱 등록

- The `PollsConfig` class is in the `polls/apps.py` file, so its dotted path is `'polls.apps.PollsConfig'`. 
- Edit the `mysite/settings.py` file and add that dotted path to the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-INSTALLED_APPS) setting.

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



#### 3-2. cmd 입력

- By running `makemigrations`, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a *migration*.

```python
python manage.py makemigrations polls
```

```bash
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```



#### 추가 : SQL 확인하기

```bash
python manage.py sqlmigrate polls 0001
```



#### 3-3. migrate 실행하기

- model 의 변화를 database에 반영

```bash
python manage.py migrate
```



### 결론 : 3steps!! 

![image-20210902211712147](images/image-20210902211712147.png)



### 5. API 활용하기

#### **5-1. model class 사용을 위해 익스텐션 설치, shell plus 사용**

장고 익스텐션 설치 및 실행

```bash
pip install django-extensions (이후 settings.py 에 app 'django_extensions' 등록)
```

```bash
python manage.py shell_plus
```

추가 (비주얼보정용)

```python
pip install ipython
```



#### 5-2. shell 써보기

```bash
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```



#### 5-3. App 내의 Model 수정해서 보기좋게 만들기

- `__str__` 은 편의성을 위해 넣어주는것이 중요하다!

```python
# polls/models.py

from django.db import models

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
```



#### 5-4. custom method 넣기

```python
# polls/models.py

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

- Note the addition of `import datetime` and `from django.utils import timezone`, to reference Python’s standard [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime) module and Django’s time-zone-related utilities in [`django.utils.timezone`](https://docs.djangoproject.com/en/3.2/ref/utils/#module-django.utils.timezone), respectively.
- If you aren’t familiar with time zone handling in Python, you can learn more in the [time zone support docs](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/).



- `exit` 으로 빠져나가기



# Django Admin

### admin user 생성

생성

```bash
$ python manage.py createsuperuser
```

유저네임 생성 (보통 admin)

```bash
Username: admin
```

이메일(선택)

```bash
Email address: admin@example.com
```

비밀번호 입력

```bash
Password: **********
Password (again): *********
Superuser created successfully.
```



### 서버 실행

```bash
$ python manage.py runserver
```

` http://127.0.0.1:8000/admin/ ` 주소로 접속



### 어드민단에서 앱 관리

- 앱 내의 admin.py 파일에서 model class를 등록해야한다

```python
# polls/admin.py

from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
