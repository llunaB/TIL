## #single -threaded #setTimeout #WebAPI #CallStack #TaskQueue

- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다. => T

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다. => F
  - Task Queue로 이동한 뒤에 들어간다.
  - 이벤트를 처리하는 Call Stack 이 하나이므로, 즉시 처리하지 못하는 이벤트들은 다른곳 (Web API)로 보내 처리하도록 하고, 처리된 이벤트들은 처리된 수서대로 대기실(Task queue)에 줄을 세워 놓고, Call Stack이 비면 담당자(Event Loop)가 대기 줄에서 가장 오래된(제일 앞의) 이벤트를 Call Stack으로 보낸다.
  - 그림으로 표현하면 다음과 같다.
  - **Event Loop를 기반으로 하는 동시성 모델(Concurrency model)**

![img](https://blog.kakaocdn.net/dn/BGaem/btrjGb2v8si/fk9w4PuO9KrIEMvPOWVci1/img.png)Concurrency model

**Call Stack이란?** 

- 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조

**Web API (Browser API)란?**

- Javascript 엔진이 아닌 브라우저 영역에서 제공하는 API
- setTimeout(), DOM events 그리고 AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리

**Task Queue(Event Queue, Message Queue)란?**

- 비동기 처리된 callback 함수가 대기하는 Queue(FIFO) 형태의 자료 구조
- main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지

**Event Loop**

- Call Stack이 비어 있는지 확인
- 비어있는 경우 Task Queue에서 실행 대기중인 callback 함수가 있는지 확인한다.
- Task Queue에 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 push한다.



------



## 동기함수와 비동기함수(방식)의 차이점

**동기 함수는** 요청을 보낸 후 응답을 받아야지만 다음 동작이 이루어진다. 모든 일은 순차적으로 진행되며 어떤 작업이 수행 중이라면 다음 작업은 대기하게 된다. 반면, 비동기함수는 작업이 병렬적으로 수행된다.



자바스크립트는 **single thread(싱글 스레드)**로 프로그램이 동작한다. 하지만 **비동기처리방식**을 사용하는데, 그것이 가능한 이유는 **비동기식 처리 모델인 Web API 가 엔진(웹브라우저나 Node.js)과 함께 동작하기 때문**이다. 이때 setTimeout이나 AJAX로 http 데이터를 가져오는 시간이 소요되는 일들을 처리한다.



이러한 Web API들이 자바스크립트 엔진 스레드와는 따로 비동기처리를 따로 돌면서, 콜백함수를 가지고 이벤트 루프에 들어가 처리되는대로 콜백함수를 다시 자바스크립트 엔진으로 돌려보내준다.



참고 : https://blog.metafor.kr/164



Alert의 경우 동기 함수라서, alert창을 닫기 전에는 다른 코드가 실행하지 못하도록 막는다.

Web API 를 사용하는 함수에는 내장함수 setTimeout, 웹으로 요청 보내는 비동기함수 등이 있다.



------



## 콜백 함수 Callback function

콜백 함수란 '다른 함수에 인자로 전달된 함수'이다.

외부 함수 내에서 호출되어 루틴을 완료하는데 동기식과 비동기식이 모두 사용된다.

대부분은 비동기 작업이 완료된 후 코드 실행을 계속하는 데 주로 사용된다.

비동기 작업이 완료된 후 코드 실행을 계속하는데 사용되는 경우를 비동기 콜백 (asynchronous callback)이라 한다.



------

