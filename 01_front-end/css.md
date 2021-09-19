# CSS

## 기본문법

- 선택자 {

  속성: 값;

  속성: 값;

  }



## 선언방식

- 내장방식 : html 내에 <style></style> 요소 내에 입력

- 인라인 방식 : 요소의 style 전역속성으로 추가

- 링크 방식 : html 내에서 <link> 로 연결하는 방식

  - ```html
    <link rel="stylesheet" href="./css/main.css">
    ```

  - 병렬방식

- Import 방식 : css 안에서 또다른 css 문서를 가져와 연결하는 방식

  - ```css
    @import url("./box.css");
    
    div {
      color: red;
    }
    ```
    
  - 직렬방식 : html 에서 상위 css 가 연결되어있어야만 작동한다.
  - main.css 양이 많을 경우 먼저 처리하는 과정에서 시간이 오래 걸리므로 일부러 늦출때 사용



## 선택자

- 기본선택자
  - `*` 전체 선택자
  - `tag` 태그 선택자
  - `.classname` 클래스 선택자
  - `#idname` 아이디 선택자
- 복합선택자
  - `span.orange` 일치 선택자 : 태그와 클래스를 동시에 만족하는 요소 선택
  - `ul > .orange` 자식 선택자 : 선택자의 자식 요소를 선택
  - `div .orange` 자손(하위, 후손) 선택자 : 선택자의 하위 모든 요소 선택
  - `.orange + li` 인접 형제 선택자 : orange 클래스를 지닌 의 다음 요소 중 li **하나**를 선택
  - `.orange ~ li ` 일반 형제 선택자 : orange 클래스를 지닌 의 다음 요소 중 li **모두**를 선택

- 가상클래스

  - `:hover` 마우스 오버하는 동안 선택

    ```css
    .box:hover {
      width: 300px;
    }
    ```

  - `active` 마우스를 클릭하고 있는 동안 선택

    ```css
    .box:active {
      width: 300px;
    }
    ```

  - `:focus` 포커스되면 선택 , 포커스 가능한 요소에서만 동작

    ```css
    input:focus {
      background-color: palegoldenrod;
    }
    ```

    - 만약 focus 요소가 아닌 요소를 focus 되도록 만들고싶다면 html `tabindex` 속성을 `-1` 로 사용, 비권장

    ```html
    <div class="box" tabindex="-1"></div>
    
    .box:focus {
      width: 300px;
    }
    ```

    

- 일반 가상클래스 선택자

  - `ABC:first-child` 선택자 ABC가 형제 요소 중 첫째라면 선택
  - `ABC:last-child` 선택자 ABC가 형제 요소 중 막내라면 선택

  - `ABC:nth-child(n)` 선택자 ABC가 형제 요소 중 (n)번째라면 선택 (n은 0부터 시작)
    - ABC:nth-child(2n) : 짝수번째 요소 선택
  - `ABC:not(XYZ)` 선택자 XYZ가 아닌 ABC 요소 선택



- 가상요소 선택자

  - `ABC::before` 선택자 ABC 요소의 내부 앞에 내용(가상의 인라인 요소)을 삽입
  - `content`  값을 비워 놓더라도 Css속성 필수!! 

  ```css
  .box::before {
    content:"";
  }
  ```

  - 앞! Content!

  ```html
  <div class="box">
    Content!
  </div>
  
  .box::before{
  	content: "앞!";
  }
  ```

  - Content! 뒤!

  ```html
  <div class="box">
    Content!
  </div>
  
  .box::after{
  	content: "뒤!";
  }
  ```

  - 사용예시

  ![image-20210918130217935](CSS.assets/1.png)

  ![image-20210918130230509](CSS.assets/2.png)

