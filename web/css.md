# CSS

Cascading Style Sheet

사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어



## 정의 방법

1. 인라인
2. 임베딩 - <head> 내 <style> 지정
3. 외부 참조 - 외부 css파일을 <head>내 <link>를 통해 불러온다. 모듈화 가능

![image-20210802111708995](/Users/euijinpang/TIL/web/css.assets/image-20210802111708995.png)

## CSS Seletor

![image-20210802112159807](/Users/euijinpang/TIL/web/css.assets/image-20210802112159807.png)

### 기본 선택자

- 전체 선택자, 요소 선택자

```css
<!-- 전체 선택자 -->
* {
	color : red;
}
<!-- 요소 선택자 -->
h2 {
	color : orange;
}
```



- 클래스 선택자, 아이디 선택자, 속성 선택자

```css
<!-- . 클래스 선택자 -->
.green{
	color : green;
}

<!-- # id 선택자 - id는 문서에서 단 한번만 !!! 사용!!--> 
#purple{
	color : purple;
}
```



### 결합자 (combinators)

- 자식, 자손 결합자

```css
<!-- 자식 결합자 : 바로 아래 요소 -->
.box > p {
	color : green;
}
<!-- 자손 결합자 : 하위의 모든 요소 -->
.box p {
	color : green;
}
```

- 일반 형제 결합자, 인접 형제 결합자

```css
<!-- 일반 형제 결합자 : 형제 요소 중 뒤(코드상 뒤)에 위치하는 요소를 모두 선택 -->
p ~ span {
	color : green;
}
<!-- 인접 형제 결합자 : 형제 요소 중 '바로' 뒤에 위치하는 요소 한개를 선택 -->
p + span {
	color : green;
}
```





### 의사 클래스/요소 (pseudo class)

- 링크, 동적 의사 클래스
- 구조적 의사 클래스



## 적용 우선순위(cascading order)

1. `!important`
2. 인라인 > id선택자 > class선택자 > 요소선택자
3. 코드 순서



## 크기 단위

- px
- %
- em : 바로 위, 부모 요소에 영향을 받는다. 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐.
- rem
  - 최상위 요소(html) 사이즈(16px)를 기준으로 배수 단위를 가짐.
- viewport 
  - 주로 스마트폰이나 테블릿 디바이스의 화면
  - 글자 그대로 디바이스의 뷰포트를 기준으로 상대적인 사이즈 결정.



## shorthand

![image-20210802151352157](/Users/euijinpang/TIL/web/css.assets/image-20210802151352157.png)

![image-20210802151402562](/Users/euijinpang/TIL/web/css.assets/image-20210802151402562.png)

## BOX-SIZING

- 디폴트는 `content-box` 이다.
- 우리가 일반적으로 영역 볼 때는 border까지 너비를 보기 때문에 `box-sizing`을 `border-box`로 설정

![image-20210802151849256](/Users/euijinpang/TIL/web/css.assets/image-20210802151849256.png)

## 마진 상쇄

- block A의 top과 block B의 bottom에 적용된 각가의 margin이 둘 중 큰 마진값으로 결합
- 따라서, margin-top , margin-bottom 중 하나 사용하자!





## Display : block & inline

##### display : block

- 화면 가로 전체 차지 (100%)
- 블록 요소 안에 인라인 요소 들어갈 수 있음
- div / ul, ol, li / p / hr / form

##### display : inline

- 컨텐츠 영역만큼 차지

- 상하여백은 `line-height` 로 지정한다. 가로세로폭 못정하니까!
- width, height, margin-top, margin-bottom 지정 불가
- span / a / image / input,label / b, em, i, strong

![image-20210802153333828](/Users/euijinpang/TIL/web/css.assets/image-20210802153333828.png)

##### display : inline-block

- inline처럼 한 줄에 표시 가능하며
- block처럼 width, height, margin 속성 적용 가능하다



##### display : none vs. visibility : hidden

- none - 해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다)
- hidden - 공간은 남아있고 화면에만 표시하지 않는다.



## CSS Position

##### static

- 모든 태그의 기본위치 (좌측 상단)
- 부모 요소 내에 배치시 부모 요소의 위치를 기준으로 배치

---------아래는 좌표 프로퍼티로 이동가능

##### relative

- 자기자신의 static 위치를 기준으로 이동
- 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음

<img src="/Users/euijinpang/TIL/web/css.assets/image-20210802155316974.png" alt="image-20210802155316974" style="zoom:50%;" />

```css
.relative{
  position:relative;
  top:100px;
  left:100px;
}
```

##### absolute

- 절대 위치 : 요소를 일반적 문서 흐름에서 제거, <u>레이아웃에 공간을 차지하지 않음</u>
- <u>static이 아닌</u> 가장 가까이 있는 부모/ 요소를 기준으로 이동(없는경우 body에 붙는 형태)
- <u>**따라서 static이 아닌 부모를 미리 만들고 이동시켜야한다!!**</u>
- 격리된 UI 

<u><img src="/Users/euijinpang/TIL/web/css.assets/image-20210802155333284.png" alt="image-20210802155333284" style="zoom:50%;" /></u>



```css
.parent{
  position:relative;
}

.absolute_chold{
  position:absolute;
  top:50px;
  left:50px;
}
```



##### fixed

- 고정 위치: 일반적 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
- 부모요소와 관계없이 viewport를 기준으로 이동
- 스크롤 시에도 항상 같은 곳에 위치함

<img src="/Users/euijinpang/TIL/web/css.assets/image-20210802155351662.png" alt="image-20210802155351662" style="zoom:50%;" />



```css
.fixed{
  position:fixed;
  bottom:0;
  right:0;
}
```



