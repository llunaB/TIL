[TOC]

# Database

## 데이터베이스

- 체계화된 데이터의 모임
- 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

## 데이터베이스로 얻는 장점

- 데이터 중복 최소화
- 데이터 무결성(정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성 (물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지

# RDB

## 관계형 데이터베이스

- 키와 값들의 간단한 관계를 표로 정리한 데이터베이스

## 용어 정리

- 스키마 : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것
  - column | datatype
- 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합
- 열/필드 (column, field) : 각 열에는 고유한 데이터 형식이 지정됨.
- 행/레코드 (row, record) : 실제 데이터가 저장되는 형태
- 기본키 (Primary Key) : 각 행(레코드)의 고유 값으로 반드시 설정해야 한다. sql 에서는 rowid.

# RDBMS

## 관계형 데이터베이스 관리 시스템

- Relational Database Management System
- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
- MySQL, SQLite, PostgresSQL, ORACLE, MS SQL

## SQLite

- 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단히 DB 구성을 할 수 있으며, 오픈소스 프로젝트로 자유롭게 사용 가능

# SQL

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

## DDL & DML

- DDL : Data Definition Language
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, DROP, ALTER
- DML : Data Manipulation Language
  - 데이터를 저장, 조회, 수정, 삭제 하기 위한 명령어
  - INSERT, SELECT, UPDATE, DELETE



---

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```
  
  * 확인
  
    * sqlite3에서 스키마 확인
  
      ```sqlite
      sqlite > .schema users_user
      CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
      ```



## 실행(장고 프로젝트)

- ORM

  ```bash
  # 가상환경 셋팅(셸 설치)
  python -m venv venv
  source venv/bin/activate
  # 셸플러스 실행
  python manage.py shell_plus
  ```

- SQL

  ```bash
  sqlite3 db.sqlite3
  ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 만 켜고 작성해주세요.

![image-20211004230033199](DB.assets/image-20211004230033199.png)

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql
   SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create (
    first_name='길동',
    last_name='홍',
    age=10,
    country='제주',
    phone='010-1234-1234',
    balance=100,
   )
   ```

   ```sql
   -- sql
   INSERT INTO users_user
   VALUES (102, '길동', '김', 20, '서울', '010-1234-1234', 100);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=102)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id=102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   In [14]: user = User.objects.get(pk=102)
   
   In [15]: user
   Out[15]: <User: User object (102)>
   
   In [16]: user.last_name
   Out[16]: '김'
   
   In [17]: user.last_name = '홍'
   
   In [18]: user.save()
   
   In [19]: user.last_name
   Out[19]: '홍'
   ```

      ```sql
   -- sql
   UPDATE users_user
   SET first_name='철수'
   WHERE id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   In [22]: user = User.objects.get(pk=102)
   
   In [23]: user.delete()
   Out[23]: (1, {'users.User': 1})
   
   In [24]: User.objects.get(pk=102)
   ```

   ```sql
   -- sql
   DELETE FROM users_user
   WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   User.objects.count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user 
   WHERE age-30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   User.objects.filter(age__lte=20).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE age<=20;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE age=30 AND last_name='김';
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   User.objects.filter(Q(age=30)|Q(last_name='김'))
   ```

   ```sql
   -- sql
   SELECT * FROM users_user 
   WHERE age=30 OR last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone__startswith='02-').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE phone LIKE '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country='강원도', last_name='황').values('first_name').first().get('first_name')
   ```

      ```sql
   -- sql
   SELECT first_name FROM users_user 
   WHERE country='강원도' AND last_name='황'
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY age DESC LIMIT 10;
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY balance ASC LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

   ```python
   # orm
   User.objects.order_by('balane', '-age')[:10]
   ```

   ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY balance ASC, age DESC LIMIT 10;
   ```

4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name', '-first_name')[4]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user 
   ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   User.objects.aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   SELECT AVG(age) FROM users_user WHERE last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   SELECT AVG(balance) FROM users_user 
   WHERE country='강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   User.objects.aggregate(Sum('balance'))
   ```

      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```

# 와일드카드 문자 LIKE

- % (percent sign)
  - 이 자리에 문자열이 있을 수도, 없을수도 있다.
- _ (underscore)
  - 반드시 이자리에 한 개의 문자가 존재해야 한다.

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
```

