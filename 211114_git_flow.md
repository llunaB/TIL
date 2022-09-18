### 🌈 commit convention

- `feat` : new feature for the user, not a new feature for build script
- `fix` : bug fix for the user, not a fix to a build script
- `docs` : changes to the documentation
- `style` : formatting, missing semi colons, etc; no production code change
- `refactor` : refactoring production code, eg. renaming a variable
- `chore` : updating grunt tasks etc; no production code change

```bash
feat: profile-history schrollbar add
```



### ⭐️ git flow 

##### 1. git clone

```bash
git clone https://lab.ssafy.com/s06-webmobile1-sub1/S06P11A206.git
```

##### 2. develop 브랜치로 이동

```bash
git switch develop
```

 ### 👉  feature work flow

 ##### 3. feature branch 생성

```bash
git branch feature/be/user/login
```
##### 4. feature branch 로 이동

```bash
git switch feature/be/user/login
```

##### 5. ‼️**중요**‼️ develop branch pull 진행 

```bash
git pull origin develop
```

##### 6. 개발 후 add - commit - push 진행

- 일반적으로는 `develop` 브랜치에 바로 `push` 하지만,  ssafy project에서는 진행사항 확인을 위해  `feature branch` 도 `remote` 에 올립니다.

```bash
git add .
git commit -m "feat: profile-history schrollbar add"
git push origin develop
```

##### 7. feature branch 에서 개발 진행

- `convention` 참고
```bash
git add .
git commit -m "feat: profile-history schrollbar add"
git push origin feature/be/user/login
```

##### 8. 테스트까지 진행 후 develop branch에 merge 진행
- `assignee` 와 `reviewer`는 필요시 등록합니다.

- 방법 1 : `feature branch` 에서 `develop branch` 로 `push` 

```bash
# feature 
git push origin develop
```

- 방법 2 : `develop branch` 에서 `feature branch` 를 `merge` 

```bash
# develop 
git merge feature/be/user/login
```

##### 9. merge request 작성

- `gitlab` 의 푸시알림 확인
- `merge request` 만들기
- 내용 입력 후 `delete branch after merge request` 체크되어있는지 확인, ‼️**체크 해제**‼️
- `merge` 

##### 10. develop branch pull
- `pull` 은 매번 해주기
```bash
git pull origin develop
```
