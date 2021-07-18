# command

> git 기본 명령어 정리

## 생성

##### init

- 현재 폴더를 git으로 관리하겠다
- 현재 폴더에 `.git` 폴더를 생성 
- 최초 한 번만 실행하는 명령어
- 프로젝트 단위에서 실행

```bash
git init
```



## 확인

##### status

- 현재 git이 관리하고 있는 파일들의 상태를 보여주는 명령어

```bash
git status
```

##### 

##### log

- 커밋의 히스토리를 보여주는 명령어

``` bash
git log
```



## 관리(로컬)

##### add

- working directory에서 staging area에 파일을 업로드하는 명령어
  - `.` : 현재폴더, 하위폴더, 하위파일 모두 업로드

```bash
git add <file name>
# git add .
```



##### commit

- staging area에 올라온 파일들을 하나의 커밋으로 만들어주는(스냅샷 찍는) 명령어
- commit message 부분에는 변경한 요소를 간략히 적는다

```bash
git commit -m "commit message"
```

## 

## 관리(원격)

##### remote add

- 원격 저장 주소를 로컬에 저장하는 명령어
  - nickname에는 일반적으로 `origin`을 사용한다.
  - url 주소는 git이 관리하고 있는 (git init으로 설정한) 위치의 url.git

```bash
git remote add <nickname> <url>
```



##### push

- 원격 저장소로 로컬의 커밋 기록을 업로드 하는 명령어
- nickname 에는 일반적으로 `origin` 을 사용한다. 

```bash
git push <nickname> <brach name>
```



