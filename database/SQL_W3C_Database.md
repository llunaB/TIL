[TOC]

# DB 

## DB 생성

```sql
CREATE DATABASE databasename;
```

## DB 제거

```sql
DROP DATABASE databasename;
```

## DB 백업

💡실제 데이터베이스와 다른 경로에 보관해야 디스크 충돌 나도 보존이 가능하다.

### 전체 백업

```sql
BACKUP DATABASE databasename
TO DIST = 'filepath';
```

### 부분 백업

마지막 백업 상태에서 변한 부분만 백업하며 속도가 빠르다.

```sql
BACKUP DATABASE databasename
TO DIST = 'filepath';
WITH DIFFERENTIAL;
```



# Table

## Table 생성

컬럼과 데이터 타입을 넣어 테이블을 생성한다.

```sql
CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
  ...);
```

```sql
CREATE TABLE Persons (
  Person ID int,
  LastName varchar(255),
  FirstName varchar(255),
  Address Varchar(255),
  City Varchar(255)
);
```

### 기존 Table로 새로운 Table 생성

기존 테이블에서 원하는 컬럼을 가져와 새로운 테이블을 생성할 수 있으며, 이때 value는 기존 테이블 것이 그대로 채워진다.

```sql
CREATE TABLE new_table_name AS
SELECT column1, column2, ...
FROM existing_table_name
WHERE ...;
```

## Table 삭제

```sql
DROP TABLE table_name;
```

### Table 안의 data 만 삭제

```sql
TRUNCATE TABLE table_name;
```



## ALTER TABLE

존재하는 테이블에서 `columns` 를 더하고, 삭제하고, 수정할 수 있는 구문이다.

또한 다양한 `constraints` 를 추가하거나 삭제할 수도 있다.



👉 데이터 타입은 여기를 참고! https://www.w3schools.com/sql/sql_datatypes.asp



### Column 더하기

```sql
ALTER TABLE table_name
ADD column_name datatype;
```

이메일 컬럼을 고객 테이블에 더해보자.

```sql
ALTER TABLE Customers
ADD Email varchar(255);
```



### Column 삭제하기

ADD 와는 다르게 COLUMN 추가

```sql
ALTER TABLE table_name
DROP COLUMN column_name datatype;
```

이메일 컬럼을 고객 테이블에서 삭제해보자.

```sql
ALTER TABLE Customers
DROP COLUMN Email;
```



### Column 수정하기 (데이터 타입 변경하기)

- SQL

```sql
ALTER TABLE table_name
ALTER COLUMN column_name datatype;
```

- MySQL

```mysql
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

- Oracle

```sql
ALTER TABLE table_name
MODIFY column_name datatype;
```



# Contraints

테이블 안의 데이터를 제약하기 위한 요소들



## Constraints 생성하기

테이블 생성할 때 넣거나, 이미 만들어진 테이블을 ALTER 하여 추가한다.

```sql
CREATE TABLE table_name (
  column1 datatype constraint,
  column2 datatype constraint,
  ...
);
```

데이터 타입을 제약하여 정확성과 신뢰성을 높인다.

컬럼 레벨, 테이블 레벨로 설정이 가능하며 각각 적용범위가 다르다.

다음은 자주 쓰이는 제약사항이다.

차례대로 살펴보자.



- `NOT NULL` - Ensures that a column cannot have a NULL value
- `UNIQUE` - Ensures that all values in a column are different
- `PRIMARY KEY` - A combination of a `NOT NULL` and `UNIQUE`. Uniquely identifies each row in a table
- `FOREIGN KEY` - Prevents actions that would destroy links between tables
- `CHECK` - Ensures that the values in a column satisfies a specific condition
- `DEFAULT` - Sets a default value for a column if no value is specified
- `CREATE INDEX` - Used to create and retrieve data from the database very quickly



## NOT NULL

- 사용 안할 때 : `column` 은 `NULL` 값을 가질 수 있다.
- 사용시 :  `column` 은 `NULL` 값을 가질 수 **없다.**

### table 생성시

데이터 추가시 해당 필드는 반드시 채워넣어야 한다.

```sql
CREATE TABLE Persons (
  ID int NOT NULL,
  LastName varchar(255) NOT NULL,
  FirstName varchar(255) NOT NULL,
  Age int
);
```

### table 수정시

기존 테이블 수정시 - Age 컬럼에 추가해보자.

```sql
ALTER TABEL Persons
MODIFY Age int NOT NULL;
```



## UNIQUE

- 사용시 :  `column` 의 `all values` 는 달라야 한다.
- `PRIMARY KEY` 는 이미 이 제약을 가지고 있다.

### table 생성시

- SQL

```sql
CREATE TABLE Persons (
  ID int NOT NULL UNIQUE,
  LastName varchar(255) NOT NULL,
  FirstName varchar(255),
  Age int
);
```

- MySQL

```sql
CREATE TABLE Persons (
  ID int NOT NULL,
  LastName varchar(255) NOT NUll,
  FirstName varchar(255),
  Age int,
  UNQUE (ID)
);
```

이름을 따로 붙이고 싶거나 여러 개의 컬럼에 적용하고 싶다면 다음을 사용하자.

MySQL, SQK, Oracle 공통이다.

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
  	CONSTRAINT UC_Person UNIQUE (ID, LastName)
);
```

