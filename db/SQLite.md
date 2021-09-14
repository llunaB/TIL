# SQLite

- 서버 형태가 아닌 파일 형식으로 응용프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스

- Django 기본설정

  - settings.py

  ![image-20210915004710479](image/image-20210915004710479.png)



- SQLite는 따로 `primary key` 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK 옵션을 가진 `rowid` 컬럼을 정의

  ```sql
  SELECT rowid, * FROM tablename;
  ```

  

## 설치

- 맥은 설치되어있음
- 윈도우는 가이드 따라 설치 - 명령어 통일 등 



## 주의사항

- `.headers on` 등은 프로그래밍 명령어라 ` ;` 필요없지만 그 외에는 끝날때 `;` 를 붙여줘야만 문장이 끝났다고 할 수 있다.
- 대소문자 구분하지 않는다. 구분은 convention으로, 문법은 대문자로, 변수는 소문자로 작성한다.



## 명령어(macOS)

- 실행 전 가상환경 셋팅!

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- 최초 실행

```bash
sqlite3
```

- 종료

```bash
.exit
```

- **sqlite 실행**

```bash
# 터미널 껐다 켰을때
sqlite3 tutorial.sqlite3 
```

- 데이터베이스 생성

```bash
.database
```

- csv 파일을 데이터베이스에 적용하기

```bash
.mode csv
.import hellodb.csv 테이블명
.tables
```

- 헤더 보기

```bash
.headers on
```

- 열로 보기

```bash
.mode colum
```

- 스키마보기

```bash
.schema 테이블명
```

- 터미널 정리하기

```bash
.shell clear
```



## Table 

- 테이블 생성하기

```sql
CREATE TABLE tablename (
id INTEGER PRIMARY KEY,
name TEXT
);
```

- 테이블 삭제하기

```sql
DROP TABLE tablename;
```

- 테이블명 변경하기

```sql
ALTER TABLE 기존이름 RENAME TO 새이름;
```





## 추가개념

### AUTOINCREMENT

```sql
CREATE TABLE tablename (
INTEGER PRIMARTY KEY AUTOINCREMENT,
...
);
```



### WILDCARDS

- % , _ 

```sql
SELECT * FROM 테이블 WHERE 컬럼 LIKE 'wildcardpattern'
```



### ORDER BY

- 특정 컬럼 기준으로 데이터 정렬하기
  - ASC : 오름차순
  - DESC : 내림차순

```sql
SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2 DESC;
```



### Agrregation

- COUNT
- SUM
- MAX
- MIN



### GROUP BY

- 지정된 기준에 따라 행 세트를 그룹으로 결합
- 데이터를 요약하는 상황에서 사용

```sql
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
```

