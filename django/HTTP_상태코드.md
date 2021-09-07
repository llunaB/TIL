# HTTP 상태 코드

https://developer.mozilla.org/ko/docs/Web/HTTP/Status



[`200 OK`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/200)

요청이 성공적으로 되었습니다. 성공의 의미는 HTTP 메소드에 따라 달라집니다:
GET: 리소스를 불러와서 메시지 바디에 전송되었습니다.
HEAD: 개체 해더가 메시지 바디에 있습니다.
PUT 또는 POST: 수행 결과에 대한 리소스가 메시지 바디에 전송되었습니다.
TRACE: 메시지 바디는 서버에서 수신한 요청 메시지를 포함하고 있습니다.

- 잘 됐다!

---



[`500 Internal Server Error`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/500)

서버가 처리 방법을 모르는 상황이 발생했습니다. 서버는 아직 처리 방법을 알 수 없습니다.

- 서버의 문제. 디버깅이 필요한 상황. 
- 500은 개발자 잘못.



---



[`301 Moved Permanently`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/301)

이 응답 코드는 요청한 리소스의 URI가 변경되었음을 의미합니다. 새로운 URI가 응답에서 아마도 주어질 수 있습니다.

- 리다이렉트, 그런 주소 없으니까 다른 곳으로 연결해드릴게요. 오타를 쳐도 들어오게 만든다. 하위 도메인 등 이용

  - naver.com => www.naver.com 

  

---

- 400은 사용자 잘못

[`400 Bad Request`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/400)

이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.

- 고객님이 잘못하셨습니다.



[`401 Unauthorized`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/401)

비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다

- 여기는 직원 전용이에요. 들어올 권한이 없으세요.



[`403 Forbidden`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/403)

클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않습니다. 예를들어 그들은 미승인이어서 서버는 거절을 위한 적절한 응답을 보냅니다. 401과 다른 점은 서버가 클라이언트가 누구인지 알고 있습니다.

- 같은 회사 사람인데 권한이 없어



[`404 Not Found`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/404)

서버는 요청받은 리소스를 찾을 수 없습니다. 브라우저에서는 알려지지 않은 URL을 의미합니다. 이것은 API에서 종점은 적절하지만 리소스 자체는 존재하지 않음을 의미할 수도 있습니다. 서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위하여 이 응답을 403 대신에 전송할 수도 있습니다. 이 응답 코드는 웹에서 반복적으로 발생하기 때문에 가장 유명할지도 모릅니다.

- 없는 정보를 요청했습니다. "죄송합니다. 요청하신 페이지를 찾을 수 없습니다."



[`405 Method Not Allowed`](https://developer.mozilla.org/ko/docs/Web/HTTP/Status/405)

요청한 메소드는 서버에서 알고 있지만, 제거되었고 사용할 수 없습니다. 예를 들어, 어떤 API에서 리소스를 삭제하는 것을 금지할 수 있습니다. 필수적인 메소드인 `GET`과 `HEAD`는 제거될 수 없으며 이 에러 코드를 리턴할 수 없습니다.

- POST 방식으로 넣어야 하는데, GET 방식으로 들어옴. 