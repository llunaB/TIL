# Jira 및 JQL 활용

## Jira

### 백로그 설정

### 스프린트 설정

- 백로그에서 하나씩 빼서 스프린트에 담는다.

### 스크럼 미팅(데일리)

- 오늘의 기분 이야기하기
- 오늘 내가 할 일, 하고 있는 일, 한 일 발표하기

### 용어

- `story` : 유저스토리 , 기능(시나리오)
- `task` : 스토리와 구분은 잘 안된다
- `bug` : 버그
- `epic` : 큰 개념에 할일을 담음 (ex. 사용자 관리, 서버관리, 결제관리 or.. 프론트엔드/백엔드)

- `summary` : 이슈의 제목
- `reporter` : 생성하는 사람 또는 보고자
- `component` : 기능적인 측면에서 큰 항목. 에픽과 컴포넌트의 개념은 팀별로 정하면 된다.



## JQL

Jira Query Language

### Dates

- Current(Today) 기준으로 
  - 1d, 2d, 3d, -1d, -2d, -3d, ...
  - 1w, 2w, -1w, -2w, ...

### Functions

- `startOfDay()`  : 00 시

- `currentLogin()` : 현재 로그인한 시간 기준 이후 또는 이후 생성된 이슈를 알고싶을때

- `currentUser()` : 현재 로그인한 사용자 (가 담당자인 이슈를 보여줘) 

- 이틀 전에 수정된 이슈를 보여줘

  ```
  project = DP AND updated > -2d
  ```

- 일요일 이후 수정된 이슈 조회

  ```
  project = DP AND updated > startOfWeek()
  ```

- 월요일 이후 금요일 이전에 수정된 이슈 조회

  ```
  project = S06P10A214 AND updated > startOfWeek(1d) AND updated < endOfWeek(-1d) 
  ```

- 내가 담당자인 이슈 조회

  ```
  project = S06P10A214 AND assignee = currentUser()
  ```

- 내가 담당자이면서 끝낸 이슈 조회

  ```
  project = S06P10A214 AND assignee = currentUser() AND status = Done
  ```

  

### smart commit 기능

- github 과 연계, merge가 끝나면 이슈도 닫힌다.
- 이슈를 기반으로 브랜치를 생성할 수 있다.