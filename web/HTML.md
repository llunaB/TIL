# HTML

웹페이지가 어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어

### <u>**Wen Documents - MDB Web Docs**</u>

https://developer.mozilla.org/ko/



## Setting

##### Chrome Developor Tool

- Elements : DOM 탐색 및 CSS 확인 및 변경
  - Style : 요소에 적용된 CSS 확인 및 변경
  - Computed : 스타일이 계산된 최종 결과
  - Event Listeners : 해당 요소에 적용된 이벤트
- Sources, Network, Performance, Application, Secutiy, Audits 등

##### VS extension

- open in browser
- auto rename tag
- highlight matching tag



## 웹 표준 : WHATWG

- from W3C to **WHATWG**

- https://whatwg.org/



## Browser

- Can I use? https://caniuse.com/



## HTML : **Hyper Text Markup Language**

웹 페이지를 작성하기 위한 언어. 웹 콘텐츠의 **'의미' 와 '구조'** 를 정의

- Hyper? : 텍스트 등 정보가 동일 선상에 있는 것이 아니라 다중으로 연결된 상태!
- Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접속할 수 있는 텍스트
- HTTP & HTML



## HTML 기본구조

- html
  - Head
  - Body
    - header
    - section
    - footer

  

#### Open Graph Protocol

메타태그 등 다양한 기능을 <head></head>에 넣을 수 있다.

- https://metatags.io/



#### DOM(Document Object Model) 트리

HTML은 DOM 구조로 이루어진다. 부모 관계, 형제 관계

각 태그를 별도의 객체라고 할 수 있다.

<img src="html.assets/1.png">



#### 요소(element)

- 태그는 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 열고 닫는 태그로 구성, (모두 그런 것은 아니다)
- 내용이 있는 태그와 없는 태그
  - 있다
  - 없다 : br, img, hr, input, link, meta



#### 속성(attribute)

- 태그 내에 사용하며 태그 별로 다르다
  - `href` - 속성명
  - `https://google.com` - 속성값

```html
<a href="https://google.com">

# = 양 옆 공백없이!
# 쌍따옴표 사용!
```

- 태그 상관없이 사용하는 HTML Global Attribute

```bash
id, class / hidden / lang / style / tabindex / title
```



#### HTML 예시

```html
<!DOCTYPE html>
<html>
  
  <head>
    <meta charset="UTF-8">
    <title>타이틀입니다.</title>
  </head>
  
  <body>
    <h1>
      h1입니다.
    </h1>
    <!-- 이것은 주석입니다 -->
    <a href="https://google.com"> 구글로 고고!
    </a>
  </body>
  
</html>
```



#### 시맨틱 태그 - div를 구분한 개념

의미를 담은 구조만 잡는 태그

- **검색엔진 최적화(SEO)를 위해 메타태그, 시맨틱 태그 쓰려는 노력 해야**
- Non semantic (div, span) / **Semantic (h1, table)** 
- 가장 잘 활용한 경우? 구글 뉴스! https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko
- 예시

```
header : 문서 전체나 섹션의 헤더
nav : 네비게이션
aside : 사이드 공간
section : 문서의 일반적인 부분, 컨텐츠의 그룹
article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
footer : 푸터
```

<img src="html.assets/2.png">

 

------



## HTML 문서 구조화

#### Inline & Block

- `<span> vs <div>`



#### group

- `<p>, <hr>, <ol>,<ul>, <pre>, <blockquote>, <div>`



#### text

- `<a>`
- `<b> vs <strong>` : 둘 다 굵게 하지만 strong은 실제 의미까지 강조**, `<strong>`의 경우 웹 접근성 강조**
  - 네이버 널리 : https://nuli.navercorp.com/
- `<i> vs <em>`
- `<span>,<br>,<img>`



#### table

- <tr>, <td>, <th>
- <thead>, <tbody>, <tfoot>
- <caption>
- colspan, rowspan
- scope 속성
- <col>, <colgroup>



#### form - 중요!!!

- 서버에서 처리될 데이터를 제공하는 역할
- 기본 속성
  - action : 어디로 데이터를 보낼 것인가?
  - method

##### input tag - form 내에 들어간다

- https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input 다양한 input type 확인!
- <label> 서식 입력 요소의 캡션
- <input> 공통 속성
  - name, placeholder
  - required
  - autofocus
- type에 따라 각 동작이 달라진다

```html
<!DOCTYPE html>
<html>
  
  <head>
    <meta charset="UTF-8">
    <title>타이틀입니다.</title>
  </head>
  
  <body>
    <header>
      <a>
        <img scr="" alt="main.img">
      </a>
      <h1>SSAFY 학생 건강설문</h1>
    </header>
    <section>
      <!-- action은 반드시 있어야 한다. -->
      <form action="#">
        <div>
          <!-- label은 for 와 input tag의 id를 연결하여, 이 태그가 무엇을 가리지는지 보여줌 -->
          <label for="name">이름을 기재해주세요.</label><br>
          <!-- 창 접속시 자동 커서 - autofocus -->
          <input type="text" id="name" name="name" autofocus>
        </div>
        <hr>
        <div>
          <label for="region">지역을 선택해주세요.</label><br>
          <!-- required는 필수, 안눌렀을 경우 제출안됨 -->
          <select name="region" id="region" required>
            <option value="">선택</option>
            <option value="서울">서울</option>
            <option value="대전">대전</option>
            <!-- disabled 선택 안됨 -->
            <option value="부울경" disabled>부울경</option>
          </select>
        </div>
        <hr>
        <!-- input type "radio" -->
        <div>
          <p>오늘의 체온을 선택해주세요.</p>
          <!-- 미리 선택되어있게 checked 라는 속성값을 준다. -->
          <input type="radio" name="body-heat" id="normal" value="normal" checked>
          <!-- label 태그 -->
          <label for="normal">37도 미만</label><br>
          <input type="radio" name="body-heat" id="warning">
          <label for="warning">37도 이상</label><br>
        </div>
        <hr>
        <!-- submit 이 있어야 제출가능 -->
        <input type="submit" value="제출">
      </form>
    </section>
    <footer>

    </footer>

  </body>
  
</html>
```
