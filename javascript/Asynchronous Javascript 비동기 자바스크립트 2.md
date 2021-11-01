## #Promise #.then #.catch

- Promise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는 비동기 처리가 성공/실패했을 경우 전달할 인자와 함께 호출된다. => T
- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이며 .catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다 => T



## Async callbacks 비동기 콜백

백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수이다.

백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 다음 작업을 실행하거나 작업 완료를 알린다.

callback 함수를 다른 함수의 인수로 전달할 때, 함수의 참조로 인수를 전달하는 것이지 즉시 실행되는 것이 아니다.



즉, 비동기 로직을 수행할 때 특정 시점에서 호출할 수 있는 callback 함수를 사용하는 것이다.



## Callback hell

순차적으로 비동기 작업을 처리하기 위해 호출을 반복하다보면 콜백 지옥을 마주하게 된다.

이렇게 되면 디버깅이 어려워지고 코드 가독성이 떨어지므로 해결해야한다.



## Promise callbacks

Promise callback 방식을 사용하여 지옥탈출 해보자.



## Promise object

비동기 작업의 최종 완료 또는 실패를 나타내는 객체로 다음 메서드를 사용한다.



## .then()

이전 작업(promise)이 성공했을 때 수행할 작업을 나타내는 callback 함수이다.

각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받는다.

성공했을 때의 코드를 callback 함수 안에 작성한다.

## .catch()

.then이 하나라도 실패하면 동작한다.

이전 작업의 실패로 생성된 error 객체를 사용한다.

## .finally()

결과와 상관없이 무조건 지정된 callback 함수가 실행된다.

어떠한 인자도 전달받지 않으며 무조건 실행되어야 하는 절에서 활용한다.



------



## Axios

"Promise based HTTP client for the browser and Node.js"

브라우저를 위한 Promise 기반의 클라이언트로 XMLHttpRequest를 대체한다.



## Axios를 활용하여 버튼 누르면 이미지 출력되게 만들기

<!-- axios CDN을 삽입한다. -->

// axios를 사용하여 URL로 GET 요청을 보내고 Promise 객체를 받는다.

// .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.

// 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.

```javascript
<body>
  <button>댕댕이</button>
  <div class="dog-box">

  </div>
  <!-- axios CDN -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const URL = 'https://dog.ceo/api/breeds/image/random'
    const myButton = document.querySelector('button')

    // 버튼을 클릭하면, dog api로 요청을 보냄
    myButton.addEventListener('click', function () {
      axios.get(URL)
        .then(response => {
          // console.log(response.data)
          return response.data
        })
        .then(response => {
          // console.log(response.message)
          const imgUrl = response.message
          // img 태그 생성
          const newImgTag = document.createElement('img')
          // img 태그의 src 속성에 imgUrl 값 할당
          newImgTag.src = imgUrl
          // console.log(newImgTag)
          // div 태그의 자식 태그로 완성된 img 태그를 삽입
          const dogBox = document.querySelector('.dog-box')
          dogBox.appendChild(newImgTag)
        })
        .catch(error => {
          console.log(error)
        })

    })

  </script>
</body>
```



## Axious를 활용하여 버튼 누르면 게시물 불러오기 (forEach Array helper 메서드 사용)

```javascript
<body>

  <button>게시물 불러오기</button>
  <ul></ul>
  
  <!-- axios CDN을 삽입한다. -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const API_URL = 'https://jsonplaceholder.typicode.com/posts'
    
    const btn = document.querySelector('button')
    btn.addEventListener('click', function () {
      // get 요청 보내기
      axios.get(API_URL)
        // .then(() => {})
        .then((res) => {
          const posts = res.data

          // posts.forEach(() => {})
          posts.forEach((post) => {
            const li = document.createElement('li')
            li.innerText = post.title
            document.querySelector('ul').appendChild(li)
          })
        })

    })


  </script>
</body>
```



## 같은 기능, 다른 표현방식

![img](https://blog.kakaocdn.net/dn/KA1Ip/btrjyInHs6P/OtUt1zzapcYzuMh9hi6m5K/img.png)