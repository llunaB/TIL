## Media Query

```css
@media (min-width)
  
@media (width: 600px;)

@
```



## favicon

- realfavicongenerator.net



## Bootstrap Scource Code 톺아보기

#### Compiled CSS vs. Source files (SASS, SCSS)



| Compiles CSS               | Source Files        |
| -------------------------- | ------------------- |
| bootstrap - 5. 1. 0 - dist | bootstrap - 5. 1. 0 |
| rtl.css                    | SASS                |
| min.css                    | SCSS                |
| css.map                    |                     |





## BEM (Block, Element, Modifier)

- getbem.com/naming/
  - Block 요소 : 그 자체로 존재 가능
    - .block
  - Element : 독립적 존재 불가하며 블록 내에 있어야 한다. 
    - .block__elem.
  - Modifier : Block이나 Element의 상태 표시
    - .block--(modifier)--(name)
    - .block__elem.--(modifier)-(name)

```html
<style>
  .form{}
  .form--theme--xmas{}
  .form__group{}
  .form__input{}
  .form__input--theme-xmas{}
  .form__submit{}
  .form__submit--disabled{}
</style>


<form class="form form--theme-xmas">
  <div class="form__group">
    <label for="name">이름</label>
    <input class="form__input form__input--theme-xmas" type="text">
  </div>
  <div class="form__group">
    <div class="form__group">
      <input class="form__submit form__submit--disabled" type="submit">
    </div>
  </div>
</form>
```
