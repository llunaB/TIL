# Docker 명령어 정리



- 버젼 확인

```bash
docker -v
```



- 도커 컨테이너 실행 (이미지 다운로드와 실행을 한 번에 진행)

  - ```
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    2db29710123e: Pull complete 
    Digest: sha256:2498fce14358aa50ead0cc6c19990fc6ff866ce72aeb5546e1d59caac3d0d60f
    Status: Downloaded newer image for hello-world:latest
    ```

  - ```
    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
     3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.
    ```

```bash
docker run [컨테이너 이름] 
```



- 모든 컨테이너 조회 ( -a 옵션은 정지(실행 종료)된 컨테이너까지 조회하는 옵션)

```bash
docker ps -a
```



- 현재 실행중인 컨테이너만 보기

```bash
docker ps 
```



- 특정 컨테이너 삭제 (컨테이너 ID는 앞 부분 2자리만 입력 가능)

```bash
docker rm [컨테이너 ID 또는 NAME]
```



- 도커 이미지 조회

```bash
docker images
```



- 특정 도커 이미지 삭제
  - TAG중 최신을 의미하는 latest 태그명은 생략 가능

```bash
docker rmi [이미지 ID (앞부분 2자리 가능) 또는 이미지명: TAG명]
```



### Jenkins 

- Jenkins를 도커 컨테이너로 실행
  - `--name` : 원하는 이름 설정
  - `-d` : 백그라운드 데몬으로 실행
  - `-p` : 가상 머신(Guest PC) 에서 동작하는 서비스에 docker proxy 서비스가 NAT 기능을 수행, 포트 포워딩을 해주어 실제 머신(Host PC) 의 IP로 서비스에 접속이 가능하도록 해준다.
  - 팁 : 컨테이너 삭제시 생성된 데이터가 함께 삭제되므로 보통 호스트 pc의 디렉토리에 데이터가 생성되도록 컨테이너에는 볼륨 마운트 옵션을 추가하여 실행시킨다.
  - `-v` : 볼륨 마운트 옵션 *-v your/home:/var/jenkins_home*

```
docker run --name ej_jenkins -d -p 9080:8080 jenkins/jenkins
```



- Jenkins 서버 컨테이너의 bash 실행
  - Jenkins 컨테이너에는 bash가 포함되어 있지만 없는 서비스의 경우 bash대신 sh 사용 가능
  - `-i` : interactive 모드로 표준 입출력을 키보드와 화면을 통해 가능하도록 하는 옵션
  - `-t` : 텍스트 기반의 터미널(TTY) 를 에뮬레이션 해주는 옵션
  - `-it` : 두 옵션을 합친 옵션

```bash
docker exec -it ej_jenkins bash
```



- 컨테이너의 OS 버젼 확인

```bash
jenkins@92552ea0b836:/$ cat /etc/issue
Debian GNU/Linux 11 \n \l
```



- 컨테이너 안(bash) 에서 Admin 패스워드가 저장된 파일 확인

```
jenkins@92552ea0b836:/$ cat /var/jenkins_home/secrets/initialAdminPassword
```



- 컨테이너 bash 종료

```
jenkins@92552ea0b836:/$ exit
```



- 기타 패스워드 확인

```
docker logs ej_jenkins
```



- 컨테이너 안의 패스워드 파일을 개발 PC로 복사

  - ```bash
    docker cp 파일명 myjenkins:/var/jenkins_home
    ```

  - ```
    docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
    ```

```
docker cp ej_jenkins:/var/jenkins_home/secrets/initialAdminPassword ./
```

```
ls
```



- 컨테이너 제시작

```
docker restart ej_jenkins
```



- 컨테이너 삭제
  - `-f` : 실행중인 컨테이너도 강제 삭제 가능

```bash
docker rm ej_jenkins
docker rm -f ej_jenkins
```





### Usage

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

```
Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the container
      --cgroupns string                Cgroup namespace to use (host|private)
                                       'host':    Run the container in the Docker host's cgroup namespace
                                       'private': Run the container in its own private cgroup namespace
                                       '':        Use the cgroup namespace as configured by the
                                                  default-cgroupns-mode option on the daemon (default)
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
  -d, --detach                         Run container in background and print container ID
      --detach-keys string             Override the key sequence for detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
      --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
      --device-read-iops list          Limit read rate (IO per second) from a device (default [])
      --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second) to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --domainname string              Container NIS domain name
      --entrypoint string              Overwrite the default ENTRYPOINT of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --gpus gpu-request               GPU devices to add to the container ('all' to pass all GPUs)
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to report unhealthy
      --health-start-period duration   Start period for the container to initialize before starting
                                       health-retries countdown (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container that forwards signals and reaps processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC mode to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the container
      --name string                    Assign a name to the container
      --network network                Connect a container to a network
      --network-alias list             Add network-scoped alias for the container
      --no-healthcheck                 Disable any container-specified HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1 for unlimited)
      --platform string                Set platform if server is multi-platform capable
      --privileged                     Give extended privileges to this container
  -p, --publish list                   Publish a container's port(s) to the host
  -P, --publish-all                    Publish all exposed ports to random ports
      --pull string                    Pull image before running ("always"|"missing"|"never") (default "missing")
      --read-only                      Mount the container's root filesystem as read only
      --restart string                 Restart policy to apply when a container exits (default "no")
      --rm                             Automatically remove the container when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the process (default true)
      --stop-signal string             Signal to stop a container (default "SIGTERM")
      --stop-timeout int               Timeout (in seconds) to stop a container
      --storage-opt list               Storage driver options for the container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the container
      --volumes-from list              Mount volumes from the specified container(s)
  -w, --workdir string                 Working directory inside the container
```

