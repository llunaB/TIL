# Lifecycle Hooks

- 각 Vue instance 는 생성시 초기화 단계를 거치는데 이럴 때 사용자 정의 로직을 실행할 수 있다.

# created

- application의 초기 데이터를 API 요청을 통해 불러올 수 있다.
- 하단 코드를 보면 따로 버튼을 누르거나 사용자가 동작을 하지 않더라도 페이지를 열자마자 `created` 부분이 실행되면서 `getImg()` 메서드가 실행되고 이에 따라 `axios`  가 동작, 이미지 주소를 불러와서, 최종적으로 DOM에서 이미지가 출력된다. 

```vue
<body>
  <div id="app">
    <img v-if="imgSrc" :src="imgSrc" alt="sample img">
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const API_URL = 'https://dog.ceo/api/breeds/image/random'
    const app = new Vue({
      el: '#app',
      data: {
        imgSrc: '',
      },
      methods: {
        getImg: function () {
          axios.get(API_URL)
            .then(response => {
              this.imgSrc = response.data.message
            })
        }
      },
      // vue의 instance가 생성된 직후
      created: function () {
        this.getImg()
      }
    })
  </script>
</body>
```



# 자주 쓰는 hooks

- ## beforeCreate

- ## created

- ## beforeMount

- ## beforeUpdate

![Instance lifecycle hooks](https://v3.vuejs.org/images/lifecycle.svg)