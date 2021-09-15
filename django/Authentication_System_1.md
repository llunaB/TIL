## Authentication System-1

- The Django Authentication System
- 쿠키와 세션
- 로그인
- 로그아웃
- 로그인 사용자에 대한 접근 제한



## The Django Authentication System

- Django 인증 시스템은 `django.contrib.auth`에 `Django contrib module`로 제공
- 필수구성은 `settings.py`에 이미 포함되어 있으며 INSTALLED_APPS 설정에 나열된 두 항목으로 구성
  1. django.contrib.auth : 인증 프레임워크와 핵심 기본모델 포함
  2. django.contrib.contenttypes : 사용자가 생성한 모델과 권한을 연결

- Django 인증 시스템은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공한다.



### Authentication & Authorization

- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정



### accounts 이름으로 앱 생성

- django 내부적으로 auth를 accounts라는 이름으로 사용하기 때문에 accounts 이름 권장



---



## 쿠키와 세션

### HTTP

- Hyper Text Tranfer Protocol
  - HTML 문서와 같은 리소스(자원, 데이터) 들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
  - 웹에서 이루어지는 모든 데이터 교환의 기초

### HTTP 특징

- 비연결지향(connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다!
- 무상태(stateless)
  - 연결을 끊는 순간 클라이언트와 서버간 통신이 끝나고 상태정보 유지되지 않는다.

```
클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재!
```

### 쿠키?

- 서버가 사용자의 웹브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트 방문시, 해당 웹사이트 서버를 통해 사용자의 컴퓨터에 설치
  - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE 데이터 형식으로 저장
  - 쿠키를 저장해두었다, 동일한 서버에 재요청시 저장된 쿠키를 함께 전송!
- 쿠키는 두 요청이 동일 브라우저에서 들어왔는지 아닌지를 판단할 때 사용
  - 상태가 없는 HTTP 프로토콜에서 상태정보를 기억시켜줌으로써 로그인 상태를 유지

```
웹페이지에 접속하면 요청한 웹페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 재요청시 요청과 함께 쿠키도 전송
```

![image-20210915225241554](image/0.png)

### 쿠키 사용목적

1. 세션 관리(Sesson Management)
   - 로그인, 아이디 자동완성, 공지 하루동안 안보기, 팝업 체크, 장바구니 등 정보관리
2. 개인화(Personalization)
   - 사용자 선호, 테마 등 설정
3. 트래킹(Tracking)
   - 사용자 행동을 기록 및 분석

### 쿠키 lifetime

1. Session cookies
   - 현재 세션이 종료되면 삭제됨
   - 브라우저가 "현재 세션(current sesison)"이 종료되는 시기를 정의
2. Persistent cookies(Permanent cookies)
   - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제

### Session in Django

- Django의 세션은 미들웨어를 통해 구현됨
- Django는 database-backed sessions 저장방식을 기본값으로 사용
- Django는  특정 session id를 포함하는 쿠키를 사용함여 각각의 브라우저와 사이트가 연결된 세션을 알아냄
  - 세션 정보의 Django_DB의 **django_session** 테이블에 저장됨
- 모든 것을 세션으로 사용하려하면 사용자가 많을 때 서버에 부하가 걸릴 수 있음



```bash
## 쿠키 vs 세션

쿠키
- 저장을 브라우저에 한다
- 단일방향

세션
- 세션 id를 쿠키로 저장
- 브라우저와 db에 모두 저장
- 양방향
```



### Authentication System in MIDDLEWARE

- SessionMiddleware
  - 요청 전반에 걸쳐 세션을 관리
- AuthenticationMiddleware
  - 세션을 사용하여 사용자를 요청과 연결



```bash
## 유저의 종류

- 로그인 유저
- 익명 유저 Anonymous
```



## 로그인

- Session 을 Create하는 로직
- `AuthenticationForm` 사용
- `login`함수 사용 
  - login (request, user) : HttpRequest 객체와 User 객체가 필요
  - 세션에 user의 ID 정보를 저장
- `get_user()` 
  - AuthenticationForm 의 인스턴스 메서드
  - user_cache는 인스턴스 생성시 None으로 할당, 유효성 검사 통과시 로그인한 사용자 객체로 할당
  - 인스턴스 유효시에만 user를 제공



### AuthenticationForm

- class AuthenticationForm(forms.Form):
- Article은 Article을 받아오지만 Authentication Form은 사용자정보를 토대로 세션아이디를 가져오는 것이므로 모델폼이 아닌 일반 폼이다.
- 사용자가 입력한 `username`,`password` 를 저장되어있는 데이터와 비교
  - 맞으면 => `session id` 를 `create`



### auth_login

- 세션아이디를 저장

![image-20210915232230171](image/1.png)

![image-20210915232322881](image/2.png)

![image-20210915232135090](image/3.png)



## 로그아웃

- Session을 Delete하는 로직
- 서버 DB와 웹에서 모든 정보 삭제
- `logout`함수 사용
  - logout(request) : HttpRequest 객체를 인자로 받고 반환 값 없음
  - 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
  - 현재 요청에 대한 session data를 DB에서 삭제, 클라이언트 쿠키에서도 sessionid 삭제
  - 다른 사람이 동일 웹브라우저를 사용하여 로그인하고, 이전 사용자의 세션데이터 접근하는 것을 방지!

![image-20210915232135090](image/4.png)





## 로그인 사용자에 대한 접근 제한

- 로그인 사용자에 대한 액세스 제한 2가지 방법

1. `.is_authenticated` attribute
2. The `login_required` decorator



#### 1. .is_authenticated

- 모든 User 인스턴스에 대해 항상 True
- 사용예
  - 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정
  - 인증된 사용자(로그인 상태)라면 로그인 로직을 수행할 수 없도록 처리
  - 인증된 사용자(로그인 상태)만 로그아웃 로직을 수행할 수 있도록 처리
  - 인증된 사용자(로그인 상태)만 게시글 작성 링크를 볼 수 있도록 처리

#### 2. login_required

- 사용자가 로그인되어있지 않으면, `settings.LOGIN_URL`에 설정된 문자열 기반 절대경로로 redirect
  - LOGIN_URL 기본값은 '/accounts/login/'
- 사용자가 로그인되어 있으면 정상적으로 view 함수를 실행
- 인증 성공시 "next"라는 쿼리 문자열 매개변수에 사용자가 redirecte 되어야하는 경로 저장
  - 예) /accounts/login/?next=/articles/create/



## 두 데코레이터로 인한 문제점과 해결

- @require_POST 작성된 함수에 @login_required를 함께 사용하는 경우 에러 발생
- 1. redirect 과정에서 POST 데이터 손실
  2. redirect는 GET 방식으로 요청됨
- 해결 : login_required 는 GET method request를 처리할 수 있는 view 함수에서만 사용해야함