- 패턴

```sql
-- 2% or 2_        2로 시작하는 값
-- %2 or _2        2로 끝나는 값
-- %2%       2가 들어가는 값
-- _2%       아무 값이 하나 있고 두번째가 2로 시작하는 값
-- 1___      1로 시작하고 총 4자리인 값
-- 2_%_%		 2로 시작하고 적어도 3자리인 값
-- 2__%      2로 시작하고 적어도 3자리인 값 
```

# AUTOINCREMENT

- 순서대로 증가
- id 에 사용하면 중복을 방지 (ex. Id 5번 삭제후 다시 추가하면 5번이 아닌 6번이 추가)

# ALTER TABLE

- 테이블 이름 변경

```sql
ALTER TABLE articles RENAME TO new_articles;
```

- 테이블에 새로운 열 추가
  - 이때 NOT NULL 없이 만들거나 혹은 디폴트를 함께 지정해야 에러가 나지 않는다.

```sql
ALTER TABLE new_articles ADD COLUMN title TEXT NOT NULL DEFAULT '제목';
```

- 열 이름 수정

```sqlite
ALTER TABLE hotels RENAME COLUMN grage TO grade;
```



---

# SQL

```sql
-- shell 정리 및 정료 
-- in sqlite
• shell clear
• .exit

-- in django_shell_plus
• clear
• exit

-- sqlite 실행하기 & 파일생성하기(파일명.sqlite3)
sqlite3 tutorial.sqlite3

-- 헤더 켜기
.headers on
-- 컬럼 보이기
.mode column

-- table 생성
CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- table 삭제
DROP TABLE classmates;

-- 테이블 이름 변경
ALTER TABLE countries RENAME TO hotels;

-- 열 이름 변경
ALTER TABLE hotels RENAME COLUMN grage TO grade;

-- table 확인
.tables

-- schema 확인
.schema classmates

--전체 데이터 조회
SELECT * FROM classmates;

------------------------------------------------
-- CREATE
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
-- 넣는 데이터의 개수가 컬럼의 개수와 동일하다면 컬럼이름을 생략가능
INSERT INTO classmates VALUES ('홍길동', 23);
-- NOT NULL 을 넣어 테이블 생성(필수값)
CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
-- rowid를 사용해서 테이블 생성(수업에서 사용)
CREATE TABLE classmates(
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );


-- rowid와 나머지 모든 열을 보여주세요
SELECT rowid, * FROM classmates;


-- READ
SELECT rowid, name FROM classmates;
-- READ LIMIT OFFSET
SELECT rowid, name FROM classmates LIMIT 2;
SELECT rowid, name FROM classmates LIMIT 2 OFFSET 2;
-- READ 조건
SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age>=30 AND last_name='김';
-- WHERE
SELECT rowid, name FROM classmates WHERE address='서울';  
-- DISTINCT : 중복되는 값 제외하고 보여줌
SELECT DISTINCT age from classmates;
-- users table의 총 row의 수
SELECT COUNT(*) FROM users;


-- DELETE
DELETE FROM classmates WHERE rowid=1;


-- UPDATE
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;


-- 연산
-- AVG
SELECT AVG(age) FROM users WHERE age>=30;
-- MAX
SELECT first_name, MAX(balance) FROM users;
-->>>"순옥",1000000
-- AVG + WHERE
SELECT AVG(balance) FROM users WHERE age>=30;


-- LIKE
-- 나이가 20대인 사람만 조회?
SELECT * FROM users WHERE age LIKE '2_';
-- 지역번호가 02인 사람만 조회?
SELECT * FROM users WHERE phone LIKE '02-%';
-- 이름이 '준'으로 끝나는 사람?
SELECT * FROM users WHERE first_name LIKE '%준';
-- 중간번호가 5114인 사람만?
SELECT * FROM users WHERE phone LIKE '%-5114-%';


-- ORDER BY
-- 나이순으로 오름차순 정렬?
SELECT * FROM users ORDER BY age ASC;
-- 상위 10개 조회?
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;


-- GROUP BY
-- 각 성(last_name)씨가 몇 명씩 있는지 조회?
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-->>> "강",23 "고",10 ...
```



