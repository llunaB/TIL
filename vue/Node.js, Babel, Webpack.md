# Node.js

- Javascript Runtime Environment
- 자바스크립트를 브라우저 아닌 환경에서도 구동할 수 있는 자바스크립트 런타임 환경

# NPM(Node Package Manager)

- 자바스크립트 언어를 위한 패키지 관리자

# Babel

- Javascript Compiler
- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역해주는 도구
- 원시 코드(최신 버젼)을 목적 코드(구 버젼)으로 옮긴다.
- 개발자는 최신 문법이 이전 브라우저나 환경에서 동작하지 않는 상황을 해결할 수 있다.

# Webpadk

- Static module bundler
- 모듈 간 의존성 문제를 해결하기 위한 도구로, 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드한다.
- 모듈 의존성 문제를 해결해주는 작업을 Bundling 이라 하고, 이런 일을 해주는 도구를 Bundler라 한다.

# node_modules & package-lock.json

- `package-lock.json` 의 경우, `node_modules`에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 팀원 및 배포 환경에서 동일한 종속성을 설치하도록 보장한다.
- node_modules는 git에 올리지 않도록 주의한다.