## Media Query

```css
/* 가로가 700보다 크면 레드, 600이면 블루, 500보다 작으면 블랙 */
@media (min-width: 700px) {
  h2 { color: red;}
}
@media (width: 600px;) {
  h2 { color: blue;}
}
@media (max-width: 500px) {
  h2 { color: black;}
}

@media (orientation: landscape) {
  p.orientation::after { content: '가로입니다.';}
}
@media (orientation: portrait) {
  p.orientation::after { content: '세로입니다.';}
}
```



## font

- google fonts

```html
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100&display=swap" rel="stylesheet">

  <style>
    * {
      font-family: 'Noto Sans KR', sans-serif;
    }
  </style>

</head>
```



## icon

- fontawesome https://fontawesome.com/v5.15/icons?d=gallery&p=2&m=free
- bootstrap https://icons.getbootstrap.com/



## favicon

- realfavicongenerator.net



## Bootstrap Source Code 톺아보기

#### **Compiled CSS vs. Source files (SASS, SCSS)**

- SCSS : Syntatically Awesome Style Sheet, 중도
- SASS : 급진..
- source file을 쓰려면 따로 브라우저가 해석할 수 있도록 컴파일러가 필요하다. 일반 css로 바꿔줘야.

| Compiled CSS                                                 | Source Files               |
| ------------------------------------------------------------ | -------------------------- |
| 폴더 : bootstrap - 5. 1. 0 - dist                            | 폴더 : bootstrap - 5. 1. 0 |
| .rtl.css  (아랍어 등 우-좌 언어를 지원)                      | SASS                       |
| .min.css (모든 공백을 제거해 가볍게 만든 css)                | SCSS                       |
| .css.map (min.css 에러시 원본에서 몇번째 줄인지 말해주기 위한 디버깅용 파일) |                            |



## Specificity

- 우선순위(명시도)



## Naming Convention: BEM (Block, Element, Modifier)

> 어떻게 클래스 명을 지을 것인가? getbem.com/naming/ 

- 3가지 요소가 있다.
  - Block 요소 : 그 자체로 존재 가능한 요소
    - .block
  - Element : 독립적 존재가 불가하며 블록 내에 있어야 하는 요소
    - .block__elem.
  - Modifier : Block이나 Element의 상태 표시하는 요소
    - .block--(modifier)--(name)
    - .block__elem.--(modifier)-(name)

```html
<style>
  .form {}
  
  .form--theme--xmas {}
  
  .form__group {}
  
  .form__input {}
  .form__input--theme-xmas {}
  
  .form__submit {}
  .form__submit--disabled {}
</style>

<form class="form form--theme-xmas"> /* block */
  <div class="form__group"> /* element, form에 소속된 group이란 이름의 엘레먼트 */
    <label for="name">이름</label> 
    <input class="form__input form__input--theme-xmas" type="text"> /* element, form에 소속된*/
  </div>
  <div class="form__group"> /* element, form에 소속된*/
    <input class="form__submit form__submit--disabled" type="submit"> /* element, form에 소속된*/
  </div>
</form>
```
