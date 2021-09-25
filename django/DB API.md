# DB API

Model을 만들면 장고는 객체들을 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만든다. 

## Making Queries

> Article.objects.all()
>
> 순서대로 Class Name, Manager, QuerySet API



## CRUD

### READ

DB 인스턴스 객체를 얻기 위해 쿼리문을 날리며, 레코드가 하나이면 인스턴스 객체로, 두 개 이상이면 쿼리셋으로 리턴

```bash
# 전체 article 객체 조회
Article.objects.all()
```

- detail

```python
def detail(request, pk):
  article = Article.objects.get(pk=pk)
  ...
  # 왼쪽 pk 는 DB에 저장된 레코드의 pk
  # 오른쪽 pk는 variable routing을 통해 받은 pk
```



### QuerySet API Method

- all() : 현재 쿼리셋의 복사본을 반환
- get() : 주어진 lookup 매개변수와 일치하는 객체를 반환
- .filter() : 주어진 lookup 매개변수와 일치하는 새 쿼리셋 반환

```bash
article = Article.objects.get(pk=1)
```



### 게시글 정렬 순서 변경

```python
def index(request):
  articles = Article.objects.all()[::-1] # 쿼리셋을 파이썬이 변경
  articles = Article.objects.order_by('-pk') # DB 조작으로 내림차순
```



### CREATE

방법이 여러가지인데, 초기값과 함께 인스턴스 생성하는 방법 사용

```bash
article = Article(title='second', content='django')
article.save()
# 출력
article.pk
article.title
article.content
```

- save() 메서드 : 객체를 데이터베이스에 저장
- str 메서드 : 오브젝트를 문자열로 반환



### DELETE

```bash
article = Article.objects.get(pk=1)
article.delete()
```



## Field lookups

- 조회 시 특정 검색 조건을 지정
- 쿼리셋 메서드에 대한 키워드 인수로 지정된다.
- 쿼리셋 메서드 : filter(), exclude(), get() 등

```bash
Article.objects.filter(pk__gt=2)
Article.objects.filter(content__contatins='ja')
```