# Computed vs. Method

- 둘 다 데이터를 변경시키는(계산하는) 속성

```vue
<body>
  <div id="app">
    <p>원본 메시지: "{{ message }}"</p>
    <p>computed: "{{ reversedMessageComputed }}"</p>
    <p>methods: "{{ reversedMessageMethod() }}"</p>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: '안녕하세요'
      },
      computed: {
        reversedMessageComputed: function () {
          return this.message.split('').reverse().join('')
        }
      },
      methods: {
        reversedMessageMethod: function () {
          return this.message.split('').reverse().join('')
        }
      }
    })
  </script>
</body>
```

- 함수의 형태로 정의하지만 함수의 반환 값이 바인딩된다.
- `computed` 의 경우 종속된 데이터 (message) 이 변경될 때만 함수를 실행하기 때문에 종속 데이터가 변경되지 않는 한, 함수를 여러 번 호출해도 계산을 다시 하지 않는다.  따라서 호출하는게 아니라 이미 계산된 값을 사용.
- 반면 `methods`를 호출( )하면 렌더링 할때마다 함수를 매번 실행한다.

# watch

- 데이터가 변경되었을 때 (다른 데이터를 바꾸기 위해) 함수를 실행한다.

- `num` 이라는 감시하는 데이터로 함수명을 정의
- computed가 특정 데이터를 다른 값으로 만든다면, watch는 그 값의 변화를 통해 다른 데이터를 변경시킨다.

