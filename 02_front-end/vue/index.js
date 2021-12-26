var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

app.message = 'data changed!'

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: new Date().toLocaleString(),
    isRed: true,
    isActive: true,
    fontSize: 30,
  }
})

var app3 = new Vue({
  el: '#app-3',
  data: {
    show: false,
    seen: true,
    myType: 'A',
    isButtonDisabled: true,
  }
})

// app3.seen = false

var app4 = new Vue({
  el: '#app-4',
  data: {
    myStr: 'Hello World!',
    fruits: ['apple', 'banana', 'coconut'],
    todos: [
      { text: 'Learn Javasvcipt' },
      { text: 'Learn Vue' },
      { text: 'Learn Build somethig awesome' }
    ]
  }
})

var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'hihi vue',
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})

var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Hello~',
    message_kor: '',
  },
  methods: {
    oninputChange: function (event) {
      console.log(event)
      this.message_kor = event.target.value
    }
  }

})

Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>',
})

var app = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      {id: 0, text: 'vegi'},
      {id: 1, text: 'cheese'},
      {id: 2, text: 'any'}
    ]
  }
})

var app = new Vue({
  el: '#app-8',
  data: {
    myHtml: '<b>Hello</b>'
  }
})

var app = new Vue({
  el: '#app-9',
  data: {
    isChecked: true,
    num: 10,
  },
  computed: {
    doublenum: function() {
      return this.num * 2
    },
  },
  methods: {
    doublenumMethod: function() {
      return this.num * 2
    },
    add: function() {
      console.log(this.num)
      return this.num += 1
    }
  },
  watch: {
    num: function() {
      console.log(`${this.num}이 변경되었습니다.`)
    }
  }
})

var app = new Vue({
  el: '#app-10',
  data: {
    numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
  },
  // 필터를 computed로 대체
  computed: {
    getOddNums: function () {
      let oddNum = []
      this.numbers.forEach(element => {
        if(element % 2 == 1) {
          oddNum.push(element)
        }
      })
      return oddNum
    },
    getUnderTenNums: function () {
      let underTenNum = []
      this.numbers.forEach(element => {
        if(element <= 10) {
          underTenNum.push(element)
        }
      })
      return underTenNum
    }
  },

})