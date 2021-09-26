# Handlign HTTP requests

## Django에서 HTTP 요청을 처리하는 방법

1. Django shortcut functions
2. View decorators



## Django shortcut functions

django.shortcuts 패키지가 여러 함수와 클래스를 제공

- render()
- redirect()
- get_object_or_404()
- get_list_or_404()



## get_object_or_404()

모델 manager object에서 get()을 호출하지만, 해당 객체가 없을경우 `DoesNotExist`예외 대신 `HTTP 404` 를 발생시킨다.

get() 메서드의 경우 조건에 맞는 데이터가 없을 경우 에러를 발생시킨다. (500)

```python
# view.py

from django.shortcuts import get_object_or_404

def detail(request, pk):
  article = get_object_or_404(Article, pk=pk)
```



## Django View Decorators

- 뷰 함수의 기능확장을 위해 함수에 적용가능한 데코레이터를 제공

### Allowed HTTP methods

요청 메서드에 따라 view함수에 대한 액세스를 제한

- require_http_methods(['GET', 'POST'])
- require_POST()

```python
# views.py
from django.views.decorators.http import require_http_methods, require_POST

@require_http_methods(['GET', 'POST'])
def ...

@require_POST
def ...
```


