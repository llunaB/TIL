# listen port & pid 확

맥 환경에서 포트 정보를 확인하고, 모르는 포트를 열어놓은 프로세스가 있는지 확인.



- lsof (list open files) 이용시

```bash
sudo lsof -iTCP -sTCP:LISTEN -n -P
```



- netstat 이용시

```bash
netstat -anv | grep LISTEN
```



- LISTEN 포트, 프로세스와 TCP 세션 전부 조회

```bash
sudo lsof -i -n -P | grep TCP
```



- 특정 서버 포트 상태를 보고 싶을 경우

```bash
sudo lsof -i:포트번호
```

```bash
netstat -anv|greo '<포트번호>'
```



- pid만 찾을 경우

```bash
lsof -t -t:포트번호
```



- IPv4 (TCP & UDP)

```bash
lsof -i 4
```



- IPv6 (TCP & UDP)

```bash
lsof -i 6
```





