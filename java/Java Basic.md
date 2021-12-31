[TOC]

# Java Basic

# tip

- **"sout" + tab** : System.out.println();  단축키
- for문 ( 조건부분 ) 작성시 변수타입 잊지말자!!!!



# 구조

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

- `public` - 접근 제어자
- `HelloWorld` - (내가 정한) 클래스명
- `static` - 바로 실행 가능하게 하는 제어자. main은 가장 먼저 실행되어야 하므로 main 앞에는 항상 static을 붙인다.
- `main` - 메소드(함수) 의 이름. 자바는 실행시 가장 먼저 main 이라는 이름의 메소드를 찾아 실행한다.
- `String[] args` - 자료형 + 변수명 으로 main 메서드가 받는 문자열 파라미터이다.
- `void` - 메서드의 리턴 값이 없다는 뜻이다.
- `System` - 자바의 내장 클래스이다.
- `out` - 자바 내장 클래스의 변수이다.
- `println` - 자바 내장 클래스의 변수의 메서드이다.



# 자료형

## 자료형이란?

변수에 저장되는 데이터의 종류

- Primitive Type(기본형) 과 Reference Type(참조형)으로 나뉜다.
  - `기본형`: 미리 정해진 크기의 메모리 사이즈로 표현 / 변수 자체에 값을 저장
  - `참조형`: 미리 정해질 수 없는 데이터 표현 /  변수에는 실제 값을 참조하는 주소를 저장

### [기본형] 8 Primitive Type - 미리 정해진 공간

변수가 값 자체를 보관한다.

##### 정수형

- `byte` : 8bit
- `short` : 16bit
- `기본형` `int` : 32bit 정수 리터럴.
- `long` : 64 bit / 롱 리터럴 표현방법 L
  - long myLong = 12345678910L;

##### 논리형

- `boolean` : true, false

##### 실수형

- `기본형` `double` : 64bit / 소수형 (float 쓰지 않는다.) / 리터럴 표현방법 d
  - double j = 314d;
- `float` : 32bit / 소수형 / 리터럴 표현방법 f
  - float h = 3.14f;

##### 문자형

- `char` : 16bit / 1자리 문자열(아스키코드)

### [참조형] Reference Type .. heap!

레퍼런스 타입은 미리 만들 수 없는 데이터를 별도의 공간(heap)에 표현하고(실제 객체를 만들고) 그 공간의 주소를 저장한다. 변수가 값을 '가리킨다'.

- `String` : 기본값은 `null`
- `객체` : 기본값은 `null`



## 기본형 vs. 참조형

- 기본형 - a와 b는 각각 다른 보관함

```java
int a = 3;
int b = a;

a = 4;

// a => 4
// b => 3
```

- 참조형 - p1과 p2는 같은 값을 가리킴

```java
Person p1, p2;
p1 = new Person("김모모", 29);

p2 = p1;
p2.setName("이모모");

// p1.getName() => 이모모
// p2.getName() => 이모모
```

```java
int[] a = new int[3]l;
int[] b = a;

a[0] = 1;
b[0] = 2;

// a[0] => 2
// b[0] => 2
```



# String Class

문자열은 String 클래스 기반의 자료형이다.

- 생성자로 생성

```java
char data[] = {'가', '나', '다'};
String myString = new String(data);
```

- 문자열 리터럴로 생성 & 메서드

```java
// 문자열 리터럴(String Literal)
String a1 = "aBc";
System.out.println(a1.toUpperCase()); 	// 대문자로 변환
System.out.println(a1.toLowerCase()); 	// 소문자로 변환
System.out.println(a1); 								// "aBc" 원본 유지
```

- 참조형의 비교연산자는 기본형과 다르게 값 자체가 아닌 가리키는 인스턴스를 비교

```java
// 참조형의 비교연산자는 가리키는 인스턴스가 같은 인스턴스인지를 확인
String b1 = "aBc";
System.out.println(b1.toLowerCase() == "abc"); 				// false
System.out.println(b1.toLowerCase().equals("abc")); 	// true
```



# Math Class & Random Class