- 속성 선택자

  - `[ABC]` 속성 ABC 를 포함한 요소 선택

  ```css
  <input type="text" value="hi">
  
  [type] {
    color: red;
  }
  ```

  - `[ABC="XYZ"] 속성 ABC를 포함하고 값이 XYZ인 요소

  ```css
  <input type="text" value="hi">
  
  [type="text"] {
    color: red;
  }
  ```



## 스타일 상속

- 자동상속

  - 글자/ 문자 관련 속성들은 대부분 상속된다.

- 강제상속

  - 부모요소로부터 속성값을 상속받아 사용하세요
  - 자식요소의 높이값도 200px, 색상도 orange 가 된다.

  ```css
  .parent{
    width: 300px;
    height: 200px;
    background-color: orange;
  }
  
  .child{
    width: 100px;
    height: inherit;
    background-color: inherit;
  }
  ```



## 선택자 우선순위

- 점수가 높은 선언부터 적용
- 점수가 같으면 마지막에 적용된 속성이 적용
  - 상속은 점수를 계산하지 않는다

---

![image-20210918131659030](CSS.assets/3.png)

---

![image-20210918132103309](CSS.assets/4.png)

---



## CSS 속성

#### width, height

- auto (default)
- px, em ,vw

#### max-width, max-height, min-width, min-height

- none (max default) / 0 (min default)
- auto
- px, em, vw, vh



#### 단위

- px
- % (부모요소의 대비)상대적 백분율

---



- em (부모 또는 조상요소 대비) 요소의 글꼴 크기 : 1em 기준 -> 헷갈린다.
- rem 루트요소(html)의 글꼴 크기 : 기본 16px
  - html { font-size: 16px;}
  - 편리하게 관리 가능
- vw 뷰포트 가로 너비의 백분율 : 50vw 는 화면의 절반 차지
- vh 뷰포트 세로 너비의 백분율 : 50vh 는 화면의 절반 차지



#### 마진(외부 여백)

- margin: top, bottom / left,right;
- margin: top / left,right / bottom;
- margin: top / right / bottom / left;

- 음수 사용 가능



#### 패딩(내부여백)

- 단위 % : 부모요소의 가로너비 대비 
- 여백이 추가된 만큼 요소의 크기가 늘어난다



#### 테두리

- `border: border-width border-stype border-color;`

- border-방향-속성 

- 요소의 크기가 늘어남

- .item { border: 10px solid black;}

  - border-width 
    - px, em, % 로 지정
    - 단축속성, 방향 존재
  - border-style
    - none(default 선없음)
    - solid
    - dashed
    - 단축속성, 방향 존재

  - border-color
    - black(default)
    - 색상
      - hex 색상코드 #000
      - rgb(255, 255, 255)
      - rgba(0, 0, 0, 0.5)
    - transparent(투명)
    - 단축속성, 방향 존재



#### 모서리 둥글게(border-radius)

- `border-radius: Npx;`
- 요소 모서리 원의 반지름이 N
- 특정 모서리
  - border-radius: 0 10px 0 0 ; => 오른쪽 상단만 둥글게



#### 크기계산(box-sizing)

- content-box : 요소의 내용으로 크기 계산(default)
- **border-box : 요소의 내용 + padding + border 로 크기 계산**(가로, 세로)



#### 넘침 제어(overflow)

요소의 크기 이상으로 내용이 넘쳤을 때 잘라냄

부모안에 자식이 더 클경우 부모에게 적용

overflow-x, overflow-y 로 개별제어 가능

- visible : 내용넘침(default)
- hidden : 잘라냄
- scroll : x,y충 스크롤바 생성
- auto : 필요한 스크롤바만 생성



#### 출력 특성(display)

![image-20210918143232314](css.assets/5.png)

- 인라인 요소 가로세로값 지정 위해 블록요소로 전환

- span {

  display: block;

  width: 100px;

  height: 30px;

  }



#### 투명도(opacity)

- `opacity: 0~1;`
  - 0.07 = 7%
  - 0.5 = 0.5 = 50%



#### 글꼴

- `font-size: 16px;`
- `font-weight : 400(normal);` // 700(bold); 글자의 두께 100~900
- `font-style: normal;` // italic; 기울기
- `line-height: 1.4;`  요소의 글꼴 크기의 배수로 지정
  - 높이는 위아래로 들어감
- `font-family: 글꼴, "글꼴2", ... , serif;`  
  - 띄어쓰기 등 특수문자 포함된 글꼴이름은 큰따옴표로 묶어야
  - 마지막에 글꼴계열 필수작성
    - serif 바탕
    - sans-serif 고딕
    - monospace 고정너비 글꼴 계열
    - cursive 필기체 계열



#### 문자

- `font-size: 16px;`

- `text-decoration: none;` underline(밑줄); line-through(중앙선);
- `text-align: left;` center;  right;
- `line-height: 100px;`
- `color: #666;`
- `text-indent: 24px;`



#### 배경

- `background-image: url("경로");`
- `background-size: 200px;` 가로세로 중 하나만 입력해도된다.
  - 단위
  - cover : 가로세로 중 더 넓은 값에 맞취짐
  - contain : 가로세로 중 더 짧은 값이 맞춰짐
- `background-repeat: no-repeat;`
  - repeat 
  - repeat-x
  - repeat-y
  - no-repeat
- `background-position: top right;` (우측 상단)
  - 방법1. 방향 ) top, bottom, left, right, center
  - 방법2. 수치 ) 좌측 상단 (0,0) 기준 x축, y축 px 설정 가능
- `background-color: #000;`
- `background-attachment:scroll;`
  - scroll : 이미지가 요소를 따라서 같이 스크롤(기본값)
  - fixed : 이미지가 뷰포트에 고정



#### 배치

- position
  - `static` 기준 없음
  - `relative` 요소 자신을 기준.  현재위치를 기준으로 우측으로 ~px, 좌측으로 ~px
    - 요소가 자기자신을 기준으로 배치되는 경우로 거의 쓰지않음
    - 원래 자기자리 지키고 있음(투명하게)
  - `absolute` 위치상 부모요소 기준
    - 부모에 relative 설정
    - 가장 많이 사용!! 
  - `fixed` 뷰포트를 기준
