# git error

### git branch root change to 'master'

##### 문제점

`git status` 로 확인시, 폴더의 브랜치 경로가 `master` 이외 경로로 설정

##### 원인

???

##### 해결방안1

`git checkout master` 입력하여 브랜치를 master로 변경

<img src="git_error_solution.assets/error-7829393.png">



##### 해결방안2

origin2 만들었다가 삭제, `git branch -m TIL master`  로 TIL 브랜치 삭제

<img src="git_error_solution.assets/Screen Shot 2021-08-01 at 10.52.31 PM.png">

<img src="git_error_solution.assets/Screen Shot 2021-08-01 at 10.54.14 PM.png">

<img src="git_error_solution.assets/Screen Shot 2021-08-01 at 10.57.21 PM.png">







##### 해결방안 3

- **`git checkout -b master`  ==> Switch to a new branch 'master'**
- **`git branch -d TIL` ==> Deleted branch TIL**
- **`git branch` ==> Check branch**



<img src="git_error_solution.assets/image-20210801230313523.png">

<img src="git_error_solution.assets/image-20210801230459751.png">

