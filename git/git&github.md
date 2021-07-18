# git & github

### git 

##### git 이란?

- 분산 버전 관리 시스템. 개발 과정과 역사를 볼 수 있고, 프로젝트 이전 버전을 복원, 변경 사항 확인도 가능하다.

##### git 작업 흐름

- add(무대위에 올린다) - commit(스냅샷을 만든다) - push(기존 커밋들에 새로 생성한 커밋을 반영한다)
- 위의 세 과정과 github은 별개이다. 앞의 세 과정은 local, github은 remote에 해당한다.







### github









### git에 올리기

##### git 으로 컨트롤하게 만든다 (master) 가 생겨야 한다

```bash
git init
```



##### git status로 확인

```bash
git status
```



##### 깃에 올리기

```bash
git add <file name>
```



##### (처음 설정시) 유저이름 설정하기

```bash
git config --global user.name <name>
```



##### (처음 설정시) 이메일 설정하기

```bash
git config --global user.emial <email>
```



##### 커밋하기

```bash
git commit -m "add <file name>"
```



##### 푸시하기

```bash
git push origin master
```





