# MySQL

- 서버 끊기

```mysql
mysql> QUIT
```

- 기존 데이터베이스 확인

```mysql
mysql> SHOW DATABASES;
```

- 새 데이터베이스 생성

```mysql
mysql> CREATE DATABASE pets;
```

- 데이터베이스 내부에 테이블 생성

```mysql
mysql> USE pets
```

```mysql
CREATE TABLE cats
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the cat
  owner           VARCHAR(150) NOT NULL,                # Owner of the cat
  birth           DATE NOT NULL,                        # Birthday of the cat
  PRIMARY KEY     (id)                                  # Make the id the primary key
);
```

- 테이블의 모든 열에 대한 정보 표시

```mysql
mysql> DESCRIBE cats;
```

- 테이블에 레코드 추가

```mysql
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Sandy', 'Lennon', '2015-01-03' ),
  ( 'Cookie', 'Casey', '2013-11-13' ),
  ( 'Charlie', 'River', '2016-05-21' );
```

- 테이블에서 레코드 검색

```mysql
mysql> SELECT * FROM cats;
```

- 특정 조건에 따른 선택

```mysql
mysql> SELECT name FROM cats WHERE owner = 'Casey';
```

- 테이블에서 레코드 삭제

```mysql
mysql> DELETE FROM cats WHERE name='Cookie';
```

- 테이블에서 열 추가

```mysql
mysql> ALTER TABLE cats ADD gender CHAR(1) AFTER name;
```

- 테이블에서 열 삭제

```mysql
mysql> ALTER TABLE cats DROP gender;
```



### 예시

```mysql
SELECT

F.title AS FilmTitle,
CONCAT(A.first_name, ' ', A.last_name) AS ActorName

FROM film F

LEFT JOIN film_actor FA
ON F.film_id = FA.film_id

LEFT JOIN actor A
ON A.actor_id = FA.actor_id

LIMIT 100;
```

![image-20211213221143982](MySQL_명령어.assets/image-20211213221143982.png)

![image-20211213221335299](MySQL_명령어.assets/image-20211213221335299.png)