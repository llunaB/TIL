# Django ORM

- SQL 문으로 확인하기

```
data = Model.objects.get(id=1)
print(data.query)
```

- 실행

```
python manage.py shell_plus
```

- 모델 불러오기

```
from <app>.models import <Model>
```

- 모든 데이터 조회하기

```
Model.objects.all()
```

- 데이터 생성하기

```
Model.objects.create(title='', price=1000)
```

- 모든 데이터 보기

```
Model.objects.all().values()
```

- 특정 필드만 보기

```
Model.objects.all().values('title')
```

- 정렬하기

```
Model.objects.order_by('title')
```

- 데이터 갯수 세기

```
nums = Model.objects.count()
```

- 특정 조건을 제외한 데이터 조회

```
data = Model.objects.exclude(title='love')
```

- 하나의 데이터 조회하기

```
Model.objects.get(title__contains="사랑")
```

- 제목에 '사랑'이 들어간 여러개의 데이터 조회하기

```
Model.objects.filter(title__contains="사랑")
```

- 평점 1부터 5까지 사이의 여러개의 데이터 조회하기

```
Model.objects.filter(rating__range=(1, 5))
```

- 평점 4부터 5까지 받았으면서 해당 유저가 리뷰를 남기지 않은 영화를 조회하기

```
Model.objects.filter(rating__range=(4,5)).exclude(user=user)
```

- 감독 이름이 봉준호인 영화 모두 조회하기

```
data = Movie.objects.filter(director__iexact='봉준호') # 대소문자 미구분
data = Movie.objects.filter(director__exact='봉준호') # 대소문자 구분
```

- 영화의 제목에 love 가 포함된 데이터 조회하기

```
data = Movie.objects.filter(title__contains='love') # 대소문자 구분
data = Movie.objects.filter(title__icontains='love') # 대소문자 미구분
```

- 영화 평점이 4점 이상인 데이터 조회

```
data = Movie.objects.filter(rank__gte=4) # gte= 이상 lte 이하 gt 초과 lt 미만
```

- 영화 장르가 1,2,3 중 하나인 데이터 조회

```
data = Movie.objects.filter(genre__in=[1,2,3])
```

- 빠져나가기

```
exit()
```

- 데이터 수정하기

```
data = Model.objects.get(id=1)
data.title = "제목변경"
data.save()
```

- 데이터 삭제하기

```
data = Model.objects.get(id=3)
data.delete()
```

