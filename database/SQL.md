# SQL

### 1. SQL 용어 및 개념

- Structured Query Language

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정, 자료의 검색 및 관리

#### 용어

- 기본키(Primary Key)
  - 각 행(레코드)의 고유값으로 반드시 설정해야 한다.

- 테이블
  - 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

- 스키마
  - 관계형 데이터베이스에서 자료의 구조, 표현방법 등 전반적인 명세를 기술한 것.

- 행 = 로우 = 레코드
  - 단일 구조 데이터 형식을 가리키는 행

- 열 = 컬럼 = 필드
  - 고유한 데이터 형식이 지정되는 열

- RDB(관계형 데이터베이스)
  - **python** => (makemigrations) => **schema** => (migrate) => **Table**



---



### 2. SQL과 No-SQL

- Django에서 연동만 시켜주면 모든 DBMS 사용이 가능하다

- ##### SQL Database

  - SQL - relational databse
  - MySQL, Maria DB, Oracle 등 RDBMS

- ##### NoSQL Database

  - 데이터베이스마다 각각 문법이 다르다

  - MongoDB(자바스크립트), Firebase(리얼타임) => json, 딕셔너리 형태



---



### 2. SQL 문법

- DDL - 데이터 정의 언어
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, DROP, ALTER
- DML - 데이터 조작 언어
  - 데이터를 저장, 조회, 수정, 삭제 하기 위한 명령어
  - INSERT, SELECT, UPDATE, DELETE



---



### 3. Relational DBMS(RDBMS)

- Relational Database Management System
- 표로 만들어진 관계형 데이터베이스를 관리하는 시스템

- 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템
- DB-Engine => 모두 **SQL 문법** 을 사용!
  - MySQL, SQLite, PostgreSQL, ORCLE, MS SQL



---



### 4. INSERT INTO

```sql
CREATE TABLE classmates(
	name TEXT,
	age INT,
	address TEXT
);

INSERT INTO classmates (name, age, address) VALUES('홍길동', 20, 'seoul')
```



---



### 5. 와일드카드 문자

- % (percent sign)
  - 이 자리에 문자열이 있을 수도, 없을수도 있다.
- _ (underscore)
  - 반드시 이자리에 한 개의 문자가 존재해야 한다.

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
```

- 패턴

```sql
-- 2%        2로 시작하는 값
-- %2        2로 끝나는 값
-- %2%       2가 들어가는 값
-- _2%       아무 값이 하나 있고 두번째가 2로 시작하는 값
-- 1___      1로 시작하고 총 4자리인 값
-- 2_%_%		 2로 시작하고 적어도 3자리인 값
-- 2__%      2로 시작하고 적어도 3자리인 값
```

