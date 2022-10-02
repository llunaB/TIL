# TIL

> Today I Learned



- 0728
  - Java HashMap 사용하기

- 0831
  - Java 옵저버 패턴

- 0901
  - Spring, JDK, Maven, Jar

- 0917
  - Disk는 Sequential Device 가 아닌 Random Device로 파일을 읽고 쓰기 위해 내부적인 Block으로 쪼갠다.
  - 그리고 이 블록의 조합을 Mater Blocktable에 기록하며, 해당 파일이 00번 block에 있다고 기록한다.
  - NTFS File System은 mater file table과 mirroring file table 2개를 두고, 깨지면 sync를 맞추어 찾는다.

- 0921
  - `.dat`  : 파일을 만든 프로그램과 관련된 특정 정보를 저장하는 일반 데이터 파일
  - `.bat` : MS-DOS 명령어를 한 번에 적어놓고 실행할 수 있게 만든 명령어 스크립트

- 0922 
  - 메세지큐와 메세지 브로커
  - **Publish-and-subscribe** **messaging**

- 0927
  - AP, WEB, WAS, DB server

- 1002

  - 개발도구의 분류 : 구현도구 - 테스트도구 - 형상관리 도구 - 빌드도구
  - 서버 하드웨어 개발환경 : 웹서버 - 웹어플리케이션 서버 - DB서버
    - Web Server : Apache, Nginx
    - Web Appication Server (WAS) : Tomcat, Jeus!! 제우스 !!!
    - 여기서 WAS 를 `미들웨어` 로 분류한다.(소프트웨어 기준)

  - 형상관리 도구 유형

    - 클라이언트/서버방식 : SVN 

      - 소스 저장소 == 서버, 작업 PC == 클라이언트

      - 원격 저장소로부터 checkout받고, 코딩 후 commit 

      - ```
        - trunk: 프로젝트에서 가장 중심이 되는 디렉토리 
        - branches: trunk에서 뻗어져 나온 나뭇가지를 뜻함. 프로젝트 내의 작은 프로젝트라고 생각하면 됨 
        - tags: 버전 별로 소스코드를 따로 관리하는 공간(버전 별로 태그를 붙여서 tag 디렉토리 안에 보관한다고 생각하면 됨)
        ```

    - 분산저장소 방식 : Git

      - 저장소 백업 따로 안해도 clone만 하면 됨
      - 수백-수천명 프로그래머의 분산작업에 용이, 소스충돌위험 낮음

  - 소프트웨어 모듈의 응집도와 결합도

    - 응집도는 모듈내부, 높을수록 좋고 결합도는 모듈간, 낮을수록 좋다. 독립성이 높아야 오류수정이 용이.

    
