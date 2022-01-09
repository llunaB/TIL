# 1. Generics

## 1.1 지네릭스란?

지네릭스는 다양한 타입의 객체들을 다루는 메서드나 컬렉션 클래스에 컴파일 시의 타입체크를 해주는 기능이다.

다룰 객체의 타입을 미리 명시해준다.



## 1.2 지네릭 클래스의 선언

지네릭 타입은 클래스와 메서드에 선언할 수 있다.

### 지네릭 클래스 Box<T>

- 클래스에 선언
  - `T` : 타입 변수, 타입 매개변수

```java
class Box<T> {
  T item;
  void setItem(T item) { this.item = item; }
  T getItem() { return item; }
}
```

- 지네릭 클래스가 된 Box 클래스의 객체 생성 - 실제 타입 지정
  - `String` : 지정된 타입, 매개변수화된 타입(대입된 타입)

```java
Box<String> b = new Box<String>();
b.setItem("abc");
String item = b.getItem();
```