```java
import java.lang.Math;
import java.util.Random;
import java.util.function.DoubleConsumer;
import java.util.stream.DoubleStream;

public class Conv {
    public static void main(String[] args) {
        // Math Class
        // 절댓값
        System.out.println(Math.abs(-10));
        System.out.println(Math.abs(8));

        // 최솟값
        System.out.println(Math.min(4.2, -5.3));
        System.out.println(Math.max(4.0, 10));

        // Random Class - 인스턴스 생성해야한다.
        Random rand = new Random();
        System.out.println(rand.nextInt(10)); // 0 이상 10 미만의 랜덤한 값
				
      	// 10 이상 30 미만의 랜덤한 값 = 0이상 20미만 랜덤값 + 10
        int min = 10;
        int max = 30;
        int rand_int = (int)Math.floor(Math.random()*(max-min+1) + min); 
        int rand_int2 = rand.nextInt((max-min)+1) + min; 
      
        System.out.println("rand+int " + rand_int);
        System.out.println("rand+int2 " + rand_int2);
      
        // 랜덤 불리언
        System.out.println(rand.nextBoolean());

        // 0에서 1사이의 난수 5개 생성
        DoubleStream ds = rand.doubles();
        ds.limit(5).forEach(new DoubleConsumer() {
            @Override
            public void accept(double value) {
                System.out.println(value);
            }
        });
    }
}

```



# Wrapper class

기본 자료형을 객체 형식으로 감싸는 클래스

- 기본 자료형을 참조형처럼 다룰 때 사용한다.
- Wrapper class의 인스턴스는 생성자 및 리터럴로 생성 가능하다.
- `Integer` 클래스는 `int` 형을 감싼다.
- `Double` 클래스는 `double` 형을 감싼다.
- `Long` 클래스는 `long`형을 감싼다.
- `Boolean` 클래스는 `boolean` 을 감싼다.

```java
// 생성자로 인스턴스 생성
Integer i = new Integer(123);

// 리터럴로 인스턴스 생성
Integer i = 123;
```

- 비교 - 참조형 비교연산자는 가리키는 객체가 같은지 비교, 두 생성자를 통해 만든 다른 객체이므로 false를 반환

```java
System.out.println(123 == 123); 	// true
System.out.println(new Integer(123) == new Integer(123));		// false
System.out.println(new Integer(123).equals(new Integer(123))); 	// true
```



# Array & ArrayList

- ArrayList 는 파이썬 배열처럼 동적배열로 사용 가능하다.

### 선언

```java
ArrayList<자료형(Wrapper 클래스)> 리스트명 = new ArrayList<>();
```

### 메서드

- `ArrayList.add(val)`  맨 뒤에 값을 추가한다.
- `ArrayList.remove(idx)` 해당 인덱스의 값을 삭제한다.
- `ArrayList.get(idx)` 해당 인덱스의 값을 가져온다.
- `ArrayList.size()` 리스트 길이를 구한다.

```java
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Conv {
    public static void main(String[] args) {
        // 일반 배열 생성1 (메서드 활용)
        int[] myArray = (int[])Array.newInstance(int.class, 10);
        System.out.println(Arrays.toString(myArray));
        // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        // 일반 배열 생성2 (선언 + 메모리할당)
        String[] myArray2;
        myArray2 = new String[10];
        System.out.println(Arrays.toString(myArray2));
        // [null, null, null, null, null, null, null, null, null, null]

        // 일반 배열 생성3 (통합)
        int[] myArray3 = new int[10];
        System.out.println(Arrays.toString(myArray3));
        // [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        // ArrayList 생성 
        ArrayList<Integer> myArrayList = new ArrayList<>();
        System.out.println(myArrayList);
        // []
        
        myArrayList.add(1);
        System.out.println(myArrayList);
        // [1]
        
        myArrayList.add(0, 3);
        myArrayList.add(0, 5);
        System.out.println(myArrayList);
        // [5, 3, 1]
        
        System.out.println(myArrayList.get(0));
        // 5
        
        myArrayList.remove(0);
        System.out.println(myArrayList);
        // [3, 1]
        
        System.out.println(myArrayList.size());
        // 2
    }
}
```



# 2차원 배열

- 선언은 행, 렬 순서로
- 데이터 입력은 for 문 인덱스 활용
- 출력은 deepToString 메서드로
  - 2차원 배열을 Arrays.toString() 함수를 이용하여 출력하면, 배열 안에 있는 배열을 가리키는 주소값이 차례로 출력되므로 Arrays.deepToString 메서드 사용해야 한다.

