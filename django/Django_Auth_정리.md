![image-20210917091441454](/Users/euijinpang/TIL/django/Django_Auth_정리.assets/image-20210917091441454.png)

1. 브라우저가 로그인 정보를 보내면 서버가 서버 메모리에 `session` 을 저장
2. 서버는 `cookie(sessionid)` 를 브라우저에 전송
3. 브라우저는 `cookie(sessionid)` 와 함께 인증응답`authenticate req` 을 서버에 전송
4. 서버는 `cookie`를 체크하여 `session`으로부터 유저정보를 얻고(session id 즉 key를 확인하고 value를 얻음) 응답을 반환

