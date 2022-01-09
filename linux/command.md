# command-line interface(CLI)

> 리눅스 기본 명령어 정의



## 형태

command + -option(커맨드를 어떻게 실행할 것인지) + argument(어느 대상에 대해 실행할 것인지)



## 매뉴얼

man + argument(command)

- 올리기 b, 내리기 spaceber, 나오기 q



## 기호

- $ : prompt
- / : Root directory
- ~ : Home directory (/Users/euijinpang)
- . : 현재 위치한 폴더를 지칭
- .. : 현재 위치한 폴더를 기준으로 상위 폴더를 지칭



## 단축키

- tab : 파일/폴더 이름 자동완성 기능
- ctrl+c : 실행중인 프로세스 취소
- 키보드 방향키 위 아래 : 이전에 입력한 명령어 기록 탐색
- control + A , E : 커서 맨 앞뒤 이동
- option + 화살표 : 단어 이동
- clear + Enter : 화면 클리어



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

- 특정 이름으로 시작하는 파일 찾기

```
ls |grep <keyword>
```



##### cd (change directory)

- 해당 위치로 이동하는 명령어
  - `..`은 상위 폴더를 의미한다.

```bash
cd <folder name>
```



## 검색

- 디렉토리의 정보를 다양한 열과 함께 테이블 포맷으로 보여준다
- List files in long format

```
ll
or
ls -l
```

- 디렉토리만 보여준다
- List only directories

```
ls -d */
```

- 숨겨진 파일까지 보여준다
- List files in long format including hidden files

```
la -a
```

- 최근 수정된것을 먼저 보여준다
- List files and sort by date and time

```
ls -t
ls -tr(역순)
```

- 사이즈별로 보여준다(큰것부터 작은것까지)
- List files and sort by file size

```
ls -S
ls -Sr(역순)
```

- 파일사이즈 단위와 함께 보여준다
- List files in long format with readable file sizes

```
ls -lh
```

- 섞어서 사용한다
- 숨김파일 + 역순 + 리스트로 + 변경순서별 + 파일사이즈

```
ls -arlth
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



## 읽기 & 수정하기

##### cat (concatenate)

- 파일 읽기

```bash
cat <option> <file name>
```

- 파일 여러개 읽기

```bash
cat <file1> <file2> <file3>
```

- 파일 여러개 합쳐 큰 파일 만들기 
  - 세 개의 합쳐 새로운 file 4 를 만든다.

```bash
cat <file1> <file2> <file3> > <file4>
```

- 기존 파일에 덧붙이기
  - 기존에 있는 file2에 file1의 내용을 덧붙이며, 새로운 파일이 생성된다.

```bash
cat <file1> >> <file2>
```

- 새로운 파일 만들기
  - touch <file name> 과 같지만 명령어 입력 후 표준입력으로 내용을 입력, CTRL-d 를 입력하면 새로운 내용이 저장된 새로운 파일이 만들어진다.

```bash
cat > <file name>
```



## 삭제

##### rm (remove)

- 파일 삭제

```bash
rm <file name>
```

- 지정한 폴더 및 파일 경고없이 강제 삭제 => 쓰지 않는다!!

```bash
rm -rf <file name>
```

- 해당 폴더 안의 모든 파일 삭제

```bash
rm -f * 
```

- 파일 삭제할 때 확인하기

```bash
rm -ri 
```

- 같은 형식의 파일 전부 제거

```bash
rm *.exe
```

- 디렉토리 삭제(파일 및 폴더 삭제)

```bash
rm -r folder/
```



## 확인

- 경로 확인

```bash
tree folder/
```

