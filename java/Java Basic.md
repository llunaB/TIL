# Java Basic

## tip

- **"sout" + tab** : System.out.println();  단축키
- for문 ( 조건부분 ) 작성시 변수타입 잊지말자!!!!



## 자료형

- `byte` : 8bit
- `short` : 16bit
- `int` : 32bit 정수 리터럴.
- `long` : 64 bit / 롱 리터럴 표현방법 L
  - long myLong = 12345678910L;
- `boolean` : true, false
- `double` : 64bit 소수형 (float 쓰지 않는다.) / 리터럴 표현방법 d
  - double j = 314d;
- `float` : 소수형 / 리터럴 표현방법 f
  - float h = 3.14f;

- `char` : 1자리 문자열

기본자료형이 아닌 클래스

- `String`



## 2차원 배열

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



## 배열

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



## aliasing vs clone

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



## for-each (index 가 아닌 배열의 value 순회)

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





## 출력

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



## 연산자

- 파이썬과 다른점
  -  `/`  정수 나누기 정수 = 정수가 출력된다. (몫 == python `//`)

- 불린 연산자
  - `&&` : and
  - `||` : or



## 형 변환

- 바꾸고자 하는 형이 기존의 형보다 넓은 데이터를 담을 수 있는 경우 특별한 처리 없이 형 변환 가능

- 연산자 형변환 랭킹

  - double > float > long > int > short > byte

    - 피연산자 중 하나라도 소수형이 있다면 소수형이 나온다.
    - int 에 double 을 할당할 수 없다. double의 범위가 더 크기 때문이다.
      - 억지로 바꾸고 싶으면 `type casting`을 해서 소수 부분을 버린다.
      - `(int) 3.14` => 3

    - 정수 / 정수를 소수로 바꾸려면 `type casting` 한다.
      - `System.out.println((double) 8 / 5);` => 1.6



## 조건문 & switch 문

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



## while문

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



## for문

```java
        int sum = 0;
        for (int k = 1; k <=5; k++) {
            sum += k;
        }
        System.out.println(sum);
```

