### git

- **git init** : 현재 디렉토리를 Git이 관리하는 프로젝트 디렉토리(=working directory)로 설정하고 그 안에 레포지토리(.git 디렉토리) 생성
- **git config** **user.name 'codeit'** : 현재 사용자의 아이디를 'codeit'으로 설정(커밋할 때 필요한 정보)
- **git config user.email 'teacher@codeit.kr'** : 현재 사용자의 이메일 주소를 'teacher@codeit.kr'로 설정(커밋할 때 필요한 정보)
- git add

```
git add [file name]
git add [directory name]
```

- git help

```
git help [command name]
man git-[command name]
```

- git add 취소하기(staging area에서 파일 제거)

```
git reset file.py
```

- git 인식내용 보기

```
git status
```

---

### github

- **git push** : 새로운 커밋을 로컬 레포지토리에서 리모트 레포지토리에 반영 (collaborator 지정시 타인도 가능)

- **git pull** : 리모트 레포지토리의 새로운 내용을 로컬 레포지토리에 반영

- **git clone** : 프로젝트 디렉토리 가져오기

---

### commit 다루기

- 커밋 히스토리 보기

```
git log
```

- 커밋 히스토리 깔끔하게 보기

```
git log --pretty=oneline
```

- 커밋 자세히 보기 - 특정 커밋에서 어떤 변경사항이 있었는지 보기
  - `---`이전 커밋
  - `+++`해당 커밋

```
git show [commit_id]
```

- m 옵션 없이 커밋메세지 남기기

  - git commit 

  - `i` 누르고 맨 commit 메세지 작성

  - `esc` + `:wq` 로 나가기

- 최신 커밋 수정하기(추가 커밋 없이)
  - git log --pretty=oneline
  - 파일 수정
  - git add .
  - **git commit --amend**

# commit message 작성 가이드라인

**(1) 커밋 메시지의 제목과 상세 설명 사이에는 한 줄을 비워두세요.**

**(2) 커밋 메시지의 제목 뒤에 온점(.)을 붙이지 마세요.**

**(3) 커밋 메시지의 제목의 첫 번째 알파벳은 대문자로 작성하세요.**

**(4) 커밋 메시지의 제목은 명령조로 작성하세요.(Fix it / Fixed it / Fixes it)**

**(5) 커밋의 상세 내용에는 이런 걸 적으면 좋습니다.**

- 왜 커밋을 했는지
- 어떤 문제가 있었고
- 적용한 해결책이 어떤 효과를 가지는지

**(6) 다른 사람들이 자신의 코드를 바로 이해할 수 있다고 가정하지 말고 최대한 친절하게 작성하세요.** 

# 커밋할 때 알아야할 가이드라인

**(1) 하나의 커밋에는 하나의 수정사항, 하나의 이슈(issue)를 해결한 내용만 남기도록 하세요. 다양하게 수정을 하고나서 하나의 커밋으로 남기는 것은 좋지 않습니다. 하나의 커밋이 하나의 사실만을 갖고 있어야 나중에 이해하기 쉽습니다.** 

**(2) 현재 프로젝트 디렉토리의 상태가 그 내부의 전체 코드를 실행했을 때 에러가 발생하지 않는 상태인 경우에만 커밋을 하도록 하세요. 나중에 동료 개발자가 특정 커밋의 코드로 실행했을 때 에러가 발생한다면 혼란을 줄 수 있습니다.**



### alias 설정

- **git histroy라고만 써도 자동으로 git log --pretty=oneline을 실행**

```bash
git config alias.history 'log --pretty=oneline'
```



- 두 커밋 간의 차이 보기

```
git history
```

```
git diff [commit1_id] [commit2_id]
```



- working directory 내부 살펴보기

```
ls -al
```



## HEAD 의 이동

- hard / mixed / soft
- `git history` => repository 확인
- `cat [file_name]` => working directory 확인
- `git status` => staging area 확인

- 이전 커밋으로 head 를 이동시키고 + staging area 바꾸기 + working directory 내부도 바꾸기(이전것 다 날아가므로 주의!!!)

```
git reset --hard [commit_id]
git reset --hard HEAD^ 					# 상대경로(바로 직전 커밋으로 이동)
git reset --hard HEAD~n					# 상대경로(n단계 전 커밋으로 이동)
```

- 이전 커밋으로 head 를 이동시키고 + staging area 바꾸기 + working directory 내부 안바꿈

```
git reset --mixed [commit_id]
```

- 이전 커밋으로 head 를 이동시키고 + staging area 안바꿈 + working directory 내부 안바꿈

```
git reset --soft [commit_id]
```

- 이전 상태로 돌리기

```
git pull
```



# branch

- 기본적으로 master 브랜치 생성
- brach 생성

```bash
git branch branchA
```

- branch 이동

```bash
git checkout branchA
```

- 현재 레포지토리의 모든 브랜치 확인

```bash
git brach
```

- branch 삭제

```bash
git branch -d branchA
```

- branch 만들고 바로 이동

```bash
git checkout -b branchA
```

- master 브랜치에서 내용을 수정하고, branchA에서 그 변경 내용을 반영하고 싶은 경우

```bash
# master brahch 바꾼 상태
git checkout branchA
git merge master
# commit message
:wq
```

- conflict 해결

```bash
# conflict 메세지 출력
# 해당 파일 접속하여 머지의 결과가 되면 좋겠다는 내용으로 수정
git add .
git commit
:wq
```

- merge 작업 취소

```bash
git merge --abort
```

- 로컬 레포지토리의 내용을 맨 처음 리모트 레포지토리에 보낼 때 (로컬 레포지토리의 A 브랜치에 대응되는 리모트 레포지토리의 A' 브랜치가 있을 때, A' 브랜치를 A 브랜치의 upstream 브랜치라 한다.)

```bash
git push --set-upstream origin master 
```



# git fetch

- merge는 안하고 일단 가져와서 확인
- git fetch
- git diff



- 어떤 파일의 특정 코드를 누가 작성했는지 찾아내는지

```bash
git blame [file_name]
```

```bash
git show [commit_id]
```



# git revert

- 이미 리모트에 올라간 커밋 취소하고 되돌리기

```bash
git revert [commit_id]
:wq
git push
```

# 여러 커밋 취소하기

```bash
git revert [commit_from_id]...[commit_to_id]
:wq
git push
```

```bash
git h
```

