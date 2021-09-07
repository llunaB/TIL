# command

> 리눅스 기본 명령어 정의



## 기호

- $ : prompt
- / : Root directory
- ~ : Home directory
- . : 현재 위치한 폴더를 지칭
- .. : 현재 위치한 폴더를 기준으로 상위 폴더를 지칭



## 단축키

- tab : 파일/폴더 이름 자동완성 기능
- ctrl+c : 실행중인 프로세스 취소
- 키보드 방향키 위 아래 : 이전에 입력한 명령어 기록 탐색



## 이동

##### pwd (print working directory)

- 현재 나의 위치를 확인하는 명령어

```bash
pwd
```



##### ls (list)

- 현재 나의 위치에 있는 파일과 폴더들을 보여주는 명령어
  - -a 옵션을 사용하면 숨김폴더, 파일까지 확인할 수 있다.
  - `.`은 현재 폴더, `..`은 상위폴더를 의미한다.

```bash
ls
ls -a
```



##### cd (change directory)

- 해당 위치로 이동하는 명령어
  - `..`은 상위 폴더를 의미한다.

```bash
cd <folder name>
```



## 생성

##### mkdir (make directory)

- 폴더를 생성하는 명령어

```bash
mkdir <folder name>
```



##### touch

- 파일을 생성하는 명령어

```bash
touch <file name>
```



## 삭제

##### rm (remove)

- 파일 삭제

```bash
rm <file name>
```

- 지정한 폴더 및 파일 삭제 

```bash
rm -r <file name>
```

- 지정한 폴더 및 파일 강제 삭제 => 쓰지 않는다!!

```bash
rm -rf <file name>
```

