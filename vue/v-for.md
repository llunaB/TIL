# v-for

![image-20211110205806902](/Users/euijinpang/TIL/v-for.assets/image-20211110205806902.png)

```vue
<!-- 배열 순회 -->
<div v-for="(fruit, index) in fruits" :key="`fruit-${index}`">
  {{ fruit }}
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      fruits: ['apple', 'banana', 'coconut'],
    },
  })
</script>

```

![image-20211110205751692](/Users/euijinpang/TIL/v-for.assets/image-20211110205751692.png)

```vue
<!-- 배열 안의 요소가 객체일 때 -->
<div v-for="todo in todos" :key="todo.id">
  {{ todo.title }} = {{ todo.completed }}
</div>

<script>
  const app = new Vue({
    el: '#app',
    data: {
      todos: [
        { id: 1, title: 'todo1', completed: true},
        { id: 2, title: 'todo2', completed: false},
        { id: 3, title: 'todo3', completed: true},
      ],
    },
  })
</script>
```

![image-20211110205713732](/Users/euijinpang/TIL/v-for.assets/image-20211110205713732.png)

```vue
<!-- 객체 순회 -->
<div v-for="value in myObj" :key="key">
  {{ value }}
</div>
<div v-for="(value, key) in myObj" :key="key">
  {{ value }}
</div>
<div v-for="(value, key) in myObj" :key="key">
  {{ key }} : {{ value }}
  
<script>
  const app = new Vue({
    el: '#app',
    data: {
      myObj: {
        name: 'kim',
        age: 50,
      }
    },
  })
</script>
```

