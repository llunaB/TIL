# git branch

- 협업의 핵심, 기능단위
- 작업단위, 기능단위 기록을 중간중간 남기게 되므로 문제가 발생했을 경우 원인이 되는 작업을 찾을 수 있다.



```bash
# 확인하기
git log --oneline
git log --oneline --graph
git status
# branch 목록보기
git branch
# 빠져나오기
q
```



## master 브랜치

- 저장소를 처음 만들면 'master'라는 이름의 브랜치가 만들어진다.



## 통합브랜치(Integration Branch)

- 언제든지 배포할 수 있는 버전을 만들 수 있어야 하는 브랜치
- 일반적으로 저장소를 처음 만들었을 때 생기는 'mater'브랜치를 통합 브랜치로 사용
- 늘 안정적인 상태, 즉 모든 기능이 정상적으로 동작하는 상태여야 한다.
- 통합 브랜치에서 토픽 브랜치를 만들어낸다.



## 토픽 브랜치(Topic Branch)

- 기능 추가나 버그 수정과 같은 단위 작업을 위한 브랜치
- 특정 작업이 완료되면 다시 통합 브랜치에 병합하는 방식으로 진행

![image-20210917094044566](/Users/euijinpang/TIL/git/git_branch.assets/image-20210917094044566.png)



## 순서

- 해당 폴더 내에서 vscode 열기


- 
```bash
touch README.md .gitignore
```


- 
```bash
git init
```

- 루트커밋하기

```bash
git add .
```

```bash
git commit -m "first commit"
```

```python
# POINT
1. branch는 단순한 포인터(화살표)다.
2. HEAD는 단순한 포인터다. (포인터의 포인터인 경우가 많다.)
3. HEAD는 현재 내가 작업중인 커밋을 의미한다.
4. HAED가 master에 있다. == 현재 master에서 작업중이다.
```

- 브랜치 생성

```bash
git branch <branch name (b1)>
```

- 브랜치 스위칭
  - HEAD가 가리키는 것이 master 에서 branch로 변함

```bash
git switch b1
# switched to branch 'b1'
```

```bash
# POINT
5. `git branch <name>`으로 새로운 브랜치 생성
6. 모든 작업은 commit 단위이다! 커밋하지 않으면 git이 관리하지 않아 이방인이 된다. 어떤 branch 에서 commit하느냐가 중요하다.
```



### 브랜치 만듦과 동시에 스위치하기

- git branch b3 >  git switch b3

  ```
  git switch -c b3
  ```



## 여럿이 협업하기

1. 새 프로젝트 생성(리모트에서) : README를 체크하고 만들면 initial commit 이 된다.
2. 다른 사용자 member 권한 부여
3. 설정- 저장소 - protected branches - 마스터브랜치 머징 및 푸쉬권한 설정
   - **master branch 에 push 금지!!** 
4. clone 받는다 + 폴더명 변경

```bash
cd 6th-collabo/
```

```bash
git clone <<address>> collabo_A
```

```bash
git clone <<address>> collabo_B
```

5. 브랜치 만들면서 이동한다.

```bash
```

6. 

```bash
git push origin dev-a
```

```bash
git push origin dev-b
```

7. merge request : dev-b 에서 작업한 내용을 master에 반영해주세요
   - Assignee
   - Reviewer
8. 머지하면 기존 브랜치는 삭제합니다 (옵션)
9. 머지한다
10. 새 마스터 받아온다
11. 기존 브랜치 지운다
12. 

