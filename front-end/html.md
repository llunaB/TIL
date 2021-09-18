# HTML

- 한국어 설정

```html
<html lang="ko">
```

- link
  - `rel` 가져올 문서와의 관계 (reference)
  - `href` 가져올 문서의 경로 (hypertext reference)
    - favorite icon => `favicon`

```html
  <link rel="stylesheet" href="./main.css">
  <link rel="icon" href="./favicon.png">
```

- 자바스크립트 가져오는 2가지 방식
  - source => `src`

```html
 <script src="./main.js"></script>
 <script>
    consol.log('Instagram!')
 </script>
```

- 메타태그 : 제작자, 내용 키워드 등 검색엔진이나 브라우저에게 제공
  - `charset` 문자인코딩 방식
  - `name`  정보의 종류
  - `content` 정보의 값

```html
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```



- 이미지

  - altertnate => `alt` 필수속성 대체텍스트

  

## 경로

![image-20210918103325781](HTML.assets/1.png)

- 상대경로
  - `	./` 주변 (생략가능)
  - `../` 상위폴더
- 절대경로
  - `http` 절대경로
  - `/` 루트경로



## 로컬호스트

- 포트번호로 구분

- ```
  http://localhost:5500/
  ```

  

## 프로젝트 경로

- http://localhost:5500/
- 루트 경로 내에 images, css, index.html 이 있다.
- my-project
  - images
    - logo.png
  - css
    - main.css
  - index.html



## 경로의 생략

- 브라우저는 자동으로 `index.html` 을 찾기 때문에 폴더명만 입력해도 된다.

```html
<a href="/about/index.html">About</a>
<a href="/about">About</a>
```

```
http://localhost:5500/about/
```

- 메인페이지로 이동하는 링크

```html
<a href="/">Home</a>
```



## 모든 파일 공백크기 2로 설정

- `cmd + shif + key` > 설정 > 탭사이즈

![image-20210918103325781](HTML.assets/2.png))



## 간단한 코드 테스트

- codepen.io
- body 내부 요소만 넣는다.

![image-20210918103325781](HTML.assets/3.png)



## 브라우저 스타일 초기화

- https://www.jsdelivr.com/package/npm/reset-css

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css">
```

- codepen

![Screen Shot 2021-09-18 at 11.08.38 AM](HTML.assets/4.png)



## HTML 핵심정리

#### 부모와 자식 관계의 이해

- 내 바로 위아래 : 부모/자식 요소
- 내 위 전부, 내 아래 전부 : 조상/자손 요소



### 빈 태그?

- 빈 태그의 경우 내용을 알 수 없어 속성이 필수이다.

```html
 <input type="text"/>
```

- 표현방식
  - <태그>
    - HTML 1/2/3/4/5
    - 편리하다.
  - <태그/> 
    - XHTML / HTML5
    - 빈 태그임을 인지하기 쉽다. 안전하다.(권장)



### 태그구조

- 빈 태그
  - <태그 속성 = "값" 속성 = "값"/>
- 태그
  - <태그 속성 = "값" 속성 = "값"> 내용 </태그>



### 글자와 상자

- 인라인 요소 (글자)
  - 수평으로 쌓인다.
  - 포함한 콘텐츠 만큼 늘거나 줄어든다.
  - 글자요소는 가로와 세로**사이즈 지정이 불가능하다.**
  - 요소의 내외부 여백에서 위아래는 적용되지 않으며 **좌우 여백만 적용된다.**
  - 자식요소로 블럭요소를 가질 수 없으며 인라인 요소만 가능하다.
    - span
      - span 태그 하나가 글자처럼 취급되므로 줄바꿈시 중간에 띄어쓰기 발생
- 블록 요소 (상자)
  - 수직으로 쌓인다.
  - 부모 요소의 크기만큼 자동으로 늘어난다. (가로)
  - 포함한 콘텐츠 크기만큼 자동으로 줄어든다. (세로)
  - 가로와 세로너비 지정이 가능하다.
  - 외내부 여백 지정이 가능하다.
  - 자식으로 또다른 블록과 인라인 요소를 포함할 수 있다.



### 핵심요소 정리

- `div` : division 의미없는 구분요소 / 블록

- `h1~6` : heading 제목의미 / 블록

- `p` : paragraph 문장의미 / 블록

- `img` : image 이미지삽입 / 인라인 / 필수속성 `src`, `alt`

- `ul`, `li` : 순서가 필요없는 목록의 집합, 목록 내 각 항목 / 블록

- `a` : ancher 하이퍼링크 지정요소 / 속성 `href`, `target`

  - target="_blank" : 새로운 탭으로 열림

  ```html
  <a href="https://naver.com" target="_blank">NAVER</a>
  ```

  

- `span` : 의미없는 구분요소 / 인라인

- `br/` :  break 줄바꿈 / 인라인

- `input` : 데이터 입력요소 / 인라인-블록요소

  - 글자요소처럼 왼쪽에서 오른쪽으로 쌓이지만 가로세로값, 여백 가질 수 있다.

  - type="text"

    - value="미리입력된 값"
    - placeholder="사용자가 입력할 값의 힌트"
    - disabled

  - type="checkbox"

    - ![image-20210918115953214](HTML.assets/5.png)

    - ```html
      <label>
        <input type="checkbox"/> Apple
      </label>
      <label>
        <input type="checkbox" checked/> Banana
      </label>
      ```

  - type="radio"

    - 같은 `name`으로 묶어 택1 그룹을 만든다.

    - ![image-20210918115853049](HTML.assets/6.png)

    - ```html
      <label>
        <input type="radio" name="fruitss"/> Apple
      </label>
      <label>
        <input type="checkbox" name="fruits"/> Banana
      </label>
      ```

    

- table  : 테이블 요소 / 블록

  - table row /  table data

  - A B 

    C D

  - ![image-20210918120415086](HTML.assets/7.png)

  - ```html
    <table>
      <tr>
        <td>A</td><td>B</td>
      </tr>
      <tr>
        <td>C</td><td>D</td>
      </tr>
    </table>
    ```



## 주석

- 단축키

 ```
 cmd + /
 ```

  

## 전역속성

- 각 요소는 사용할 수 있는 속성이 있지만, 모든 바디 내 태그 요소가 사용하는 속성이 있다.
- `title` : 요소의 정보나 설명을 지정, 마우스오버시 툴팁으로 출력
- `style` : 요소에 적용할 스타일을 지정
- `class` : 요소를 지칭하는 중복가능한 이름
- `id` : 요소를 지칭하는 고유한 이름
- `data-이름="데이터"` : 요소에 데이터를 지정, 자바스크립트에서 활용

