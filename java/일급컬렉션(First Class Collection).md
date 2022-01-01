# 일급 컬렉션(First Class Collection)

# 정의

**퍼스트 클래스 컬렉션**
이 규칙의 적용은 간단합니다. 컬렉션을 포함하는 클래스는 다른 멤버 변수를 포함하지 않아야 합니다. 각 컬렉션은 자체 클래스로 래핑되므로 이제 컬렉션과 관련된 동작에 홈이 있습니다. 필터가 이 새로운 클래스의 일부가 됨을 알 수 있습니다. 또한 새 클래스는 두 그룹을 함께 결합하거나 그룹의 각 요소에 규칙을 적용하는 것과 같은 활동을 처리할 수 있습니다.

**Rule 4: First class collections**

Application of this rule is simple: any class that contains a collection should contain no other member variables. Each collection gets wrapped in its own class, so now behaviors related to the collection have a home. You may find that filters become a part of this new class. Also, your new class can handle activities like joining two groups together or applying a rule to each element of the group.



# 예시

아래의 코드를

```java
Map<String, String> map = new HashMap<>();
map.put("1", "A");
map.put("2", "B");
map.put("3", "C");
```

아래와 같이 **Wrapping** 하는 것을 얘기합니다.

```java
public class GameRanking {

    private Map<String, String> ranks;

    public GameRanking(Map<String, String> ranks) {
        this.ranks = ranks;
    }
}
```