```java
import java.util.Arrays;

public class MultiArray {
    public static void main(String[] args) {
        // 3 * 4 빈 배열 생성
        int[][] multiArray = new int[3][4];

        // 데이터 입력
        int start = 1;
        for (int i = 0; i < multiArray.length; i++) {
            for (int j = 0; j < multiArray[i].length; j++) {
                multiArray[i][j] = start;
                start++;
            }
        }
        
        // 데이터 출력
        System.out.println(Arrays.deepToString(multiArray));

    }
}

// [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
```



# 배열

```java
        // 5개짜리 배열 선언 및 생성
        int[] arr = new int[5];

        // 선언 과 생성 따로
        int[] arr2;
        arr2 = new int[5];

        // 리터럴로 생성
        int[] arr3 = {1, 3, 5, 7, 9};
```

- main.java

```java
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // 크기가 30인 정수형 배열 intArray 생성
        int[] intArray = new int[30];
        
        // 배열의 첫번째 칸부터 1001, 1002, ... 1030 을 순서대로 넣는다.
        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = 1001 + i;
        }
        // System.out.println(Arrays.toString(intArray));
        
        // 크기가 4인 문자열 배열 생성 후 문자열 삽입
        String[] remainders = new String[4];
        String[] data = {"Zero", "One", "Two", "Three"};
        
        for (int i = 0; i < remainders.length; i++) {
            remainders[i] = data[i];
        }
        // System.out.println(Arrays.toString(remainders));
        
        // for-each 사용
        // intArray 배열에 담긴 각 값을 4로 나눈 나머지를 인덱스로
        // remainders 배열에서 그 인덱스에 위치한 단어를 출력
        for (int num : intArray) {
            System.out.println(remainders[num % 4]);
        }
    }
}
```



## arraylist -> array

- 리스트 컨테이너의 인스턴스를 배열로 만들어주는 `toArray` 메서드

```java
import java.util.List;
import java.util.ArrayList;

public class to_array {

// Java program to demonstrate working of
// Objectp[] toArray()

    public static void main(String[] args) {
        List<Integer> al = new ArrayList<Integer>();
        al.add(10);
        al.add(20);
        al.add(30);
        al.add(40);

        Object[] objects = al.toArray();

        // Printing array of objects
        for (Object obj : objects)
            System.out.print(obj + " ");
    }
}

// 10 20 30 40 
```

- 문자열 리스트를 배열로 만들어준다.

```java
import java.util.Arrays;

public class Array2 {
    public static void main(String[] args) {
        String dna = "GATCC";
        char[] charArray = dna.toCharArray();

        System.out.println(Arrays.toString(charArray));
        // [G, A, T, C, C]
    }
}
```

문자열의 `toCharArray()` 메소드(함수)를 사용하면 `char[]` 배열을 얻을 수 있습니다.

```java
char[] sequence = "abc".toCharArray();
System.out.println(Arrays.toString(sequence)); // [a, b, c]
```

반대로 `char[]` 배열을 문자열로 바꾸려면 이렇게 하면 됩니다:

```java
String stringFromCharArr = new String(sequence);
System.out.println(stringFromCharArr); // abc
```



# aliasing vs clone

- 앨리어싱 : 배열을 통째로 넘겨 두 변수가 같은 주소를 가리킨다.
- 클론 : clone 메서드를 사용하여 기존 배열은 유지하고 새로운 배열을 복사한다.

```java
        int[] myArray = {1, 2, 3, 4, 5};
        int[] myAlias = myArray;
        int[] myClone = myArray.clone();
        myArray[0] = 100;

        System.out.println(myAlias[0]); // 100
        System.out.println(myClone[0]); // 1
```



# for-each (index 가 아닌 배열의 value 순회)

- r 은 intArray 의 0번 인덱스의 "값"을 가지게 된다.

```java
        int[] intArray = new int[10];
        for (int i = 0; i < intArray.length; i++) {
            intArray[i] = i+4;
        }
        System.out.println(Arrays.toString(intArray));
				// [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

				// for-each 사용
        for (int r : intArray) {
            System.out.print(r + " ");
        }
				// 4 5 6 7 8 9 10 11 12 13 
```

- str_val 은 문자열 배열의 0 번 인덱스의 "값"을 가지게된다.

