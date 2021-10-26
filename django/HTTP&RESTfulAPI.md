# HTTP

- 요청(request) : 클라이언트에 의해 전송되는 메세지
- 응답(response) : 서버에서 응답으로 전송되는 메세지



### 기본 특성

- stateless
- connectionless



- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함

![image-20211025091515166](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025091515166.png)

# HTTP request methods : 요청시

- GET, POST, PUT DELETE 등



# HTTP response status codes : 응답시

![image-20211025091623378](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025091623378.png)

- 특정 HTTP 요청이 성공적으로 완료됐는지 여부
- 5개의 그룹

# 웹에서 리소스 식별 URI(Uniform Resource Identifier)

### URL (Uniform Resource Locator) 

- 통합 자원 위치
- 네트워크 상에 자원이 어디에 있는지 알려주는 약속

### URN (Uniform Resource Name)

- 통합 자원 이름
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름

### URI (Uniform Resource Indicator)

- URL과 URN을 포함하는 개념.
- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소

![image-20211025092343427](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092343427.png)

![image-20211025092353514](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092353514.png)

![image-20211025092457678](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092457678.png)

![image-20211025092542427](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092542427.png)

![image-20211025092642397](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092642397.png)

![image-20211025092746609](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025092746609.png)



# Restful API

![image-20211025093018988](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093018988.png)

![image-20211025093242930](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093242930.png)

![image-20211025093510624](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093510624.png)

![image-20211025093619888](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093619888.png)

![image-20211025093809526](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093809526.png)

![image-20211025093935706](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025093935706.png)



# Resonse

![image-20211025100728160](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025100728160.png)

![image-20211025104210943](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025104210943.png)

![image-20211025105327249](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025105327249.png)

![image-20211025110303300](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025110303300.png)

![image-20211025110846125](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025110846125.png)

![image-20211025124642333](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025124642333.png)

https://www.django-rest-framework.org/

# view

### cbv

- function-based view

### fbv

- function-based view

![image-20211025125549763](/Users/euijinpang/TIL/django/HTTP&RESTfulAPI.assets/image-20211025125549763.png)

​		movies -> GET, POST

​		put, delete -> /movies/:id:

장고는 GET, POST 만 사용하므로 PUT, DELETE 를 위해서 update, delete 사용했다. 

그러나 Django Restful Framkework 사용하면 모두 가능.

