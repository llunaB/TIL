

# Vue CLI 환경 설치

- 설치 (나는 euiinpang에 설치함) vue2 로 진행

https://cli.vuejs.org/guide/

```bash
npm install -g @vue/cli
```

- 확인

```bash
vue --version
```

- 프로젝트 생성

```bash
vue create my-first-app
```

- 가상환경 설정하지 않으며 해당 프로젝트 안으로 들어가서 작업해야 한다.

```bash
cd <app name>
```

- 실행

```bash
npm run serve
```

# Vue Router

- 환경 맞추기 : 기존 package-lock.json기반으로 노드 모듈 생성

```bash
npm i
```

- Vue Router plugin 설치 - 커밋여부 y - 히스토리 사용여부 y

```bash
vue add router
```

- lodash 설치

```bash
npm install lodash
```



- 모듈 1개 = 스크립트 1개



package-lock.json 을 통해 node_modules 설치!

git에 올릴 때, node_modules는 올리지 않는다.(파일 엄청 크다)

# props 이름 컨벤션

- during declaration (선언시) - camelCase
- in template(HTML) - kebab-case



![image-20211108131558723](/Users/euijinpang/TIL/vue_cli.assets/image-20211108131558723.png)

![image-20211108131915628](/Users/euijinpang/TIL/vue_cli.assets/image-20211108131915628.png)

todo-item을 3번 반복한 것과 같음.

자식 버튼을 누르면, 부모 데이터가 지워져야함,

![image-20211108133629944](/Users/euijinpang/TIL/vue_cli.assets/image-20211108133629944.png)

![image-20211108133806008](/Users/euijinpang/TIL/vue_cli.assets/image-20211108133806008.png)

![image-20211108133941126](/Users/euijinpang/TIL/vue_cli.assets/image-20211108133941126.png)

# 완전히 다른 기능! todoDelete 동명이인

![image-20211108134222979](/Users/euijinpang/TIL/vue_cli.assets/image-20211108134222979.png)

![image-20211108134254719](/Users/euijinpang/TIL/vue_cli.assets/image-20211108134254719.png)



# Router

![image-20211108164158012](/Users/euijinpang/TIL/vue_cli.assets/image-20211108164158012.png)



# YOUTUBE

![image-20211108134909870](/Users/euijinpang/TIL/vue_cli.assets/image-20211108134909870.png)

![image-20211108150309023](/Users/euijinpang/TIL/vue_cli.assets/image-20211108150309023.png)

# 구글클라우드

https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials?project=western-reason-331506

# 유투브 API

https://developers.google.com/youtube/player_parameters

![image-20211109103142783](/Users/euijinpang/TIL/vue_cli.assets/image-20211109103142783.png)

![image-20211109103446861](/Users/euijinpang/TIL/vue_cli.assets/image-20211109103446861.png)

![image-20211109104151811](/Users/euijinpang/TIL/vue_cli.assets/image-20211109104151811.png)

![image-20211109104543970](/Users/euijinpang/TIL/vue_cli.assets/image-20211109104543970.png)