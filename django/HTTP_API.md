# HTTP

HyperText Transfer Protocal , 웹 상에서 컨텐츠를 전송하기 위한 약속

- 요청(request) : 클라이언트에 의해 전송되는 메세지
- 응답(response) : 서버에서 응답으로 전송되는 메세지



### 기본 특성

- stateless 상태가 없다.
- connectionless 연결성이 없다.

- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함

# HTTP request methods : 요청시

- 자원에 대한 행위를 정의
- GET, POST, PUT, DELETE
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

# HTTP response status codes : 응답시

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부
- ![image-20211114205759726](HTTP&RESTfulAPI.assets/1.png)

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

# 웹에서 리소스 식별 URI(Uniform Resource Identifier)

### URL (Uniform Resource Locator) 를 통한 자원 식별

- 통합 자원 위치
- 네트워크 상에 자원이 어디에 있는지 알려주는 약속

### URI (Uniform Resource Indicator)

- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소

# URI 구조

- Scheme(protocol) + Host(IP address) + Port + Path + Query + Fragment

- Port : HTTP 80 / HTTP 443

- Fragment = Anchor, 일종의 북마크로 # 뒤의 요청은 서버에 보내지지 않는다.

- ```bash
  https://www.example.com:80/path/to/myfile.html/?key=value#quick-start
  ```

# API

Application Programming Interface

프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스

### Web API

- 웹 어플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세이다.
- 응답 데이터 타입
  - HTML, XML, JSON 등







