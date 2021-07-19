# git flow

## git과 github 

##### git 이란?

- 분산 버전 관리 시스템. 개발 과정과 역사를 볼 수 있고, 프로젝트 이전 버전을 복원, 변경 사항 확인도 가능하다.



##### github 란?

- git을 통해 프로젝트를 올릴 수 있는 저장 공간. gitlab, bigbucket 도 동일하다.



##### git 과 github

- git과 github은 별개이다. git이 사진첩이라면 github은 구글 드라이브/드롭박스/아이클라우드이다.
- github에 업로드하고 내리는 것은 github 사이트가 아닌 터미널로 관리하는 것이 좋다.

  

## git 작업흐름 총정리 (mac과 window에서 하나의 github 관리하기) 

##### git 작업흐름은 크게 `add `- ` commit` - ` push` 로 이루어진다.

- add와 commit 은 Local 로컬영역이며, push를 통해 Remote 영역으로 넘어간다.

- Working directory (init 명령어를 통해 관리되고 있는 master경로) 파일을 `add`하여  스테이지(staging area) 위에 올려 커밋할 목록을 만든다. (INDEX)

- 이후 `commit`하여 커밋을 만든다. (create a snapshot) 커밋이 쌓인다. (HEAD)

  -----------------여기까지가 local 영역

  ---------------- 여기부터 remote 영역

- `push` 하여 Github에 올린다.



##### 1. window 에서 최초 설정

- git 로컬 저장소를 설정한다.

```bash
git init
```

- 확인해본다. master 표시 있어야 한다.

```bash
git status
```

- `add` 파일을 스테이지로 올린다.

```bash
git add <file name>
# git add .
```

- cf. 잘못되었을 경우 `add`취소한다.

```bash
git reset HEAD <file name>
# git reset
```

- `commit` 커밋을 만든다.

```bash
git commit -m "commit message"
```

- cf. 잘못 만든 경우 `commit` 취소한다. 꺽쇠 갯수에 따라 최신 커밋부터 삭제한다.

```bash
git reset HEAD^
git reset HEAD^^
git reset HEAD^^^
```

- (최초시) git commit 작성자(author)를 설정한다.

```bash
git config --global user.email myemail@gmail.com
git config --global user.name myusername
```

- (최초시) 설정한 값을 확인한다. 입력한대로 나오면 된다.

```bash
git config --global user.email
git config --global user.name
```

- 오타나 잘못 입력했을 경우 다시 입력하면 덮어씌워진다.
- 지우고 싶은 경우 지우고, 삭제되었는지 리스트에서 확인한다.

```bash
git config --unset --global user.name
git config --unset --global user.email

# 현재 상태를 확인
git config --list
```

- (최초시) 이제 Local 영역에서 Remote로 넘어왔다. 원격 저장소를 등록하자. master로 관리되고 있는 경로.git 주소를 입력하면 된다.

```bash
git remote add origin https://github.com/.../folder.git

# 등록된 원격 저장소 목록 확인
git remote -v

# 등록된 원격 저장소명 확인
git remote
```

- 원격 저장소에 `push`로 업로드한다.

```bash
git push origin master

# git push <username> <branch>

# 잘 올라갔는지 확인해본다
git status
git log
git config --list
```



##### 2. mac 에서 클론, 수정 및 푸시

github 에 잔디가 심어졌을 것이다. 이제 mac으로 작업해보자

- `clone`으로 원격 저장소에서 mac의 로컬 저장소로 프로젝트를 가져오자. *이때 master branch를 자동으로 가져오고 origin도 remote로 add해준다. 해당 디렉토리로 들어가면 이미 git 프로젝트로 init 되어있고, remote 등록도 되어 있다.* 

```bash
git clone https://github.com/.../folder.git
```



- 파일을 변경했다면, 1번과 같은 방법으로 `add` - `commit` - `push` 를 진행한다. 이때 동일한 username과 password를 입력하여 로그인한다. 

- 향후 gmail 로 인증관련 메일이 하나 올텐데, 메일대로 따라하면 된다.

  > https://ninefloor-design.tistory.com/126



##### 3. window 에서 풀, 수정 및 푸시

mac 을 통해 파일을 github에 push 했으니 window 환경에서는 다시 내려받아야 한다.

- `pull`을 통해 최신 상태로 받는다.

```bash
git pull origin master
# git pull <username> <branch>
```

- 파일을 수정하고, 다시 푸시한다. 이렇게 반복한다.