---



# 워크숍(심화)

### SQL & ORM. 

##### 1. SQL Query 

![image-20210914202734927](/Users/euijinpang/db/DB.assets/image-20210914202734927.png)

```sql
-- 1. 테이블 생성
CREATE TABLE countries(
room_num TEXT,
check_in TEXT,
check_out TEXT,
grage TEXT,
price INT
);

-- 2. 데이터 입력
INSERT INTO countries (room_num, check_in, check_out, grage, price) VALUES ('1102', '2020-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries (room_num, check_in, check_out, grage, price) VALUES ('B203', '2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries (room_num, check_in, check_out, grage, price) VALUES ('303', '2020-01-01', '2020-01-03', 'deluxe', 500);
INSERT INTO countries (room_num, check_in, check_out, grage, price) VALUES ('807', '2020-01-04', '2020-01-07', 'superior', 300);

-- 3. 테이블 이름 변경
ALTER TABLE countries RENAME TO hotels;

-- 4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price 조회
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

✅-- 5. grade별 분류하고 분류된 grade 개수를 내림차순으로 조회
✅-- GROUP BY 사용 
SELECT grade, COUNT(grade) FROM hotels GROUP BY grade ORDER BY COUNT(grade) DESC;

-- 6. 객실 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보 조회
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='suite';

✅-- 7. 지상층 객실이면서 2020년 1월 4일에 체크인한 객실의 목록을 price 오름차순으로 조회
✅-- NOT LIKE 사용
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price;

```

5번![image-20210915124028877](/Users/euijinpang/db/DB.assets/image-20210915124028877.png)

7번

![image-20210915124806269](/Users/euijinpang/db/DB.assets/image-20210915124806269.png)



![image-20210914231709628](/Users/euijinpang/db/DB.assets/image-20210914231709628.png)

##### 2. SQL ORM 비교 

1. user 테이블 전체 데이터를 조회하시오.


   ```python
   # orm
   User.objects.all()
   ```

   ```sql
   -- sql
   SELECT * FROM users_user;
   ```


2. id가 19인 사람의 age를 조회하시오.


   ```python
   # orm
   User.objects.filter(id=19).values('age')
   ```

   ```sql
   -- sql
   SELECT age FROM users_user WHERE id = 19;
   ```


3. 모든 사람의 age를 조회하시오.


   ```python
   # orm
   User.objects.values('age')
   ```

   ```sql
   -- sql
   SELECT age FROM users_user;
   ```


4. age가 40 이하인 사람들의 id와 balance를 조회하시오.


   ```python
   # orm
   User.objects.filter(age__lte=40).values('id','b
       ...: alance')
   ```

   ```sql
   -- sql
   SELECT id, balance FROM users_User WHERE age <= 40;
   ```


5. last_name이 '김'이고 balance가 500 이상인 사람들의 first_name을 조회하시오.


   ```python
   # orm
   User.objects.filter(last_name='김', balance__lt
       ...: e=500).values('first_name')
   ```

   ```sql
   -- sql
   SELECT first_name FROM users_user WHERE
      ...> last_name = '김' AND balance >= 500;
   ```


6. first_name이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오.


   ```python
   # orm
   User.objects.filter(first_name__endswit
       ...: h='수', country='경기도').values('balan
       ...: ce')
   ```

   ```sql
   -- sql
   WHERE first_name LIKE '%수' AND country = '경기도';
   ```


7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.


   ```python
   # orm
   User.objects.filter(Q(balance__gte=2000
       ...: )|Q(age__lte=40)).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE balance >= 2000 OR age <= 40;
   ```


8. phone 앞자리가 '010'으로 시작하는 사람의 총원을 구하시오.


   ```python
   # orm
   User.objects.filter(phone__startswith='010').count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '010%';
   ```


