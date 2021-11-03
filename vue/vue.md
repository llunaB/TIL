# **CSR**

![image-20211103101209990](/Users/euijinpang/Library/Application Support/typora-user-images/image-20211103101209990.png)

![image-20211103110910180](/Users/euijinpang/Library/Application Support/typora-user-images/image-20211103110910180.png)

![image-20211103112000570](/Users/euijinpang/Library/Application Support/typora-user-images/image-20211103112000570.png)



# v-show vs. v-if

### show는 렌더링을 하고 false에선 display-none으로 가림, v-if는 애초에 렌더링을 하지 않는다.

show 는 처음엔 비싼데 나중엔 토글비용 적다.

v-if는 처음엔 렌더링 비용 싼데 토글에서는 다시 렌더링 해야하므로 비용 증가 ex. 로그인-로그아웃시 서로 다른 네비게이션 바 보여주기 (If-else 분기처리)



쿼리셀렉터를 표면적으로 사용하지 않는다.

이벤트리스너는 onclick으로 대체한다.



# 데이터 => 메소드 => 출력

데이터를 관리한다.

메소드로 데이터를 동작시킨다. 

메소드를 출력한다.

# 단방향

데이터 변경하면 출력값(html 코드)도 변한다. 반대로 html 바꿨다고 data가 바뀌지는 않는다.



# webpack

여러 javascript 파일들을 풀어서 분리해주는 서비스

변수 충돌 등을 막을 수 있음(axios 불러오면 axios변수 사용 불가)

![image-20211103140954500](/Users/euijinpang/TIL/vue.assets/image-20211103140954500.png)

![image-20211103142212428](/Users/euijinpang/TIL/vue.assets/image-20211103142212428.png)

# v-bind:key  -> :key 로 생략

# v-model 을 통한 양방향 binding

- 단, 언어가 영어가 아닌 한중일 경우 따로 이벤트-메서드 제작
- https://kr.vuejs.org/v2/guide/forms.html

![image-20211103150723192](/Users/euijinpang/TIL/vue.assets/image-20211103150723192.png)

# computed vs. methods

- computed는 `이미 계산된 값`을 사용하므로 {{ computed }} 로 사용
  - 종속된 데이터값이 변화되어야만 실행된다.
- methods는 함수 호출이므로 {{ method() }} 로 사용
- 각각 필요한 경우가 있다.



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

![image-20211103152548469](/Users/euijinpang/TIL/vue.assets/image-20211103152548469.png)





![image-20211103153146638](/Users/euijinpang/TIL/vue.assets/image-20211103153146638.png)

![image-20211103153339197](/Users/euijinpang/TIL/vue.assets/image-20211103153339197.png)

![image-20211103153703970](/Users/euijinpang/TIL/vue.assets/image-20211103153703970.png)

![image-20211103153715262](/Users/euijinpang/TIL/vue.assets/image-20211103153715262.png)

미리 계산된 결과를 만들어놓고(조건), 돌려라!
if for 같이 쓰지 말라~~

![image-20211103160415180](/Users/euijinpang/TIL/vue.assets/image-20211103160415180.png)

![image-20211103171510310](/Users/euijinpang/TIL/vue.assets/image-20211103171510310.png)

![image-20211103171550308](/Users/euijinpang/TIL/vue.assets/image-20211103171550308.png)

created 가장 많이 사용! ajax 불러올 때 초기 기본값 설정시 사용

