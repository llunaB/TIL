# vscode error & solution

> vscode 에러 및 해결방법



### default interpreter 'Python 3.9.6' not 3.9.6:pyenv

##### 문제점

설치한 `requests` 모듈을 `vscode`에서 인식하지 못함

<img src="vscode_error_solution.assets/image-20210731155559927.png">



##### 원인

vscode가 기본 인터프리터 경로를 `Python 3.9.6` 으로 잡고있었다.

그러나 terminal 에서는 맥으로 파이썬 설치시 `pyenv` 로 설치하였기 때문에

3.9.6 pyenv가 디폴트였고, 이 경우 terminal 에서  `third-party library`, `module` 설치시 인식못함



##### 해결방법

- Change defauly Python interpreter path to `Python 3.9.6 : pyenv`

<img src="vscode_error_solution.assets/Screen Shot 2021-07-31 at 3.58.05 PM.png">

