# Branch

### git에서 특정 브랜치 clone하기

git을 사용하다 브랜치 전체를 clone하지 않고 특정 브랜치 하나만 clone하는 것이 가능하다. 특히 브랜치가 많은 경우 이 방법을 사용할 수 있다.

```
git clone -b {branch_name} --single-branch {저장소 URL}
ex) git clone -b euijin.bang https://lab.ssafy.com/06/seoul03/algorithm.git
```