```java
        String[] stArr = new String[5];

        stArr[0] = "문자1";
        stArr[1] = "문자2";
        stArr[2] = "문자3";
        stArr[3] = "문자4";
        stArr[4] = "문자5";

        for (String str_val : stArr) {
            System.out.println(str_val + " ");
        }

/* 
문자1 
문자2 
문자3 
문자4 
문자5 
*./
```





# 출력

- print
- println : 다음줄 바꿈
- printf : 자료형 포매팅

### printf

- `%f` : 실수
- `%c` : 문자
- `%s` : 문자열
- `%d` : 10진수 정수
- `%o` : 8진수 정수
- `%x` : 16진수 정수
- `%n` : 줄바꿈

### 배열 출력 import java.util.Arrays;

- Arrays 클래스 사용해서 출력가능하다.
- 인덱스 값을 넣지 않을 경우 기본값 0이다.

```java
import java.util.Arrays;

public class HelloWorld {
    public static void main(String[] args) {
      
      	// 5개짜리 배열 생성
        int[] arr = new int[5];
      
      	// arr[0] = 1;
      	arr[1] = 3;
        arr[2] = 5;
        arr[3] = 7;
        arr[4] = 9;
      	
      // System.out.println(arr); => 출력 불가
      System.out.println(Arrays.toString(arr));
```

- for 문 사용 하여 배열의 모든 원소 출력

```java
        for (int s = 0; s < arr.length; s++) {
            System.out.println(arr[s]);
        }
```



# 연산자

- 파이썬과 다른점
  -  `/`  값 두개가 정수일 경우 나눠도 몫인 정수가 출력된다. (몫 == python `//`)
  -  따라서 소수를 원한다면 연산하는 값중 하나에 `double` 을 넣어 실수로 바꿔주어야 한다.
  
  ```java
  public class AverageFinder {
      double computeAverage(int[] intArray) {
          int total = 0;
          for (int i = 0; i < intArray.length; i++) {
              total += intArray[i];
          }
          
          return (double)total / intArray.length; 
        	// total 에만 double 자료형 적용
          // 4.33333333333
      }
  }
  ```
  
  ```java
  public class Main {
      public static void main(String[] args) {
          AverageFinder finder = new AverageFinder();
        
          int[] testArray1 = {3, 7, 3};
          System.out.println(finder.computeAverage(testArray1));
      }
  }
  ```
  
  
  
- 불린 연산자
  - `&&` : and
  - `||` : or



# 형 변환

### 묵시적 형변환(promotion)

- 바꾸고자 하는 형이 기존의 형보다 넓은 데이터를 담을 수 있는 경우 특별한 처리 없이 형 변환 가능
- 연산자 형변환 랭킹

  - double > float > long > int > short > byte

    - 피연산자 중 하나라도 소수형이 있다면 소수형이 나온다.
    - int 에 double 을 할당할 수 없다. double의 범위가 더 크기 때문이다.

### 명시적 형변환(typecasting)

- 억지로 바꾸고 싶으면 `type casting`을 해서 소수 부분을 버린다.
  - `(int) 3.14` => 3

- 정수 / 정수를 소수로 바꾸려면 `type casting` 한다. 
  - `System.out.println((double) 8 / 5);` => 1.6



# 조건문 & switch 문

- 조건문 if  / else if / else

```java
        int temp = 13;
        if (temp <= 3) {
            System.out.println("low");
        } else if (temp <= 5) {
            System.out.println("mid");
        } else {
            System.out.println("high");
        }
```

- switch (break 필수, default 는 선택)

```java
        // switch
        int score = 40;
        String grade;
        switch (score / 10) {
            case 10:
                grade = "A+";
                break;
            case 9:
                grade = "A";
                break;
            case 8:
                grade = "B";
                break;
            default:
                grade = "C";
        }

        // switch 2
        switch (grade) {
            case "A+":
            case "A":
            case "B":
                System.out.println("very good");
                break;
            case "C":
                System.out.println("need more");
            default:
                System.out.println("recourse");
                break;
        }
```

```
// need more
// recourse
```



# while문

```java
        int sum = 0, i = 1;

				// sol 1

        while (sum < 10000) {
            sum += i;
            i++;
        }

				// sol 2

        while (true) {
            if (sum >= 10000) {
                break;
            }

            sum += i;
            i++;
        }

        System.out.println(sum);
        System.out.println(i - 1);
```

- 10000 미만 정수 중 153의 배수 중 가장 큰 값

