# Node.js

Chrome V8 Javascript 엔진으로 빌드된 Javascript 런타임

자바스크립트 프로그래밍 언어가 동작하는 환경

> 다양한 라이브러리를 html, css, javascript로 변경하여 웹브라우저로 보낸다.



## 자바스크립트 동작환경 2가지

1. 웹브라우저에서 동작하는 자바스크립트

2. 컴퓨터에서 동작하는 자바스크립트 => node.js 를 통해 도움을 받는다.



## NVM

node version manager

다양한 버젼의 node.js 바꿀수 있다.

10버젼 이상의 짝수버전이 신뢰도가 높다.

프로젝트에 따라 최적화 버젼이 다르다.



- 설치

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
```

- nvm 버젼 확인

```bash
nvm --version
```



- nvs 확인

```bash
nvm ls
```

- 버젼 설치

```bash
nvm install 12.14.1
nvm install 12.21.0
...
```

- 버젼 선택 (여러 버젼 설치했을 시)

```bash
nvm use 12.14.1
```

- 버젼 삭제

```bash
nvm unusntall 12.21.0
```

- 명령어 확인

```bash
nvm --help
```



## NPM

노드 패키지 매니저

다양한 패키지, 모듈 등 기능을 관리한다.

NPM 생태계 안의 패키지를 로컬 컴퓨터로 가져와서 사용한다.

node.js 설치시 함께 설치된다.

package-lock.json 은 패키지 내의 세부패키지를 자동으로 관리되는 파일이다.

package.json, package-lock.json은 삭제되면 안된다.



- 시작하기

```bash
npm init -y
```

- pakage.json 수정

```
프로젝트명 등 수정
```

- parcel-bundler 패키지 설치 (플래그 -D 꼭!)

```bash
npm install parcel-bundler -D
```

- lodash 패키지 설치

```bash
npm install lodash
```

- package.json에 기록된 (내역이 있는) 삭제한 모듈 재설치

```bash
npm install
```

![image-20210918223756398](/Users/euijinpang/Desktop/node.js.assets/image-20210918223756398.png)



## 개발용/일반 의존성 패키지

1. 개발용 의존성 패키지 설치
   - 개발할때만 필요, 웹브라우저에 필요없다
   - 플래그 `-D`
   - `npm install -D XXX`
2. 일반 의존성 패키지 설치
   - 개발할때도 필요하고, 웹브라우저에서도 동작한다
   - `npm install XXX`



## 개발 서버 실행과 빌드

parcel-bundeler 패키지 통해 터미널에서 로컬환경에서 개발서버 열기



1. package.json 에서 parcel script 수정

![Screen Shot 2021-09-18 at 10.45.31 PM](/Users/euijinpang/Desktop/node.js.assets/Screen Shot 2021-09-18 at 10.45.31 PM.png)

2. `index.html `실행

```bash
npm run dev
```

---



- lodash : 개발용 아닌 웹용

![image-20210918225315770](/Users/euijinpang/Desktop/node.js.assets/image-20210918225315770.png)



3. 웹브라우저용 빌드 실행

![image-20210918225435287](/Users/euijinpang/Desktop/node.js.assets/image-20210918225435287.png)

```bash
npm run build
```

- `dist` 폴더는 웹에서 사용하는 것!



## 유의적 버젼(SemVer)

Semantic Versioning, SemVer

버전에 의미를 부여하여 구분하고 해석한다.



- 버젼 확인

```bash
node --version
>>> v12.14.1
npm --version
>>> 6.13.4
```



#### Major.Minor.Patch

- Major : 기존 버전과 호환되지 않는 새로운 버전
- Minor : 기존 버전과 호환되는 새로운 기능이 추가된 버전 
- Patch : 기존 버전과 호환되는 버그 및 오타 등이 수정된 버전



#### ^Major.Minor.Patch

Major 버전 안에서 가장 최신 버전으로 업데이트를 허용한다는 의미

캐럿기호 제거하면 Major 도 바뀌거나 업데이트가 동작하지 않는다.



- 버젼 확인 (lastest 와 package.json 내 적인 버젼 비교)

```bash
npm info lodash
```

- 직접 버젼 확인 (lodash > package.json)

![image-20210918231007622](/Users/euijinpang/Desktop/node.js.assets/image-20210918231007622.png)

- 버젼 낮춰 설치하기

```bash
npm install lodash@4.17.20
```

- 버젼 업데이트하기

```bash
npm update lodash
```



## 버전관리 (.gitignore) **주의!!!

버전관리 할 필요가 없다면 깃헙에 올릴 필요가 없다.

항상 `npm istall` `npm run dev` `npm run build` 등으로 설치가 가능하기 때문이다!

아래 파일은 버전관리 필요가 없다.

#### .gitignore

- .cache
- dist
- node_modules

