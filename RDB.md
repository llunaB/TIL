## RDB

- 관계형 데이터베이스

**python** => (makemigrations) => **schema** => (migrate) => **Table**

- 행 = 로우 = 레코드
- 기본키(Primary Key) : 각 행(레코드)의 기본값



## RDBMS

- 표로 만들어진 관계형 데이터베이스를 관리하는 시스템

- 모두 **SQL 문법** 을 사용

  ![image-20210914091546989](/Users/euijinpang/TIL/RDB.assets/image-20210914091546989.png)



## Django

- settings.py

![image-20210914091820947](/Users/euijinpang/TIL/RDB.assets/image-20210914091820947.png)



## SQLite

- 서버 형태가 아닌 파일 형식으로 응용프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스



## 설치

- 맥은 설치되어있음
- 윈도우는 가이드 따라 설치 - 명령어 통일 등 



## SQLite 명령어

- 실행

```bash
 ~ % sqlite3
```

- 종료

```bash
.exit
```

- 파일 실행 

```bash
sqlite3 tutorial.sqlite3 
```

- 생성

sqlite > .database

![image-20210914094603397](/Users/euijinpang/TIL/RDB.assets/image-20210914094603397.png)

![image-20210914094334295](/Users/euijinpang/TIL/RDB.assets/image-20210914094334295.png)

![image-20210914094847698](/Users/euijinpang/TIL/RDB.assets/image-20210914094847698.png)

![image-20210914095033633](/Users/euijinpang/TIL/RDB.assets/image-20210914095033633.png)

![image-20210914100256157](/Users/euijinpang/TIL/RDB.assets/image-20210914100256157.png)

- ; 필수
- .header 등은 프로그래밍 명령어라 ; 필요없지만 그 외에는 끝날때 ; 를 붙여줘야만 문장이 끝났다고 할 수 있다.

- 대소문자 구분하지 않는다. 구분은 convention으로, 문법은 대문자로, 변수는 소문자로 작성한다.

.shell clear



![image-20210914100629497](/Users/euijinpang/TIL/RDB.assets/image-20210914100629497.png)

![image-20210914100705144](/Users/euijinpang/TIL/RDB.assets/image-20210914100705144.png)

![image-20210914100717836](/Users/euijinpang/TIL/RDB.assets/image-20210914100717836.png)



![image-20210914100744842](/Users/euijinpang/TIL/RDB.assets/image-20210914100744842.png)



![image-20210914101104294](/Users/euijinpang/TIL/RDB.assets/image-20210914101104294.png)

![image-20210914102044126](/Users/euijinpang/TIL/RDB.assets/image-20210914102044126.png)

```bash
# 터미널 껐다 켰을때
sqlite3 tutorial.sqlite3
```

- 빠져나오기



## SQL(Structured Query Language)

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리

![image-20210914110640521](/Users/euijinpang/TIL/RDB.assets/image-20210914110640521.png)

## 분류

![image-20210914093547744](/Users/euijinpang/TIL/RDB.assets/image-20210914093547744.png)

- 조작언어는 각각 CRUD와 대응됨



## 정의





## SQL과 No-SQL

- Django에서 연동만 시켜주면 모든 DBMS 사용이 가능하다

#### SQL Database

- SQL - relational databse
- MySQL, Maria DB, Oracle 등 RDBMS

#### NoSQL Database

각각 문법이 다르다

- MongoDB(자바스크립트), Firebase(리얼타임) => json, 딕셔너리 형태





sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables



![image-20210914125505839](/Users/euijinpang/TIL/RDB.assets/image-20210914125505839.png)

![image-20210914130523956](/Users/euijinpang/TIL/RDB.assets/image-20210914130523956.png)

![image-20210914131433032](/Users/euijinpang/TIL/RDB.assets/image-20210914131433032.png)

![image-20210914133257298](/Users/euijinpang/TIL/RDB.assets/image-20210914133257298.png)

![image-20210914133417972](/Users/euijinpang/TIL/RDB.assets/image-20210914133417972.png)

![image-20210914134311609](/Users/euijinpang/TIL/RDB.assets/image-20210914134311609.png)





## 장고

열기 sqlite3 db.sqlite3

- users_user 테이블을 다룰 것!

.headers on   => 헤더 열기

.exit => sql 닫기

SELECT * FROM users_user;



.query 붙이면 쿼리셋 볼수있다.





![image-20210914135746202](/Users/euijinpang/TIL/RDB.assets/image-20210914135746202.png)

![image-20210914140344091](/Users/euijinpang/TIL/RDB.assets/image-20210914140344091.png)



sqlite3 db.sqlite3

python manage.py shell_plus



|                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| SELECT * FROM users_user;                                    | User.objects.all()                                           |
| ''                                                           | User.objects.all().query                                     |
| INSERT INTO users_user VALUES (102, '길동', '김', 20, '서 울', '010-1234-1234', 100); | User.objects.create(first_name='길동',<br/>   ...:    ...: last_name='홍',<br/>   ...:    ...: age=10,<br/>   ...:    ...: country='제주',<br/>   ...:    ...: phone='010-1234-1234',<br/>   ...:    ...: balance=100,<br/>   ...:    ...: ) |
| SELECT * FROM users_user WHERE id=102;                       | User.objects.get(pk=102)                                     |
|                                                              | 수정 1. 가지고와서 2. 변수저장 3. 바꾸고 4. save             |
| UPDATE users_user<br/>   ...> SET first_name='철수'<br/>   ...> WHERE id=102; | In [4]: User.objects.get(pk=102)<br/>Out[4]: <User: User object (102)><br/><br/>In [5]: user = User.objects.get(pk=102)<br/><br/>In [6]: user<br/>Out[6]: <User: User object (102)><br/><br/>In [7]: user.last_name<br/>Out[7]: '김'<br/><br/>In [8]: user.last_name = '홍'<br/><br/>In [9]: user.save()<br/><br/>In [10]: user.last_name<br/>Out[10]: '홍' |
| DELETE FROM users_user WHERE id=101;                         | In [14]: user = User.objects.get(pk=100)<br/><br/>In [15]: user.delete() |
| SELECT COUNT(*) FROM users_user;                             | In [16]: len(User.objects.all())<br/>Out[16]: 100<br/><br/>In [17]: User.objects.count()<br/>Out[17]: 100 |
|                                                              | method(key=value) 정해져있어서 .filter(age>=30) 못쓴다. lookup사용해야. . django field lookup |
| SELECT COUNT(*) FROM users_user WHERE age>=30;               | User.objects.filter(age__gte=30).count()                     |
| SELECT COUNT(*) FROM users_user WHERE age<=20;               | User.objects.filter(age__lte=20).count()                     |
|                                                              | User.objects.filter(Q(age=30)\|Q(last_name='김')).count()    |
|                                                              |                                                              |
|                                                              |                                                              |