9. **❇️ 이름이 '김옥자'인 사람의 행정구역을 경기도로 수정하시오.**


      1. **방법 1번 - 하나의 인스턴스를 수정한다**.

   ```python
# orm
user = User.objects.filter(first_name='옥자', last_name='김')[0]
user.country = '경기도'
user.save()
   ```

      2. **방법 2번 - filter로 가져온 쿼리셋을 수정한다. - Update 메소드 사용**

   ```python
#orm
user.objects.filter(first_name='옥자', last_name='김').update(country='경기도')
   ```

      3. **방법 3번 - get을 써도 단일데이터면 괜찮다. 그러나 중복가능성 있음.**

```python
# orm
user = User.objects.get(first_name='옥자', last_name='김')
user.country = '경기도'
user.save()
```

```sql
-- sql
UPDATE users_user SET country = '경기도' WHERE first_name = '옥자' AND last_name = '김';
```

10. 이름이 '백진호'인 사람을 삭제하시오.

       ```python
     # orm
     user = User.objects.get(first_name='진호', last_name='백')
     user.delete()
       ```

     ```sql
    -- sql
    DELETE FROM users_user WHERE first_name='진호' AND last_name='백'; 
     ```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오.

    ```python
    # orm
    User.objects.order_by('-balance')[:4].values('first_name','last_name', 'balance')
    ```

      ```sql
    -- sql
    SELECT first_name, last_name, balance FROM users_user ORDER BY balance DESC LIMIT 4;
      ```

12. phone에 '123'을 포함하고 age가 30 미만인 정보를 조회하시오.

    ```python
    # orm
    User.objects.filter(phone__contains='123', age__lte=30)
    ```

      ```sql
    -- sql
    SELECT * FROM users_user WHERE phone LIKE '%123%' AND age < 30;
      ```

13. **❇️ phone이 '010'으로 시작하는 사람들의 행정구역을 중복없이 조회하시오.**

      - `field lookup` 사용
      - 중복없이 조회 : `distinct` 메소드 사용

      ```python
    # orm
    User.objects.filter(phone__startswith='010').values('country
    ').distinct()
      ```

      ```sql
    -- sql
    SELECT DISTINCT country FROM users_user WHERE phone LIKE '010%';
      ```

14. 모든 인원의 평균 age를 구하시오.

      ```python
    # orm
    User.objects.aggregate(Avg('age'))
      ```

      ```sql
    -- sql
    SELECT AVG(age) FROM users_user;
      ```

15. 박씨의 평균 balance를 구하시오.

    ```python
    # orm
    User.objects.filter(last_name='박').aggregate(Avg('balance'))
    ```

      ```sql
    -- sql
    SELECT AVG(balance) FROM users_user WHERE last_name = '박';
      ```

16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오.

    ```python
    # orm
    User.objects.filter(country='경상북도').aggregate(Max('balance'))
    ```

      ```sql
    -- sql
    SELECT MAX(balance) FROM users_user WHERE country='경상북도';
      ```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

    ```python
    # orm
    User.objects.filter(country='제주특별자치도').order_by('-balance')[:1].values('first_name')
    User.objects.filter(country='제주특별자치도').order_by('-balance')[0].values('first_name')
    User.objects.filter(country='제주특별자치도').order_by('-balance').first().values('first_name')
    ```
    
      ```sql
    -- sql
    SELECT first_name FROM users_user WHERE country='제주특별자치도' ORDER BY balance DESC LIMIT 1;
      ```





---



# 기타

- Django의 ModelField 중 *DateField* , *DateTimeField* 필드의 옵션으로 사용되는 *auto_now* 와 *auto_now_add*의 차이

  ```python
  last_updated =  models.DateField('last_updated',auto_now_add=True,null=True)
  ```

  - **updated_at > 수정일자 : auto_now=True 사용
    **auto_now=True 는 django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됩니다.
    주로 최종수정일자 field option 으로 주로 사용됩니다. 
  - **created_at  > 생성일자 : auto_now_add=True 사용**
    auto_now_add=True 는 django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용합니다.
