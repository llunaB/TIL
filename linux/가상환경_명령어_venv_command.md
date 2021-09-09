# 가상환경 명령어



### 1. 가상환경 생성하기

- 일반적으로 <name>에는 venv를 사용

```python
python -m venv <name>
```



### 2. 기존의 가상환경 적용하기

- 꼭 가상황경 생성 후 적용해야한다. 그렇지 않으면 전역 pip list 가 모두 나온다.

```python
pip install -r requirements.txt
```



### 3. 변경된 사항을 반영하기 또는 새 패키지 만들기

```python
pip freeze > requirements.txt
```



### 4. 가상환경 활성화하기

```bash
# Window OS
source <name>(보통 venv)/Scripts/activate
```

```bash
# mac os
source <name>/bin/activate
```



### 6. 가상환경 패키지 확인하기

```
pip list
```



### 5. 가상환경 종료하기

```python
deactivate
```