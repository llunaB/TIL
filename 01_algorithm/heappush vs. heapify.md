![img](https://blog.kakaocdn.net/dn/cLRnfg/btrjD2msBO7/mg8PwciyxfsH54RVhYvxCK/img.png)

문제를 풀다가 궁금증이 생겼다.

같은 배열을 heapq 모듈을 사용하여 heap 자료구조를 만드는데 heappush 방식과 heapify 방식의 결과가 다르다.



## 힙(heap)이란?

**힙은 "부모 노드가 자식보다 작거나 같은 값을 갖는 이진 트리" 이다.**

**힙은 "0부터 요소를 셀 때, 모든 k에 대해 a[k] <= a[2\*k+1]와 a[k] <= a[2\*k+2]가 유지되는 배열"이다.**



## heapq 힙 큐 알고리즘

힙 큐 모듈은 우선순위 큐 알고리즘이라고도 하는 힙큐 알고리즘의 구현을 제공한다.

모든 k에 대해 heap[k] <= heap[2*k+1]과 heap[k] <= heap[2*k+2] 인 배열을 사용한다.

요소는 0부터 세며, 힙의 가장 작은 요소는 루트 heap[0] 이다.



## 힙 만드는 법 1. [ ] 초기화된 리스트 사용

> **heapq.heappush(heap, item)**
> 힙 불변성을 유지하면서, item 값을 heap으로 푸시합니다.

```python
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
# is the index of a leaf with a possibly out-of-order value.  Restore the
# heap invariant.
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```

##  

## 힙 만드는 법 2. heapify() 함수로 값이 들어있는 리스트를 힙으로 변환

> **heapq.heapify(x)**
> 리스트 x를 선형 시간으로 제자리에서 힙으로 변환합니다.

```python
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    # Transform bottom-up.  The largest index there's any point to looking at
    # is the largest with a child index in-range, so must have 2*i + 1 < n,
    # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
    # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
    # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
    for i in reversed(range(n//2)):
        _siftup(x, i)
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```



## 그래서, 왜 다르냐면

```python
import heapq

nums = [5, 4, 3, 2, 1]
heap = []

for num in nums:
    heapq.heappush(heap, num)

print(heap)  # [1, 2, 4, 5, 3]


nums = [5, 4, 3, 2, 1]
heapq.heapify(nums)

print(nums)  # [1, 2, 3, 5, 4]
```

heappush 는 빈 배열에 하나씩 값을 추가하면서 위치를 바꾼다.

새로운 값은 배열의 가장 마지막 인덱스로 들어가고 startpos는 루트노드이다.



heapify는 기존 배열에서 가장 작은 값을 찾아 부모와 교환하면서 위치를 바꾸는데

두 함수를 실행하면 알고리즘 구조상 다른 결과가 나온다.



그래도 가장 작은 수는 인덱스 0 이기 때문에 pop[0]을 하면 최소값이 나오며 이는 공통이다.

따라서 문제를 풀때 큰 에로사항은 없을 것 같다.

그러나 heapify의 시간복잡도가 더 낮다고 한다. (아직 계산은 해보지 않았다.)



> 결국 두 함수 모두 heap을 만드는 것은 동일하나 heapify의 시간복잡도가 낮기 때문에
> 리스트를 바로 heap으로 바꿀 땐 heapify를 사용하는것이 좋다.



![img](https://blog.kakaocdn.net/dn/xl3sS/btrjD1Vngr2/WnaoaXKhjxYLEI6k1QXkL0/img.jpg)



## 힙의 시간복잡도 O(nlogn)

![img](https://blog.kakaocdn.net/dn/beiIhe/btrjLyi9SJ6/5W9I5kK8H35QoKHdH1TsZK/img.png)

## 힙의 사용처 : 스케줄러와 디스크 정렬

![img](https://blog.kakaocdn.net/dn/lLC16/btrjJzC8GDN/24RV1QkbYzT4H3HsyC6gdk/img.png)





파이썬 공식문서 참조[
heapq — 힙 큐 알고리즘 — Python 3.10.0 문서heapq — 힙 큐 알고리즘 소스 코드: Lib/heapq.py 이 모듈은 우선순위 큐 알고리즘이라고도 하는 힙(heap) 큐 알고리즘의 구현을 제공합니다. 힙은 모든 부모 노드가 자식보다 작거나 같은 값을 갖는docs.python.org](https://docs.python.org/ko/3/library/heapq.html)