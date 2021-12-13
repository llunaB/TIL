# java

" 자바 가상머신 Java Virtual Machine, JVM " 을 통해 어느 운영체제던 디바이스던 동일하게 동작하며 호환성 문제를 해결해준다.

- JVM : Java Virtaul Machine 자바 가상머신
- JRE : Java Runtime Environment 자바가 돌아가기 위한 환경
- JDK : Java Development Kit 자바 개발도구. JDK 설치시 JVM 설치된다.



### 구조

```java
 // HelloWorld 라는 이름의 공개된 클래스를 만든다
public class HelloWorld {
    // main 메소드는 누구나 접근할 수 있고, 바로 실행할 수 있고, 리턴값 없다.
    // arg라는 이름의 문자열 변수가 메소드에 전달된다.
    public static void main(String[] args) {                                     
        System.out.println("Hello World!");
    }
}

```

- public: 접근 제어자
- HelloWorld: (내가 정한) 클래스명
- static: 바로 실행 가능하게 만든다. main은 가장 먼저 실행되어야 하므로 main 앞에는 항상 static을 붙여준다.
- main: 메소드(함수)의 이름. 자바는 실행시 가장 먼저 main이라는 이름의 메소드를 찾아 실행한다. 자바의 함수는 모두 메소드이다. 
- String[] args: 자료형 그리고 변수명. main 메소드가 받는 문자열 파라미터
- void: 메소드(함수)의 리턴 값의 자료형. void의 경우 리턴 값이 없다.
- System: 자바의 내장 클래스
- out: 클래스 변수
- println: 메서드











