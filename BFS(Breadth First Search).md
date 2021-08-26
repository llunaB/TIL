# BFS(Breadth First Search)

## 그래프를 탐색하는 방법

- 깊이 우선 탐색
- 너비 우선 탐색



## 너비우선탐색

탐색 시작점의 인접 정점을 차례로 방문 후, 방문했던 정점을 시작점으로 다시 인접한 정점을 차례로 방문



## 풀이코드

![image-20210825152650333](BFS(Breadth First Search).assets/image-20210825152650333.png)

```python
import sys
sys.stdin = open("input.txt")

# V => 노드
# E => 엣지, 간선

V, E = map(int, input().split())
graph_list = list(map(int, input().split()))
print(graph_list)

# 인접행렬
graph = [[0 for _ in range(V+1)] for _ in range(V+1)] # 1과 인덱스를 통일
visited = [0 for _ in range(V+1)] # 한 번 방문한 곳은 다시 방문하지 않기 위해

for i in range(E): # 8개의 쌍을 돈다
    # 홀짝 분리
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1 # 무향그래프이므로 대칭 구조를 만듦

def bfs(v):
    queue = [v] # 1번 넣은 상태로 시작

    while len(queue): # 큐가 빌때까지 계속해서 작업한다
        v = queue.pop(0) # 맨 앞의 데이터를 뽑아 v 에 덮어씌운다 (위의 v와는 별개)
        if not visited[v]:    # 방문하지 않았다면
            visited[v] = 1
            print('{}번을 방문했습니다. {}'.format(v, visited))

            for w in range(1, V+1): # V 번째 노드까지 돌리면서 연결된 노드 찾음
                if graph[v][w] == 1 and visited[w] == 0: # v 행의 w 열이 1이면
                    queue.append(w)


bfs(1) # 1번 노드부터 시작
```

```python
# 주석제거

import sys
sys.stdin = open("input.txt")

V, E = map(int, input().split())
graph_list = list(map(int, input().split()))

graph = [[0 for _ in range(V+1)] for _ in range(V+1)] 
visited = [0 for _ in range(V+1)]

for i in range(E):
    start = graph_list[i*2]
    end = graph_list[i*2+1]

    graph[start][end] = 1
    graph[end][start] = 1 

def bfs(v):
    queue = [v]
    while len(queue): 
        v = queue.pop(0) 
        if not visited[v]:   
            visited[v] = 1
            print('{}번을 방문했습니다. {}'.format(v, visited))

            for w in range(1, V+1): 
                if graph[v][w] == 1 and visited[w] == 0: 
                    queue.append(w)


bfs(1)
```



![image-20210825133545589](/Users/euijinpang/TIL/BFS(Breadth First Search).assets/image-20210825133545589.png)

- 큐(Queue) 를 사용

![image-20210825105003991](/Users/euijinpang/TIL/BFS(Breadth First Search).assets/image-20210825105003991.png)

```python
# visited 배열 초기화
# Q 생성
# 시작점 enqueue

...
```

- 중복체크 방지 (한 노드가 스택에 2번 들어가는 것을 방지) (위 그림에서 B와 C가 연결)
  - DFS, BFS 모두 중복이 없어야 한다!!

![image-20210825112954705](/Users/euijinpang/TIL/BFS(Breadth First Search).assets/image-20210825112954705.png)



## 응용 - 미로

- 1칸으로 갈 수 있는 거리, 2칸으로 갈 수 있는 거리.. 몇 번 만에 갈 수 있습니까?
  - 도착할 때 까지의 거리 - BFS
  - 경로체크 - DFS

![image-20210825133658928](/Users/euijinpang/TIL/BFS(Breadth First Search).assets/image-20210825133658928.png)



## 연습문제3 풀이코드2(참고)

```python
'''
참조


7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(s, V):
    q = []              # 큐 생성
    visited= [0]*(V+1)  # visited 생성
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 시작점 visited 표시

    while q:            # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)     # 디큐(꺼내서)해서 t에 저장
        print(t)        # t에 대한 처리
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0: # t에 인접이고 미방문인 모든 i에 대해
                q.append(i)                        # enqueue(i)
                visited[i] = visited[t] + 1        # i visited로 표시

V, E = map(int, input().split())
edge = list(map(int, input().split()))


adj = [[0]*(V+1) for _ in range(V+1)]   # 인접행렬

for i in range(E):
    n1, n2 = edge[2*i], edge[2 *i +1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1     # 방향이 없는 그래프
    
bfs(1, V)
```

