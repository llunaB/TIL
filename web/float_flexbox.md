# float & flexbox

## float

- float 을 주면, **텍스트와 인라인 요소**는 옆으로 배치된다.
- **단, 블록 요소는 겹쳐진다. 레이아웃이 망가진다!!**

![image-20210804093619261](/Users/euijinpang/TIL/web/css2.assets/image-20210804093619261.png)

![image-20210804093033770](/Users/euijinpang/TIL/web/css2.assets/image-20210804093033770.png)

## float clear

- float 된 요소의 **부모 요소**에 가상의 막을 만들기
- 이때, **부모 요소**는 `class`를 `clearfix`로 정한다!

- `.clearfix::after {}`
- `::after` : 선택 요소의 마지막 자식으로 가상 요소를 하나 생성한다. 기본값은 인라인이다. 
- `clear` : float 된 요소를 무시한다. `clear: both;` 를 사용

```css
<head>
  <style>
    .left {
      float: left;
    }
    
    /* 내용은 비어있고, 블록 속성을 가진 가상의 벽을 만든다 */
    /* ::after의 기본은 Inline이므로 block요소로 바꿔준다. */
    .clearfix::after {
      content: "";
      display: block;
      clear: both;
    }
  </style>
</head>

<body>
  <div class="clearfix">
    <div class="box1 left">div</div>
    <!-- ::after -->
  </div>
  <!-- 가상의 요소 -->
  <div class="box2">div</div>
</body>
```

![image-20210804093211363](/Users/euijinpang/TIL/web/css2.assets/image-20210804093211363.png)



## flexbox (CSS Flexible Box Layout)

- 오랫동안 CSS Layout을 작성할 수 있는 도구는 float와 positioning 뿐이었다.
- `Flexbox`라 불리는 Flexible Box module은 flexbox 인터페이스 내의 아이템 간 **1) 공간 배분 2) 정렬** 기능을 제공
- 요소 간 <u>1차원 단방향 레이아웃</u>
- **정렬하려는 부모 요소에 작성**
- start와 end는 어디서 시작하느냐의 차이로, 오른쪽에서 시작시 start는 오른쪽이다.

```css
.flex-container {
  diaplay:flex;
  /* inline-flex는 아이템 사이즈만큼만 부모요소 정해짐, flex 영역을 인라인 블록으로 사용 */
}
```



## 요소와 축

### 요소

- Flex Container (부모 요소)
  - Flex Item들이 놓여있는 영역
  - 생성하려면 display 속성을 flex or inline-flex로 지정
  - <u>**부모가 아이템을 정렬한다!!!**</u>
- Flex Item (자식 요소)

### 축 

- main axis (메인 축)
  - X, Y축 관계없이, 기본은 row
- cross axis(교차 축)

![image-20210804100003735](/Users/euijinpang/TIL/web/css2.assets/flebox.jpg)

