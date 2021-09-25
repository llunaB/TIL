# TREE

## 이진 트리(Binary Tree)

모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리

노드가 자식 노드를 최대 2개까지만 가질 수 있는 트리

- 레벨 i 에서의 노드의 최대 개수 : 2 ** i
- 높이가 h인 이진 트리
  - 노드의 최소 개수 : (h + 1)개
  - 노드의 최대 개수 : (2**(h+1) - 1)개



## 이진트리의 종류

1. 포화 이진 트리
   - 최대의 노드개수를 가진 이진트리
2. 완전 이진 트리
   - 포화이진트리의 노드번호 1번부터 n 번까지 빈 자리가 없는 이진 트리
3. 편향 이진 트리
   - 높이 h에 대해 최소개수의 노드를 한쪽 방향으로만 가진 이진트리



## 완전 이진 트리

높이가 h이고 노드 수가 n개일 때, Full 이진트리의 노드번호 1번부터 n번까지 빈 자리가 없는 이진 트리

- 인덱스 * 2 = 왼쪽
- 인덱스 * 2 + 1 = 오른쪽
- 인덱스 / 2 = 부모노드

#### 모든 부모 찾기

- 1 이상일때까지 2로 계속 나누기



## 순회(Traversal)

트리의 각 노드를 중복되지 않게 전부 방문(Visit)하는 것

1. 전위순회

   - 루트 - 왼쪽 서브트리 - 오른쪽 서브트리

   - ```python
     def preorder_traverse(T):
       if T:
         visit(T)
         preorder_traverse(T.left)
         preorder_traverse(T.right)
     ```

   - ![image-20210923094803355](/Users/euijinpang/Desktop/TREE.assets/image-20210923094803355.png)

2. 중위순회

   - 왼쪽 서브트리 - 루트 -  오른쪽 서브트리

   - ```python
     def inorder_traverse(T):
       if T:
         inorder_tranverse(T.left)
         visit(T)
         inorder_traverse(T.right)
     ```

   - ![image-20210923094945417](/Users/euijinpang/Desktop/TREE.assets/image-20210923094945417.png)

3. 후위순회

   - 오른쪽 서브트리 - 왼쪽 서브트리 - 루트

   - ```python
     def postorder_traverse(T):
       if T:
         postorder_traverse(T.left)
         postorder_traverse(T.right)
         visit(T)
     ```

   - ![image-20210923095221459](/Users/euijinpang/Desktop/TREE.assets/image-20210923095221459.png)



## 포화/완전 이진트리 표현 - 배열

이진트리에 각 노드번호를 부여

루트번호를 1로 하여 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2n 부터 2**(n+1)-1 까지 번호를 차례로 부여

노드 번호를 리스트의 인덱스로 사용

![image-20210923100429860](/Users/euijinpang/Desktop/TREE.assets/image-20210923100429860.png)

### 노드 번호의 성질 (정점 번호 = 배열의 인덱스)

- 노드 번호가 i 인 노드의 부모번호 : `i//2`
- 노드 번호가 i 인 노드의 왼쪽 자식 노드 번호 : `2*i`
- 노드 번호가 i 인 노드의 오른쪽 자식 노드 번호 : `2*i +1`

![image-20210923151246276](/Users/euijinpang/Desktop/TREE.assets/image-20210923151246276.png)

```python
def f(T):
	if 	T < 마지막 정점 번호:
  	visit(T)
    f(T * 2) # 왼쪽 자식노드의 (정점번호)인덱스
    f(T * 2 + 1) # 오른쪽 자식노드의 (정점번호)인덱스
```

```python
6
1 2 1 3 2 4 3 5 3 6
V = 정점수
V-1 개의 간선에 대한 정보

def pre_order(n):
  if n: # 유효한 정점이면
    pinrt(n)
    pre_order(left[n]) # n의 왼쪽 자식으로 이동
    pre_order(right[n])  # n의 오른쪽 자식으로 이동
    
V = int(input())
edge = list(map(int, input().split()))
E = V - 1 # V개의 정점이 있는 트리의 간선 수

left = [0] * (V+1) # 부모를 인덱스로 자식번호 저장
right = [0] * (V+1) 

for i in range(E):
  p, c = edge[i*2], edge[i*2+1]
  if left[p] == 0: # p의 왼쪽자식이 없으면 왼쪽 자식으로 저장
    left[p]= c	 	
  else:						 
    right[p]= c # p의 왼쪽자식이 있으면 오른쪽 자식으로 저장

```



## Binary Search Tree 이진 탐색 트리 (재귀x, 반복문으로 구현가능)

- 모든 원소는 서로 다른 유일키를 가진다
- key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 중위 순회하면 오름차순으로 정렬된다.

![image-20210923101524884](/Users/euijinpang/Desktop/TREE.assets/image-20210923101524884.png)

![image-20210923101657809](/Users/euijinpang/Desktop/TREE.assets/image-20210923101657809.png)

![image-20210923160933633](/Users/euijinpang/Desktop/TREE.assets/image-20210923160933633.png)

![image-20210923101735702](/Users/euijinpang/Desktop/TREE.assets/image-20210923101735702.png)

![image-20210923101752563](/Users/euijinpang/Desktop/TREE.assets/image-20210923101752563.png)

## 문제1

- B조 : start에 N 을 넣으면 자식을 하나하나 찾아서 연결하는 구조
- C조 : 전위순회 - 왼쪽 자식 넣을 리스트, 오른쪽 자식 넣을 리스트 (베이직)

## 문제2. 이진탐색

- D조 : 1, 2, 4 순서로 진행

## 문제3. 이진힙

- E조 : heappush 구현

## 문제4. 노드의합

- 