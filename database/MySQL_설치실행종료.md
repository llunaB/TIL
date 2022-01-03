# MySQL & Workbench & Sakila DB

# MySQL

### 설치

- MySQL 패키지 확인

```bash
brew search mysql
```

- brew install mysql

```bash
brew install mysql
```

- MySQL 설치 확인

```bash
brew list
```

- MySQL 버전 확인

```bash
mysql -V
```



### 실행

- MySQL 실행

```bash
mysql.server start
```



### 설정

- 초기설정

```bash
mysql_secure_installation
```



### 접속

- local MySQL server 접속

```bash
mysql -u root -p
```

- 서버 설정 확인

```bash
mysql> status
```



### 서버 종료

```bash
mysql.server stop
```



### ** terminal **

```
(base) ➜  ~ cd /usr/local/mysql/bin
(base) ➜  bin ./mysql -u root -p
mysql> use sakila
```



# MySQL Workbench

MySQL 사용을 편리하게 만든 클라이언트 툴



### mysqlworkbench 설치

사이트에 접속하여 파일을 다운받거나 brew 설치가 가능하다.

https://dev.mysql.com/downloads/workbench/

```bash
brew install --cask mysqlworkbench
```

- 데이터베이스 생성

```sql
CREATE SCHEMA `mydatabase` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci ;
```

- 데이터베이스 삭제

```sql
DROP DATABASE `mydatabase`;
```



# Sakila Database

### sakila database 설치

사이트에 접속하여 다운로드

https://dev.mysql.com/doc/index-other.html

### sakila database 실행

```
File > Open SQL Script > ...sakila-schema.sql
File > Open SQL Script > ...sakila-data.sql
```

- 터미널 사용

```
use sakila
```