```css
.flex-container {
  
        /* 1. 정렬하고자 하는 부모 요소(flex container)에 선언 */
      display: flex; Default
  		display: inline-flex;
  
        /* 2. 메인축 방향 설정 */
      flex-direction: row; Default 요소들을 텍스트의 방향과 동일하게 정렬합니다.
      flex-direction: row-reverse; 요소들을 텍스트의 반대 방향으로 정렬합니다.
      flex-direction: column; 요소들을 위에서 아래로 정렬합니다.
      flex-direction: column-reverse; 요소들을 아래에서 위로 정렬합니다.
    
      	/* 5. 메인축 정렬 */
      justify-content: flex-start; Default (reverse 시 오른쪽 정렬)
  		justify-content: center; 요소들을 컨테이너의 가운데로 정렬합니다.
 		  justify-content: flex-end; 요소들을 컨테이너의 오른쪽으로 정렬합니다. (reverse 																 시 왼쪽 정렬)
  		justify-content: space-between; 요소들 사이에 동일한 간격을 둡니다. 양옆으로!
  		justify-content: space-around; items 사이의 간격이 items 양옆 간격의 2배 																			 요소들 주위에 동일한 간격을 둡니다.	
  		justify-content: space-evenly; items 사이의 간격이 items 양옆 간격과 동일
    
      	/* 6. 교차축 정렬 */
  		/* 이 CSS 속성은 다음의 값들을 인자로 받아 요소들을 cross 상에서 정렬합니다.*/
  		/* 컨테이너 안에서 모든 요소의 정렬 */
      align-items: stretch; Default 요소들을 컨테이너에 맞도록 늘립니다
  		align-items: flex-start; 요소들을 컨테이너의 꼭대기로 정렬합니다.
  		align-items: center; 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
  		align-items: flex-end; 요소들을 컨테이너의 바닥으로 정렬합니다.
  		align-items: baseline; 요소들을 컨테이너의 시작 위치에 정렬합니다.
  
        /* 3. item들이 강제로 한 줄에 배치되게 할 것인지에 대한 여부 결정 */
      flex-wrap: nowrap; Default 모든 요소들을 한 줄에 정렬합니다.
  		flex-wrap: wrap; 요소들을 여러 줄에 걸쳐 정렬합니다.
  		flex-wrap: wrap-reverse; 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.
  
        /* 4. flex-direction + flex-wrap 의 shorthand */
      flex-flow: column wrap; 

  
  			/* align content */ 여러 줄 사이의 간격을 지정 한 줄만 있는 경우, align-content는 효과를 보이지 않습니다.
  		align-content: flex-start;  여러 줄들을 컨테이너의 꼭대기에 정렬합니다. 
  		align-content: flex-end; 여러 줄들을 컨테이너의 바닥에 정렬합니다.
  		align-content: center; 여러 줄들을 세로선 상의 가운데에 정렬합니다.
  		align-content: space-between; 여러 줄들 사이에 동일한 간격을 둡니다.
  		align-content: space-around; 여러 줄들 주위에 동일한 간격을 둡니다.
  		align-content: stretch; 여러 줄들을 컨테이너에 맞도록 늘립니다.
  		
        /* 7. 교차축 개별 정렬 */
      .item1 {
      align-self: flex-start;
      align-self: flex-end;
        
        /* order: 값이 작을수록 앞으로 정렬 (기본값 0) */
      order: 0;

    
        /* 메인 축에서 남은 공간을 각 항목에게 분배
        남은 공간에 대한 배분 - 1, 2 라면 남은 공간을 1:2 로 나눔 */
      flex-grow : 0; Default
      }

      .item2 {
        /* align-self: center; */
        /* order: -1; */
        /* flex-grow:2; */
      }

      .item3 {
        /* align-self: flex-end; */
        /* order: 1; */
        /* flex-grow:3; */
        /* margin-left: auto; */
      }

      .sizeup {
        font-size: 150px;

      }
  
  align-content: flex-start;
  
	align-content: flex-end;
  
  flex-direction: column-reverse;
	align-content: center;
  
  flex-direction: column-reverse;
	flex-wrap: wrap-reverse;
	justify-content: center;
	align-content: space-between;

}
```





## Flex에 적용되는 속성

### 배치 방향 설정

- **flex-direction** 

![flex-direction](/Users/euijinpang/TIL/web/css2.assets/flex-direction.jpg)

### 메인축 방향 정렬

- **justify-content**, **(magin auto)**

### 교차축 방향 정렬

- **align-items, align-self, align-content**

![justify&align](/Users/euijinpang/TIL/web/css2.assets/justify&align.jpg)

### 기타

- **flex-wrap : 요소들이 강제로 한 줄에 배치 여부**
  - nowrap
  - wrap
  - wrap-reverse
- **flex-flow : flex-direction 과 flex-wrap의 shorthand**
  - ex) flex-flow : row nowrap;
- **flex-grow : 주축에서 남는 공간을 비율로 분배, 기본값 0**
- **order : 작은 숫자일수록 앞으로 이동, 기본값 0**



### content & items & self

- content : 여러 줄
- items : 한 줄
- self : flex item 개별 요소



### examples

- **justify-content : 메인 축 기준 여러줄 정렬**
  - flex-start : 시작 지점부터 차례로 쌓임, 기본값
  - flex-end : 쌓이는 방향이 뒤쪽부터 시작(역순은 아님)
  - center : 정중앙
  - space-between : 죄우정렬 (아이템 간 간격 동일)
  - space-around : 균등 좌우 정렬 (내부요소 여백은 외곽 여백의 2배)
  - space-evenly : 균등 정렬 (내부 요소와 외각 여백 모두 동일)
- **align-items : 교차축 기준 한 줄 정렬**
  - stretch : 기본값, 컨테이너를 가득 채움
  - flex-start : 위
  - flex-end : 아래
  - center : 가운데
  - baseline : 아이템 내부 text 에 기준선 맞춤
- **align-self : 교차축 기준 선택 개별요소 정렬**
  - auto : 기본값
  - flex-strart 
  - flex-end
  - center
  - baseline
  - stretch
- **align-content : 교차축 기준 여러줄 정렬**
  - flex-start / flex-end / center / stretch / space-between / space-around