```java
        int num = 10000;
        int key = 153;

        while (num % key > 0) {
            num --;
        }
        System.out.println(num);
```



# for문

- 반복문 시작 인덱스 설정할 때, **자료형**을 써주는 것을 잊지 말자!!!!!

```java
        int sum = 0;
        for (int k = 1; k <=5; k++) {
            sum += k;
        }
        System.out.println(sum);
```



# 배열의 모든 합 구하기

```java
public class AverageFinder {
  
    // 1. 일반 for문
    double computeAverage(int[] intArray) {
         int sum = 0;
         for (int i = 0; i < intArray.length; i++) {
             sum += intArray[i];
         }
         return (double) sum / intArray.length;
     }
    
     // 2. while문
     double computeAverage(int[] intArray) {
         int sum = 0;
         int i = 0;
        
         while (i < intArray.length) {
             sum += intArray[i];
             i++;
         }
         return (double) sum / intArray.length;
     }
     
     // 3. for-each문
     double computeAverage(int[] intArray) {
         int sum = 0;
         for (int val : intArray) {
             sum += val;
         }
         return (double) sum / intArray.length;
     }
}
```

```java
public class Main {
    public static void main(String[] args) {
        AverageFinder finder = new AverageFinder();

        // 테스트
        int[] testArray1 = {3, 7, 3};
        System.out.println(finder.computeAverage(testArray1));

    }
}
```



# max, min

```java
public class GreatestDifferenceFinder {
    int greatestDifference(int[] intArray) {
        // 원소가 0개 또는 1개면 0 리턴
        if (intArray.length < 2) {
            return 0;
        }

        // 두 원소의 차 중 최댓 값 구하기 = 최댓값 - 최솟값
        // 최댓값, 최솟값 구하기
        int max = intArray[0];
        int min = intArray[0];

        // for-each
        for (int i = 0; i < intArray.length; i++) {
            if (intArray[i] > max) {
                max = intArray[i];
            }

            if (intArray[i] < min) {
                min = intArray[i];
            }
        }
        return max - min;
    }
}
```

```java
public class Main {
    public static void main(String[] args) {
        GreatestDifferenceFinder finder = new GreatestDifferenceFinder();
    }
}
```



# null

- `null` 은 참조형 변수(Reference Type)만이 가질 수 있는 값이다.

```java
Person p1 = null;
System.out.println(p1);
// null
```

- 만약 `null` 을 보관하고 있는 변수의 메소드를 호출하면, `NullPointerException` 오류가 발생한다.
- 따라서 객체가 `null` 인지 미리 확인해야 한다.

```java
Person[] people = new Person[5]; // 5개짜리 Person 타입의 배열 생성
people[0] = new Person("김", 28);
people[2] = new Person("이", 25);
people[3] = new Person("박", 26);

for (int i=0; i < people.length; i++) {
  Person p = people[i];
  if (p != null) {
    System.out.println(p.getName());
  } else {
    System.out.println(i + "번 자리는 비었습니다.");
  }
}
```

- 문자열 배열 예시

```java
String[] strings = new String[3];
strings[0] = "hi";
strings[1] = "";

// strings => ["hi", "", null];
```

* strings[0] == null 은 `false`
* strings[0].isEmpty() 은 `false`
* strings[1] == null 은 `false`
* strings[1].isEmpty() 는 `true`
* strings[2] == null 은 `true`
* strings[2].isEmpty()는 `오류발생`



# try-catch 예외처리

```java
try {
  // 오류가 발생할 코드
} catch (Exception e) {  // 파라미터로 Exception 클래스의 인스턴스를 받음, 참조변수e
  // 오류 발생시 처리할 코드
  System.out.println(e.getMessage());
}
```

- `ArrayIndexOutOfBoundsException` 인스턴스를 파라미터로 받는다

```java
public class Main {
    public static void main(String[] args) {
        int[] smallArray = new int[3];

        for (int i = 0; i < 10; i++) {
            try {
                smallArray[i] = i;
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println(i +"번째 시도에서 예외 발생");
            }
        }
        for (int num : smallArray) {
            System.out.println(num);
        }
    }
}
```

```
3번째 시도에서 예외 발생
4번째 시도에서 예외 발생
5번째 시도에서 예외 발생
6번째 시도에서 예외 발생
7번째 시도에서 예외 발생
8번째 시도에서 예외 발생
9번째 시도에서 예외 발생
0
1
2
```

