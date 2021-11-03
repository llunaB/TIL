# Vue.js

- 사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크
- 현대적 tool과 다양한 라이브러리로 **SPA(Single Page Application)** 을 완벽하게 지원한다.

# SPA

싱글페이지라 url이 아닌 클릭을 통해 화면을 바꾼다.

이를 보완하기 위한 라이브러리가 존재한다.

# SSR vs CSR

서버사이드에서 렌더링, 클라이언트에서 렌더링하느냐가 차이이다.

Vue.js의 경우 SSR을 지원하는 **SEO 대응 기술**이 존재한다.

- Nuxt.js : Vue.js 응용 프로그램을 위한 프레임워크로 SSR 지원
- Next.js : React.js 응용 프로그램을 위한 프레임워크로 SSR 지원

# Vue.js 역할

- Server 사이드에서 Django 서버는 MTV 중 데이터베이스만 조작한다.
- Client 사이드에서 Vue 서버는 템플릿 역할을 하며 Django에서 데이터를 받아오고, 사용자 데이터를 Django로 넘긴다.

# Why Vue.js?

왜 사용할까?

### 데이터 바인딩 개념

기존 자바스크립트에서는 여러 요소의 경우 for문을 돌면서 각각 li 태그를 만들고 데이터를 만들고, 다시 부모태그에 넣었다.

뷰에서는 li 태그를 미리 만들고 데이터를 넣으면 자동으로 넣어서 태그를 자동으로 생성한다. 이것이 데이터 바인딩!!

# MVVM Pattern

![image-20211103124705483](/Users/euijinpang/TIL/Vue.js.assets/image-20211103124705483.png)

View의 model은 하나의 obeject이며 그 안에 데이터가 들어간다.

View는 DOM과 연결되며 ViewModel이 중재한다.

즉, Model 데이터가 수정되면 자동으로 View 가 변경되는 것이다!

Model <===> View

# Eslint

https://eslint.org/

javascript 디버깅 도구 (ex. v-for 사용시 key 속성 필수 작성)



# v-bind 통한 데이터 변수화



# v-model 통한 양방향 바인딩

HTML 요소와 input 값을 양방향 바인딩

model은 사용자가 입력하는 input에만 사용하며, 사용자가 입력하는 데이터를 저장한다.



# v-on 통한 이벤트 등록





# computed vs. watch

- 둘 다 종속된 데이터가 변해야만 실행된다.
- computed 는 특정 데이터를 직접 다른 값으로 만들 때 사용 (선언형 프로그래밍)
  - "특정 값이 변동하면 해당 값을 다시 계산해서 보여준다."
  - ""계산해야 하는 목표 데이터를 정의""
  - a자체를 변화.
  - 반드시 return 필요.
- watch 는 변화 상황에 맞추어 특정 데이터(감시데이터)를 지정하고 변화가 발생하면 다른 data를 바꿀 때 사용
  - watch는 명칭을 지정 (명령형 프로그래밍 방식)
  - "특정 값이 변동하면 다른 작업을 한다." 특정 대상 변경시 콜백 함수 실행
  - "데이터가 바뀌면 특정 함수를 실행"
  - a를 건드리지 않음.
  - 반드시 return이 필요한 것은 아님.

![image-20211103152548469](/Users/euijinpang/TIL/Vue.js.assets/image-20211103152548469.png)

