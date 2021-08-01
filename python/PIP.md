

# 파이썬 패키지 관리자 (pip)

[https://pypi.org/]()

![image-20210728160831682](/Users/euijinpang/TIL/python/PIP.assets/image-20210728160831682.png)

- 패키지는 모듈의 집합이다



## 파이썬 패키지 관리자 명령어

##### 패키지 설치

```bash
# 최신 버전
pip install Somepackage
# 특정 버전
pip install Somepackage == 1.0.5
# 최소 버전
pip install 'Somepackage >= 1.0.4'
```

##### 삭제하기

- pip는 패키지 업그레이드시 과거 버전을 자동으로 지워줌

```bash
pip uninstall Somepackage
```

##### 현재 환경에 설치된 pip 목록 확인

```bash
pip list
```

##### 특정 패키지 정보 확인

```bash
pip show Somepackage
```

##### 패키지 freeze

- 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용하는 형식으로 출력
- 해당 목록을 requirements.txt(관습) 으로 만들어 관리한다.

```bash
# show in bash
pip freeze
# save file
pip freeze > requirements.txt
```

##### 패키지 관리하기

- 아래 명령어를 통해 패키지 목록을 1) 관리 2) 설치 할 수 있음
- 다른 환경에 설치할 수 있음
- 일반적인 패키지 관리파일명은 **requirements.txt** 동일명 필수!!

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```





## 가상환경

- 전체 설치시 하나의 버전밖에 사용할 수 없는 상황 (global environment)
- 하나의 컴퓨터로 여러개의 프로젝트를 진행하는 경우? --> 버전이 상이할 수 있음
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지 관리



![image-20210728161000380](/Users/euijinpang/TIL/python/PIP.assets/image-20210728161000380.png)



### venv

- `venv module (Python ver. 3.5~)`

- 특정 디렉토리에 가상 환경을 만들고 고유한 파이썬 패키지 집합을 가진다

  - 특정 폴더에 가상환경이 있고 모두 독립적, 영향주지 않는다.(글로벌 포함)

  - 실행 환경에서 가상환경을 활성화

  - 해당 폴더에 있는 패키지를 관리 / 사용

    

##### 가상환경 생성

- 파일명은 venv 로 관습적으로 만든다

```bash
python -m venv <folder name>
# python -m venv venv 
```

![image-20210728094109324](/Users/euijinpang/TIL/python/PIP.assets/image-20210728094109324.png)





##### 가상환경 활성화

- 폴더에 국한된 것이 아님! 다른 폴더로 가도, 실행중이기 때문에 따로 꺼야 한다

![image-20210728094056211](/Users/euijinpang/TIL/python/PIP.assets/image-20210728094056211.png)

- mac

```bash
source <venv>/bin/activate
# source venv/bin/activate
```

- window

```bash
source <venv>/Scripts/activate
# source venv/Scripts/activate
```



##### 비활성화

```bash
deactivate
```



- 다른 경로에서 venv를 불러올 수는 있지만,
- 각 프로젝트별로 폴더를 만들어, 그 최상단에 venv를 만드는 것이 일반적이다
- 여러개 프로젝트시, 환경을 비활성화 해야!

![image-20210728100643489](/Users/euijinpang/TIL/python/PIP.assets/image-20210728100643489.png)

![image-20210728102302335](/Users/euijinpang/TIL/python/PIP.assets/image-20210728102302335.png)



- venv이 아닌 requirements 를 git에 올려 공유한다.
- 함부로 파일을 옮기면 경로가 바뀌어 드래그하거나 복사하면 안된다. 
- 반드시 requirements.txt 를 통해 서로의 환경을 맞추어야 한다!



![image-20210728102235949](/Users/euijinpang/Library/Application Support/typora-user-images/image-20210728102235949.png)



## 모듈과 패키지 활용하기

### 모듈 만들기

##### check모듈 만들기

check.py 모듈에 짝수판별함수(even) 과 홀수판별함수(odd)를 만든다

```python
# check.py

def odd(n):
	return bool(n%2)

def even(n):
	return not bool(n%2)
```

### 모듈 활용하기

import 문을 통해 가져온다

```python
import check
dir(check) # 모듈 내 확인

check.odd(3) # true
```

```python 
from check import odd
odd(5) # true

from check import * # import all
```





### 패키지 만들고 활용하기

패키지는 여러 모듈과 하위 패키지로 구조화 `package.module`

모든 폴더에는 `__init__.py` 를 만들어 패키지로 인식 for 하위버젼 호환



##### 수학과 통계 기능이 들어간 패키지

- `math`의 tools 모듈 : 자연상수 e, 원주율 pi값, 최대값을 구하는 my_max 함수
- `statistics`의 tools 모듈 : 평균을 구하는 mean 함수
- 폴더 구조

```python
# tools.py
pi = 3.141592

def my_max(number):
  return number ** 3
```

```python
# tools.py
def mean(x):
  return sum(x) / len(x)
```

```python
my_package/
	__init__.py
	math/
		__init__.py
		tools.py
	statistics/
			__init__.py
			tools.py
```

```python
# my package 안에 math 패키지를 쓰기위해 tools 모듈을 가져온다
from my_package.math import tools
print(tools.my_max(3))
print(tools.pi)
# => 27
# => 3.141592

from my_package.math.tools import *
print(my_max(5))
# => 125

from my_package.statistices import tools
print(tools.mean([1, 2, 3]))
# => 2.8

# module 이름이 같은 경우 해당 환경 내에서만 as 로 바꿀 수 있다
from my_package.math import tools as math_tools
from my_package.statistics import tools as stat_tools

print(math_tools.my_max(4))
# => 64
```



