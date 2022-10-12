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

- 1003

  - Cron Scheduler for Batch Programming : 초 분 시간 일 월 요일 연도(생략가능)
  
    ```shell
    0 15 10 * * ?   #=> 매일 오전 10시 15분에 실행
    0 0 0 * * ?     #=> 매일 새벽 12시에 실행

- 1011

  - 포인터
    - 참조 연산자 *
    - 주소 연산자 &

  ```c
  int n = 100;
  int* p = &n; //타입* 포인터명 = &변수명;
  
  //*p => 100
  //p => 0xb6c2355c
  ```

  - 구조체

  ```c
  struct jsu //구조체명
  {
    char nae[12];
    int os, db, hab, hhab;
  };
  
  void main()
  {
    struct jsu a; //구조체변수 a 선언, a.멤버변수명으로 접근
    struct jsu b[10]; //배열로 선언
  }
  ```

  

- 1012
  - 싱글톤 패턴 : 어플리케이션이 시작될 때 어떤 클래스가 최초 한 번만 메모리를 할당하고(static) 그 메모리에 인스턴스를 만들어 사용하는 디자인 패턴
    - 메모리 낭비 방지
    - 데이터 공유
    - 멀티쓰레드 환경에서 동기화 처리 필수
  - 하나의 인스턴스를 메모리에 등록하여 여러 개의 쓰레드가 동시에 해당 인스턴스를 공유하여 사용한다.
  - DBCP처럼 공통 객체를 여러개 생성해서 사용해야 하는 상황에서 사용한다
  - 여러 쓰레드에서 동시에 접근하는 것을 막기 위해 `synchronized` 를 활용한다.

```java

class Connection {

  // 기본생성자를 private 사용하여 생성 불가하게 한다
  private static Connection _inst = null;
  private int count = 0;

  // getInstance를 통해서만 생성 가능
  static public Connection getInstance() {
    if (_inst == null) {
      _inst = new Connection();
      return _inst;
    }
    // 인스턴스가 있다면 기존 것을 반환
    return _inst;
  }

  public void count() {
    count++;
  }

  public int getCount() {
    return count;
  }

  // 여러 쓰레드에서 동시에 접근하는 것을 막는다
  public synchronized static void main(String[] args) {
    Connection conn1 = Connection.getInstance();
    conn1.count();
    Connection conn2 = Connection.getInstance();
    conn2.count();
    Connection conn3 = Connection.getInstance();
    conn3.count();

    System.out.println(conn1.getCount()); // 3
  }
}

```

