# 문제별
## 추석 트래픽
https://programmers.co.kr/learn/courses/30/lessons/17676  

1초 : 4.001~5.000 - 끝나는 시간이 5초라면 1초가 아닌 0.999초를 빼야 시작하는 시간이 나옴.  

해당 구간에 아직 끝나지 않은 요청+앞으로 1초동안 (ex: 5초부터 5.999초동안) 시작하는 요청의 수를 더하면 됨.  

## 셔틀버스  
https://programmers.co.kr/learn/courses/30/lessons/17678  

통근 셔틀을 타고 갈 수 있는 가장 늦은 시간.  

줄을 서는 시간은 둘중 하나.  
맨 마지막으로 셔틀을 타는 사람보다 1분 일찍옴.  
맨 마지막의 셔틀에 자리가 남는 경우에는 셔틀이 도착하는 시간.  

## 길 찾기 게임  
https://programmers.co.kr/learn/courses/30/lessons/42892  

크게 2가지 단계로 구분.  
1. 노드의 좌표를 바탕으로 바이너리 트리를 생성  
2. 바이너리 트리순회  

단계별로 내가 사용한 방법은 다음과 같다.  
1. 좌표를 바탕으로 바이너리 트리를 생성하는 방법.  
    a.첫번째 방법.  
    [inorder와 level이렇게 2가지로 정렬을 하고 트리를 생성한다.](https://www.geeksforgeeks.org/construct-tree-inorder-level-order-traversals-set-2/)      
    inorder로 정렬할때는 노드의 x좌표를 기준으로 오름차순으로 정렬하면 된다.  

    b.두번째 방법  
    문제의 조건에 '같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.'라고 되어 있다.  
    즉 레벨로 정렬하면 바이너리 트리에 숫자를 넣은 순서가 나온다.  
    바이너리 트리를 생성할때 숫자를 넣은 순서를 다르게하면 생성되는 트리의 모양이 달라진다.  
    먼저 넣은 숫자가 높은 레벨을 차지하기 때문이다.  
    레벨로 정렬할 때는 y값의 내림차순으로 정렬하면 된다.  
    정렬한 순서대로 넣으면 바이너리 트리를 생성할 수 있다.  
    
2. 바이너리 트리순회  
pre order와 post order로 순회한다.  
모르면 검색ㄱㄱ.  

## 선입 선출 스케줄링
https://programmers.co.kr/learn/courses/30/lessons/12920  

각 코어의 완료시간을 고려하지 않고 완료되면 바로 남은 작업을 시작하는 문제이다.  

Parametric Search로 작성하면 효율성도 통과가 가능하다.  
그리고 루프문에 유의해서 작성해야 효율성도 전부 통과가 된다.  

밑에 python 소스는 우선순위큐(heap)으로 어떻게든 비벼볼려고 하다가 나왔는데  
효율성은 하나도 통과가 안되지만 파라메트릭 코드가 정확한지 보는데 유용하게 썼습니다.  
```py
import heapq
def solution1(n, cores):
    h=[(0,core) for core in range(len(cores))]# (작업완료시간, 코어숫자)
    heapq.heapify(h)

    while True:#작업끝 -> 바로 작업 수행 : 코드가 짧아진 이유.
        donetime,donecore=h[0]
        if n==1:
            return donecore+1
        heapq.heapreplace(h,(donetime+cores[donecore],donecore))#작업완료시간과 코어순서로 정렬됨.
        n-=1
```

## 입양 시각 구하기(2)
```sql
-- mysql
SELECT h.theHour
     , COUNT(DATETIME) AS numberOfItems
    FROM (
        SELECT 0 AS theHour
        UNION ALL SELECT 1
        UNION ALL SELECT 2
        UNION ALL SELECT 3
        UNION ALL SELECT 4
        UNION ALL SELECT 5
        UNION ALL SELECT 6
        UNION ALL SELECT 7
        UNION ALL SELECT 8
        UNION ALL SELECT 9
        UNION ALL SELECT 10
        UNION ALL SELECT 11
        UNION ALL SELECT 12
        UNION ALL SELECT 13
        UNION ALL SELECT 14
        UNION ALL SELECT 15
        UNION ALL SELECT 16
        UNION ALL SELECT 17
        UNION ALL SELECT 18
        UNION ALL SELECT 19
        UNION ALL SELECT 20
        UNION ALL SELECT 21
        UNION ALL SELECT 22
        UNION ALL SELECT 23
    ) AS h
    LEFT OUTER JOIN ANIMAL_OUTS 
        ON hour(ANIMAL_OUTS.DATETIME) = h.theHour
GROUP BY h.theHour
```
시간대별로 집계를 하는 문제. 0시부터 23시까지 해당 시간대에 입양된 동물의 수를 출력. 단 동물의 수가 0인 시간도 출력을 해주어야 함.  
`LEFT OUTER JOIN ANIMAL_OUTS ON hour(ANIMAL_OUTS.DATETIME) = h.theHour`: join수행시 좌측에 있는 `h`테이블을 전부 나열. 그 옆에 주어진 규칙대로 테이블을 join한다. 이때 `OUTER JOIN`임으로 규칙에 해당하는 우측 테이블의 열이 없는 경우에는 null 값이 된다.  
즉 0에서 23시까지 나열된 h테이블에  
|theHour|
|-|
|0|
|1|
|2|
|3|
|4|
|5|
|6|
|7|
|8|
|9|
|10|
|11|
|12|
|13|
|14|
|15|
|16|
|17|
|18|
|19|
|20|
|21|
|22|
|23|

`ON` 뒤에 지정된 규칙대로 테이블을 join 한다.  
`GROUP BY`를 했기 때문에 animal_outs에서 `hour(ANIMAL_OUTS.DATETIME) = theHour`에 해당하는 여러 row가 하나의 그룹을 이루고 있게 된다. select명령으로 조회하면 한 그룹당 하나의 row를 보여준다. 물론 빈 그룹이면 빈 row가 join되어 있을 것이다. (시퀄라이즈에서 include하면 하위 키 안에 배열에 있겠지.) 그 여러 row의 값을 세는 명령이 바로 count(datetime)이다.  
근데 나같으면 저렇게 길기만한 쿼리를 시퀄라이즈로 짜기보다는 그냥 받아서 적절히 가공하겠다.  

- 참고1: `UNION ALL`은 (컬림이 같은) 두 테이블을 이어붙인다.  
- 참고2: mysql에서는 `connect by`가 없다고 한다. 오라클에 있다는데 뭔지는 모름. `UNION `혹은 `UNION DISTINCT`은 중복을 제거함. 당연히 중복을 제거하느라 추가적인 연산을함.  
- 참고3: 다른 코드를 보면 변수를 선언해서 하는 방법도 있다. `ANIMAL_OUTS`에 있는 동물의 순번으로 넘버링 하는 방식이다. 그런데 예를 들어 동물의 숫자가 3마리라면 0,1,2까지만 넘버링되어서 0시 1시 2시만 카운트 하기떄문에 제대로 답이 안나옴. 확인하는 방법은 해당코드에서 `FROM ANIMAL_OUTS`대신 `FROM (SELECT * FROM ANIMAL_OUTS LIMIT 3) AS e`등으로 바꾸어 보연 답이 안나온다.  
