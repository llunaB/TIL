# Docker와 Kubernetes

![image-20220105153719391](0104_Docker와 Kubernetes.assets/image-20220105153719391.png)

### 도커의 장점

- 버젼관리가 쉽다

- 코드작성 -> 빌드 -> ship -> Run
- 개발자가 도커이미지를 잘 만들어서 빌드하면, 도커 컨테이너 실행을 통해 어디서든 띄울 수 있다.

### 도커의 단점

- 컨테이너가 여러개면 처음에는 프록시라는 서버로 접속한다.

- 프록시가 요청을 컨테이너로 연결해준다.

- 서버를 추가하면 로드밸런서가 중간에서 동작하고, 프록시가 서버 2개를 바라보게 된다.

- 도커가 앱을 띄우긴 하지만 로드밸런서는 모두 사람이 관리해야 한다.

- 로드밸런서 - 특정 경로로 들어오면 특정 컨테이너를 바라보도록 설정하는 것.

  

# Container Orchestration

복잡한 컨테이너 환경을 효과적으로 관리하기 위한 도구!

![img](https://i1.wp.com/www.docker.com/blog/wp-content/uploads/2019/10/Docker-Kubernetes-together.png?fit=533%2C300&ssl=1)



![image-20220105154143782](0104_Docker와 Kubernetes.assets/image-20220105154143782.png)



# 쿠버네티스를 이용한 브랜치별 테스트 서버 배포

![image-20220105154217727](0104_Docker와 Kubernetes.assets/image-20220105154217727.png)

![image-20220105154227194](0104_Docker와 Kubernetes.assets/image-20220105154227194.png)

# DevOps 가 되는 법

![image-20220105154306932](0104_Docker와 Kubernetes.assets/image-20220105154306932.png)