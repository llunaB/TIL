# git

> 버전 관리 시스템



### 생성

##### init

- 현재 폴더를 git으로 관리하겠다.
- 현재 폴더에 `.git` 폴더를 생성
- 최초 한번만 실행하는 명령어
- 프로젝트 단위에서 실행

```bash
git init
```

##### 

##### 처음 생성시

- 등록

```bash
git config --global user.name "name"
git config --global user.email "email"
```



### 확인

##### status

- 현재 git 이 관리하고 있는 파일들의 상태를 보여주는 명령어

```bash
git status
```

##### log

- 커밋의 히스토리를 보여주는 명령어 (git log --online)

```bash
git log
```



### 관리(로컬)

##### add

- working directory에서 staging area에 파일을 업로드 하는 명령어
  - `.` : 현재 폴더, 하위 폴더, 하위 파일 모두 의미

```bash
git add <file name>
# git add .
```

##### commit

- staging area에 올라온 파일들을 하나의 커밋으로 만들어주는 (스냅샷 찍는) 명령어

```bash
git commit -m "commit massage"
#-로 시작하는 것은 옵션
```



### 관리(원격)

##### remote add

- 원격 저장소 주소를 로컬에 저장하는 명령어
  - nickname에는 일반적으로 `origin`

```bash
git remote add <nickname> <url>
```

##### push

- 원격 저장소로 로컬의 커밋기록을 업로드 하는 명령어

```bash
git push <nickname> <branch name>
```



---



### 시작하기

1. 초기화 : 폴더를 repository(로컬저장소)로 바꿔준다.

```bash
git init
```

2. 변경사항 추가하기

```bash
git add README.md .gitingnore
```

3. commit 하기

```bash
git commint -m "first commit"
```
4. 원격저장소와 연결
```bash
git remote add <name> <url>
```

5.  push

```bash
git push <name> <url>
```



# clone 하기

해당 페이지에서 http 주소 복사 

```bash
git clone <URL>
```



## 한페이지 요약

```bash
git init
git config --global user.name "username"
git config --global user.email "email"
-------Repo 
git add <filename>
git commit -m <message>
-------Local Repo
git remote add <name(origin)> <URL>
git push <name(origin)> <branch(master)>
-------Remote Repo (github)
```