### table 수정시

MySQL, SQK, Oracle 공통이다.

ID 컬럼에 제약을 걸어보자.

```sql
ALTER TABLE Persons
ADD UNIQUE (ID);
```

이름을 따로 붙이고 싶거나 여러 개의 컬럼에 적용하고 싶다면 다음을 사용하자.

```sql
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);
```



### 제약사항 삭제하기

MySQL

```sql
ALTER TABLE Persons
DROP INDEX UC_Person;
```

Others

```sql
ALTER TABLE Persons
DROP CONSTRAINT UC_Person;
```



## PRIMARY KEY

`PRIMARY KEY` 는 테이블의 각 레코드를 구분하는 유니크한 제약이다.

`NULL` 값을 가질 수 없다.

한 테이블은 단 `한 개` 의 프라이머리 키를 가질 수 있으며, 이 프라이머리 키는 하나 또는 여러 개의 컬럼으로 이루어질 수 있다.

### table 생성시

MySQL

```mysql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
```

Others

```sql
CREATE TABLE Persons (
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);
```

따로 이름을 붙이거나 여러 개의 컬럼으로 `PRIMARY KEY`를 구성하고 싶다면 다음과 같이 실행한다. (디비공통)

```sql
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
  	CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);
```

👉 **이 예제에서 `PRIMARY KEY` 는 `PK_Person` 한 개이다. 그러나 `PRIMARY KEY`  의 `value` 는 두 개의 `column` 으로부터 만들어졌다! (ID + LastName)**



### table 수정시

`ID` 컬럼에 프라이머리 키를 추가해보자.

```sql
ALTER TABLE Persons
ADD PRIMARY KEY (ID);
```

💡프라이머리 키를 추가하고 싶다면, 그 해당 컬럼은 NULL 값을 가질 수 없도록 처음부터 선언되어야 한다.

```sql
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID, LastName);
```



### PRIMARY KEY 제약 삭제하기

MySQL

```mysql
ALTER TABLE Persons
DROP PRIMARY KEY;
```

Others

```sql
ALTER TABLE persons
DROP CONSTRAINT PK_Persons;
```



## FORIEGN KEY

`FOREIGN KEY` 란 테이블의 하나의 필드로, 다른 테이블의 `PRIMARY KEY` 를 참조하는 필드를 의미한다.

`FOREIGN KEY` constraint 는 외래키에 유효하지 않은 데이터가 들어오는 것을 방지한다. 왜냐하면 반드시 부모테이블의 데이터중 하나여야 하기 때문이다.



### table 생성시

Orders 테이블을 생성할 때, PersonID 컬럼에 외래키를 설정하자.

MySQL

```mysql
CREATE TABLE Orders (
	OrderID int NOT NULL,
  OrderNumber int NOT NULL,
  PersonID int,
  Primary KEY (OrderID),
  /* Persons 테이블의 PersonID 를 참조한다는 뜻 */
  FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

Others

```sql
CREATE TABLE Orders (
  OrderID int NOT NULL PRIMARY KEY,
  OrderNumber int NOT NULL,
  PersonID int FOREIGN KEY REFERENCES Persons(PersonID)
);
```



### table 수정시

Orders 테이블의 PersonID 컬럼에 외래키를 설정해보자.

DB 공통

```sql
ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
```

이름을 짓거나 여러 컬럼에 대해 외래키를 설정하고 싶다면 다음과 같이 해보자.

```sql
ALTER TABLE Orders
ADD CONSTRAINT FK_PersonOrder
FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
```



### FORIEGN KEY 제약 삭제하기

MySQL

```sql
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;
```

Others

```sql
ALTER TABLE Orders
DROP CONSTRAINT FK_PersonOrder;
```



## CHECK

## DEFAULT

## CREATE INDEX