- 속성
  - top, bottom, right , left



- 요소 쌓임 순서
  1. 요소에 position 속성의 값이 있는 경우 위에 쌓인다.
     - static 은 값이 없다고 본다. (우선순의 최하)
  2. 1번 조건이 같은경우, z-index 속성의 숫자값이 높을수록 쌓인다.
     - **z-index** : 기본값 0
  3. 1,2 번 조건이 같을 경우, HTML의 다음 구조일수록 쌓인다.



- 특정 요소에 position 부여시(absolute, fixed) 자동적으로 블록요소가 된다.
  - `relative` 말고 `absolute`, `fixed` 인 경우!!
  - `display:block;` 을 준 것과 같다. 



## 플렉스(정렬) - 1차원 레이아웃

### container

- 움직이고 싶은 요소들의 부모 요소에 `display:flex` 적용

- 적용시 flex container가 된다

#### flex container & flex items

![image-20210918172803713](CSS.assets/6.png)



- 각 요소에 부여하는 속성이 나눠져있다.

![image-20210918172945295](CSS.assets/7.png)



## flex container 속성

- #### `display:flex;` 블록 요소와 같이 flex container 정의

  - inline-flex : 인라인 요소와 같이 flex container 정의

  ![image-20210918173145508](CSS.assets/8.png)

  ![image-20210918173431618](CSS.assets/9.png)

  

- #### `flex-direction: row;` 주축을 설정

  - row: 행 축이 주축이 되며 좌(start)에서 우(end)
  - row-reverse : 행 축이 주축이 되며 우(start)에서 좌(end)
  - column : 열 축이 주축이 되며, 위에서 아래로
  - column-reverse : 열 축이 주축이 되며 아래에서 위로

  ![image-20210918173942874](CSS.assets/13.png)

- #### `flex-wrap: nowrap;` flex items 묶음(줄바꿈) 여부 (주축 row 일 때)

  - nowrap: 묶음(줄바꿈) 없음
  - wrap : 묶음(줄바꿈) 있음

  ![image-20210918173745972](CSS.assets/12.png)

- #### `justify-content: flex-start;` 주 축의 정렬방법

  - flex-start : flex items를 시작점으로 정렬
  - flex-end : flex items를 끝점으로 정렬
  - center : flex items를 가운데 정렬

  ![image-20210918174223696](CSS.assets/15.png)

- #### `align-content: stretch;`  교차축의 **여러 줄** 정렬 방법 (주축 row 일 때)

- item이 2줄이상이고, wrap 일때, 여백있을때만 동작 (사용빈도 낮다)

  - stretch : flex items 를 교차축으로 늘림
  - flex-start : flex items를 시작점으로 정렬
  - flex-end : flex items를 끝점으로 정렬
  - center: flex items를 가운데 정렬

  ![image-20210918174535941](CSS.assets/16.png)

![image-20210918174643989](CSS.assets/17.png)

- #### `align-items: stretch;` 교차축의 **한 줄** 정렬방법

  - stretch: flex items를 교차축으로 늘림
  - flex-start: flex items의 각 줄의 시작점으로 정렬
  - flex-end: flex items를 각 줄의 끝점으로 정렬
  - center: flex items를 각 줄의 가운데 정렬

  ![image-20210918174838963](CSS.assets/18.png)

![image-20210918175002519](CSS.assets/19.png)

### 주사용방법

![image-20210918175436008](CSS.assets/20.png)



## flex items 속성

- #### `order : 0;` flex item의 순서

  - 숫자 : 숫자가 작을수록 앞에 정렬된다. 기본값 0 

  ![image-20210918175738771](CSS.assets/image-20210918175738771.png)

- #### `flex-grow: 0;` flex item의 증가 너비 비율

  - 0 : 기본값. 증가비율 없음
  - 숫자 : 증가비율
  - 증가비율 0인 요소를 제외한 나머지 공간을 어떻게 차지할것인가?

  ![image-20210918175929649](CSS.assets/image-20210918175929649.png)

  

- #### `flex-shrink: 1;` flex item의 감소 너비 비율

  - 1 : 기본값, flex container 너비에 따라 감소 비율 적용
  - 숫자 : 감소비율. **0 사용시 아이템의 실제너비 유지**
  - 주축의 가로 너비가 줄어들면 점점 줄어든다.

  ![image-20210918180301026](CSS.assets/image-20210918180301026.png)

- #### `flex-basis: auto;` flex item 공간 배분 전 기본너비

  - auto : 요소의 content 너비 (점선 사이 너비)
  - 단위 : 지정. **0 으로 설정시 기본값 없이 요소 가로넓이가 1:1:2 가 된다.**

  ![image-20210918180515898](CSS.assets/image-20210918180515898.png)

  ![image-20210918180640152](CSS.assets/image-20210918180640152.png)

​		![image-20210918180719337](CSS.assets/image-20210918180719337.png)

