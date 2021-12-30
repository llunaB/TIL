[TOC]

# Write Once, Run Anywhere

C++ 은 컴파일러로 컴파일 후 바이너리 어플리케이션이 되는데, 컴파일러와 머신코드는 운영체제 종속적이다.  반면 Java는 소스코드를 컴파일 후 "바이트코드" 를 생성하게 되며, 이것을 JVM(Java Virtual Machine) 이라 한다. 

**'.class' 파일은 JVM에서 동작시키기 때문에 어떤 OS에 깔려있던 동일하게 사용할 수 있다.**

![image-20211230130625343](java_이론.assets/image-20211230130625343.png)



# 가비지콜렉터(G.C)

더 이상 사용하지 않는 메모리를 자동으로 정리하는 기능

```java
String hello = new String("Hello"); // 메모리 생성 후 hello가 참조
System.out.println(hello);

hello = null;  // 메모리상에서 아무것도 참조하지 않는다.
// 메모리에 처음 만들어졌던 사용하지않은 메모리가 자동적으로 정리된다.
```

- G.C가 일어나는 시점은 알 수 없다.  따라서 관리할 필요가 없다.



# compile & run

- compile
  - `-d` 옵션으로 패키지 컴파일이 가능하다.

```bash
javac -d . HelloWorld.java
```

- run

```bash
java com.ssafy.HelloWorld
```



# IDE(eclipse)

Integrated Development Environment

- Build path 살피기 (설치된 JRE 라이브러리 경로)



# byte type

이진수 타입

- 00001001 => 9
- 10001001 => -128 + 9 => -119
  - First Bit 1 means Negative (Java 에서 첫번째 비트가 1이면 음수다)



## 기본형 타입과 참조형 데이터 타입

- 참조형 데이터 타입은 최대 몇 개까지 사용 가능?
  - 기본 데이터타입은 8가지다. 나머지 모든 데이터 타입은 참조형이다.



## ASCII

```java
public class HelloWorld {
	public static void main(String[] args) {
		int k = 66;
		char c = (char) k;
		System.out.println(c);
		
		c = 'A';
		k = c;
		System.out.println(k);

	}
}

// B
// 65
```



# 증감 연산자

- 전위 연산자 : 먼저 연산
- 후위 연산자 : 모듈연산을 먼저 하고 이후 연산

```java
public class HelloWorld {
	public static void main(String[] args) {
		int i = 10;
		System.out.println((i--) % 2); 
    // 0 : 10을 2로 나눈 나머지 0을 출력하고 --하여 메모리 상의 i는 9
		System.out.println(--i); 
    // 8 : 9에서 -- 하고 출력하고 메모리상의 i는 8
		System.out.println(i++); 
    // 8 : 출력 하고 ++ 메모리상의 i는 9
		// System.out.println(++(i-2)); 
    // ++, --는 변수를 대상으로 연산 진행. i-2는 연산의 결과값이므로 사용불가.
	}
}

```



# 연산자

- 이항 연산자의 최소단위는 `int` 이므로 `byte`를 사용하여도 int 로 바뀐다.
- `int` 와 `long` 을 연산하려하면 `int`가 `long` 으로 바뀐다.
- 두 개의 피연산자 중 큰 타입으로 형 변환 후 연산을 진행한다.



# 정수 overflow

```java
int i1 = Integer.MAX_VALUE;
int i2 = i1+1;
```

![image-20211230150958374](java_이론.assets/image-20211230150958374.png)

- i2는? 음수값(가장 작은 정수)이 되어버린다.



# random class

```java
import java.util.Random;

public class RandomTest{ 
  public static void main(String[] args){ 
    Random random = new Random(); 
    System.out.println( random.nextInt() ); // 1,700,703,373 (-2,147,483,648 ~ 2,147,483,647 사이의 값) 
    System.out.println( random.nextInt(10) ); // 2.3279967568276427 (0 ~ 9 사이의 값) 
    System.out.println( random.nextInt(10) + 1 ); // 2 (1 ~ 10 사이의 값) 
    System.out.println( random.nextInt(10) * (-1) ); // -7 ( -9 ~ 0 사이의 값) 
    System.out.println( random.nextBoolean() ); // true (true or false) } }\
```



# 삼항연산자

```java
import java.util.Random;

public class BasicProblem {
  public static void main(Sting[] args) {
    int n = 6;
    Random rand = new Random();
    
    int num1 = rand.nextInt(n)+1;
    int num2 = rand.nextInt(n)+2;
    
    String result = null;
    // num1과 num2가 모두 짝수이거나 홀수이면 A, 아니면 B를 출력하시오.
    
    System.out.printf("%d, %d ==> %s%n", num1, num2, result);
  }
}
```

