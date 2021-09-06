# django 실행순서



### 1. 루트폴더 생성 및 폴더 내 이동

```python
mkdir <folder name>
cd <folder name>
```



### 2. 가상환경 생성

```python
python -m venv <name>
```

일반적으로 <name>에는 venv를 사용



참고) 적용

```python
pip install -r requirements.txt
```

참고 ) 변경된 사항을 반영

```python
pip freeze > requirements.txt
```



### 3. 가상환경 실행

```bash
# Window OS
source <name>/Scripts/activate
```

```bash
# mac os
source <name>/bin/activate
```

참고 ) 가상환경 종료

```python
deactivate
```

- 활성화

```bash
source venv/bin/activate
```



### 4. 장고 설치

```python
pip install django
```



---



### 5 .gitignore , README.md 파일만들기

- .gitignore 로 만든 후, 웹사이트 들어가 내용 복사 붙여넣기
- venv 도..

![image-20210901124518417](images/image-20210901124518417.png)

```python
touch README.md .gitignore
```



### 5-2. git 등록



### 6. 장고 프로젝트 (폴더)생성

- '.' 을 찍어야, 프로젝트 폴더와 manage.py 가 동일경로에 위치

```python
django-admin startproject <name> .
```

- 잘못 생성하면?

```python
rm -rf <project name>/ manage.py
```



### 7. 장고 앱 생성 및 등록

- **이때 앱 이름은 반드시 (모델에 작성한 클래스의) 복수형으로 사용! (articles 등)**

```python
python manage.py startapp <name>
```

- **생성 후에는 무조건 등록! (project folder 내의 settings.py)**
  - local apps - 생성한 앱
  - 3rd party apps  - 'django_extensions'
  - django apps

![image-20210902191351264](images/image-20210902191351264.png)



---



### 추가설정 settings.py

- 한국어 설정

```python
LANGUAGE_CODE = 'ko-kr'
```

- 한국시간 설정

```python
TIME_ZONE = 'Asia/Seoul'
```
