## Authentication System-2

- **회원가입**
- **회원탈퇴**
- 회원번호 수정
- 비밀번호 변경



## 회원가입

### UserCreationForm

주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

```python
# accounts/views

from django.contrib.auth.forms import UserCreationForm

def signup(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # 회원가입 후 자동으로 로그인 진행하기 UserCreationForm의 save메서드
      user = form.save()
      auth_login(request, user)
      # form.save()
      return redirect('articles:index')
  else:
    form = UserCreationForm()
  context = {
    'form' : form,
  }
  return render(request, 'accounts/signup.html', context)
```



## 회원탈퇴

회원탈퇴는 DB에서 사용자를 삭제하는 것과 같다

```python
@require_POST
def delete(request):
  if request.user.is_authenticated:
    request.user.delete()
    # 탈퇴하면서 해당 유저의 세션 데이터로 함께 지울 경우, 순서 중요!
    auth_logout(request)
  return redirect('articles:index')
```



## 회원정보 수정

### UserChangeForm

사용자의 정보 및 권한 변경을 위해 admin 인터페이스에서 사용되는 ModelForm

- update.html

```python
# accounts/views.py

from django.contrib.auth.forms import UserChangeForm

def update(request):
  if request.method == "POST":
    pass
  else:
    # user 모델로 만든 modelForm
    form = UserChangeForm(instance=request.user)
  context = {
    'form' : form,
  }
  return render(request, 'accounts/update.html', context)
```



### UsrChangeForm 주의사항

일반 사용자가 접근해서는 안될 정보까지 모두 수정이 가능해짐

따라서 UserChangeForm 을 상속받는 서브클래스 CustomUserChangeForm 를 작성해 접근 가능한 필드를 조정해야함

![image-20210925135037660](/Users/euijinpang/TIL/django/Authentication_System_2.assets/image-20210925135037660.png)



### CustomUserChangeForm 작성

- get_user_model() : 현재 프로젝트에서 활성화된 사용자 모델을 반환

```python
# accounts/forms.py

from django.contrib.auth.forms import UserchageForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name'),
```

```python
# accounts/views.py
from .forms import CustomUserChangeForm

def update(request):
  if request.method == "POST":
    form =  CustomUserChangeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      retirn redirect('articles:index')
   else:
     form = CustomUserChangeForm(instance=request.user)
   context = {
     'form' : form,
   }
   return render(request, 'accounts/update.html', context)
```



## 유저모델 클라스 필드

https://docs.djangoproject.com/en/3.2/ref/contrib/auth/

![image-20210925135320954](/Users/euijinpang/TIL/django/Authentication_System_2.assets/image-20210925135320954.png)

![image-20210925135348581](/Users/euijinpang/TIL/django/Authentication_System_2.assets/image-20210925135348581.png)

![image-20210925135355303](/Users/euijinpang/TIL/django/Authentication_System_2.assets/image-20210925135355303.png)



## 비밀번호 변경

### PasswordChangeForm

이전 비밀번호를 입력하여 비밀번호를 변경할 수 있다.

이전 비밀번호를 입력하지 않고 설정가능한 SetPasswordForm 을 상속받는 서브클래스이다

```python
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      form.save()
      # 세션무효화방지 추가
      update_settion_auth_hash(request, form.user)
      return redirect('articles:index')
  else:
    form = PasswordChangeForm(request.user)
  context = {
     'form' : form,
  }
  return render(request, 'accounts/change_password.html', context)
```

### 암호 변경 시 세션 무효화 방지

암호가 변경되어도 로그아웃 되지 않도록 새로운 password hash로 session을 업데이트

```python
update_settion_auth_hash(request, user)
```

![image-20210915233251084](image/2-5.png)

