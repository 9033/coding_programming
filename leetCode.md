# 문제별
내가 풀이한 방법에 대한 설명  
LeetCode 문제 목록 링크: [Problems](https://leetcode.com/problemset/)  
## 14. Longest Common Prefix
+ trie사용해봄
  + 첫번째 str로 trie를 생성
  + 2번째 str부터는 trie를 탐색
  + end로 마킹한 부분까지 출력
## 18. 4Sum
+ `15. 3sum`에서 루프문 하나를 더 추가.
  + 이중 루프로 모든 경우의 수를 처리해야함.
## 35. Search Insert Position
+ binary search
## 61. Rotate List
+ 가능한 추가적인 메모리를 안쓰는 방법을 사용.
+ 단 방향으로 된 연결 리스트 이기 때문에 rotate하는 방향을 반대로 함.
  + 리스트의 전체 길이를 구하기 위해 탐색.
  + rotate하는 방향이 반대일때 탐색을 해야할 횟수를 구함.
  + tail의 next를 head로 설정 후에 탐색
  + 새 tail의 next를 null로 하고 리턴
## 63. Unique Paths II
+ 시작 지점에도 장애물이 있을 수 있다.
## 139. Word Break
+ wordDict에 있는 단어가 여러번 쓰일 수 있다. -&gt; s의 길이까지 문자열을 조합하는 도중에 현재 길이의 문자열을 생성한 적이 있으면 skip
## 180. Consecutive Numbers
+ lag함수를 이용해서 위 row와 위위 row의 num값을 구해서 연속인지 판단함.
## 181. Employees Earning More Than Their Managers
+ from 에 한 테이블을 여러번 집어넣고 where로 join해서 테이블을 생성 한 후에 조건에 해당하는 row출력
## 182. Duplicate Emails
+ count() 활용함
## 183. Customers Who Never Order
+ 서브쿼리보다 left join이 속도가 빠르다.
## 262. Trips and Users
1. trips에서 banned된 user랑 날짜로 필터링
2. 각 날짜 별로 전체랑 완료 안된 경우를 카운트
3. 날짜 별로 rate를 계산해서 출력
## 368. Largest Divisible Subset
+ DP, 그런데 다시 배열을 구성하는 방법이 햇갈렸다.
+ 오름차순으로 정렬 후 현재 위치에서 최대의 배열의 길이를 구한다.
+ 가장 긴 숫자를 선택. 답으로 출력할 배열에 넣음.
  + 가능한 경우의 수 중에서 하나만 출력하면 되니까 같은 길이의 숫자중에 하나만 선택해서 출력하면됨.
+ 그리고 다음 번 숫자를 선택할때 배열에 넣은 숫자와 나머지 연산을 해서 확인한 후 넣는다.
## 498. Diagonal Traverse
+ 3x3 인경우
  + 시작지점 (0,0), (1,0), (2,0), (2,1), (2,2)
  + 오른쪽 상단 방향으로 임시 배열에 넣음
  + 필요하면 리턴 배열에 임시 배열을 넣을때 reverse를 함
+ 직사각형 배열도 처리해야한다
  + ~~시간이 많이 걸리면 실제로 개발할때도 시간이 많이 걸릴것 같다.~~
## 515. Find Largest Value in Each Tree Row
+ binary tree가 나오는 이전 문제(2471, 2415등)에서 사용한 BFS 코드를 재활용. 마찬가지로 다음 레벨을 탐색하기 직전에는 큐에 다음 레벨의 노드만 들어가 있다는 점을 활용함.
+ 트리가 빈 경우를 채크하는 부분 추가.
## 570. Managers with at Least 5 Direct Reports
+ inner join 할때 조건문에 5인 이상인 것도 추가함
## 577. Employee Bonus
+ 보너스가 없는 경우 null로 출력하는것이 포인트
## 602. Friend Requests II: Who Has the Most Friends
+ `UNION` 으로 전체 id의 목록을 만들고 각 id의 수를 `LEFT JOIN`함
+ `UNION`이 중복을 없에서 left join을 사용.
+ 알고보니 `UNION ALL`을 사용해보는 문제
## 684. Redundant Connection
+ edge와 node의 수가 같으면 원형으로 연결된 곳이 한군데만 발생
+ 위상 정렬 - 간선이 1인 노드만 지움 -&gt; cycle을 이루는 노드만 남음
## 763. Partition Labels
+ 처음에 b인 경우 처음 b와 마지막 b 의 위치를 기억
+ 그 다음 문자를 처리, 처음 구간은 편의상 b-part, 그 다음 문자는 c라고 가정
  + c의 시작이 b-part사이이며 c의 마지막 위치가 b-part에서 오른쪽 밖이면 b-part를 확장
  + c의 처음과 마지막이 b-part사이에 포함되면 넘어감
  + c의 시작과 끝이 구간 밖이면 새 part를 생성
## 769. Max Chunks To Make Sorted
+ 배열을 그냥 정렬할때와 chunk로 나누어서 각각 정렬 후에 합친 결과가 같다 -&gt; 앞에 있는 chunk의 최대 숫자 &lt; 뒤에 있는 chunk의 최소 숫자
+ 정렬은 오름차순으로 하면 된다.
## 781. Rabbits in Forest
+ `[0]`이면 같은 색이 자기 자신만 있어서 1명
+ `[1]`이면 간은 색이 자기 자신과 또 다른 한명까지 2명, 그 중에서 응답을 한 사람은 한명.
+ `[1,1]`이면 간은 색이 자기 자신과 또 다른 한명까지 2명, 그리고 응답을 한 사람은 두명.
## 802. Find Eventual Safe States
+ 모든 경로가 terminal node에 도달한다는 것을 계산하려고 보니 왠지 복잡하다
+ terminal node로 가지 않는 경로가 하나라도 있는 경우는 cycle이 되는경로로 하나라도 향하는 경로가 있는 경우다
+ DFS로 탐색하면서 terminal node와 cycle로 가는 경로가 있는 노드 이렇게 두가지를 채크 하면서 탐색해야 함.
  + terminal node거나 terminal node로만 가는 경로만 있는 노드를 채크해서 탐색하는 가지수를 줄인다.
  + cycle로 가는 경로가 하나라도 있는 경우도 채크해서 탐색하는 가지수를 줄이고 답을 출력하면 된다.
## 827. Making A Large Island
+ 각 섬의 넓이를 구함
+ 타일 1개를 매꿀 경우 이어지는 넓이의 최대값 (최대 4개의 섬의 넓이 + 매꾸는 넓이(1))
## 838. Push Dominoes
+ 힘이 가해지는 부분과 전달 받는 부분을 따로 조건문으로 처리
+ 전달 받는 부분을 처리하는 기준은 힘이 가해지는 부분에서 거리를 비교 - 여기서 전달 받는 부분에서 힘이 가해지는 부분에서 L과 R의 거리가 같으면 '.'으로 처리
## 904. Fruit Into Baskets
+ sliding window
  + 바구니의 크기가 제한이 없다
  + 처음 과일을 줏기 시작한 나무 부터 오른쪽으로 이동. 이동하면서 계속 줏어야 한다.
+ 1695. Maximum Erasure Value 와 유사
## 983. Minimum Cost For Tickets
+ 1D DP 이며 2466과 거의 유사
+ 여행을 가지 않는 날인 경우 cost를 이전 날의 cost와 같게 한다.
## 1007. Minimum Domino Rotations For Equal Row
+ 4가지 경우를 고려
  + `tops[0]`과 같은 값을 tops로 옮김, `tops[0]`과 같은 값을 bottoms로 옮김, `bottoms[0]`과 같은 값을 tops로 옮김, `bottoms[0]`과 같은 값을 bottoms로 옮김
  + 가능한지 불가능한지, 교환 횟수는 얼마인지
  + 가능한 경우중에서 최소의 교환 횟수를 출력
## 1028. Recover a Tree From Preorder Traversal
+ traversal에 입력되는 탐색 순서가 DFS로 되어 있다. 그래서 stack을 사용했다.
  + 트리에 입력할 노드가 depth가 같거나 더 앝은 노드면 스택에서 parent노드가 top에 있을 때 까지 pop을 연속으로 한다.
+ TreeNode 기본값, left와 right가 null이여야 함.
  ```js
  {
    left: null,
    right: null,
  }
  ```
## 1079. Letter Tile Possibilities
+ DFS를 사용하면서 Set 등으로 중복을 채크하지 않아도 되는 방법이 있다.
## 1123. Lowest Common Ancestor of Deepest Leaves
+ 문제를 한번 읽어서는 뭘 해야 하는지 머리속에 안들어온다
## 1128. Number of Equivalent Domino Pairs
+ 각 domino가 등장한 수를 계산해서 저장
+ 등장한 domino를 pair로 만드는 수를 계산
  + 같은 domino n개에서 2개를 pair로 만들때 중복없고 순서를 고려하지 않는 조합의 공식을 사용함
## 1217. Minimum Cost to Move Chips to The Same Position
+ DP: O(n^2) (position * position)
  + 위치의 범위는 넓지만 칩의 위치의 경우의 수가 1000개 때문에 가능
+ O(n)이 존재한다
## 1261. Find Elements in a Contaminated Binary Tree
+ 실제로는 root에 배열이 아닌 트리 구조로 입력 값이 들어온다.
  + 트리 문제를 오랫만에 봐서 감을 잃었다. 배열을 트리로 변환하느라 시간을 보냈다.
    ```js
    const makeTree = (arr) => {
      _tree={
        val: 0,
      }
      const q=[_tree]
      for(let i=1;i<arr.length;i+=2){
        const node=q.shift()
        // console.log('node', node)
        const x=node.val
        // node.val = 2*x+c
        if(typeof arr[i] === 'number'){
          node.left = {
            val: arr[i], // 2*x+1
          }
          q.push(node.left)
        }
        if(typeof arr[i+1] === 'number'){
          node.right = {
            val: arr[i+1], // 2*x+2
          }
          q.push(node.right)
        }
      }
      // console.log('tree', _tree)
      return _tree
    }
    ```
## 1267. Count Servers that Communicate
+ N-queen하고 비슷해 보임, 그리고 2661하고도 비슷해 보임
+ 행에 대해서 2개 이상인지 확인, 2개 이상이면 전부 카운트
+ 열에 대해서 2개 이상인지 확인, 2개 이상이면 전부 카운트
+ 그리고 중복해서 카운트 하는 경우를 방지함
## 1352. Product of the Last K Numbers
+ 곱셈도 prefix sum이 적용 된다고 함
  + 인덱스 기준으로 -i * -j === -i / (-j-1)
  + 0이 포함되는 경우 0으로 출력하게 처리
## 1368. Minimum Cost to Make at Least One Valid Path in a Grid
+ bfs에서 queue를 priority queue 로 변경함. 최소 cost부터 우선 탐색. 목적지에 도달하는 경우 종료.
+ dfs, bfs모두 타임 아웃나옴
+ cell에 갔을때 이전에 방문했을떄 cost보다 같거나 많으면 해당 경로는 종료. 그렇지 않으면 현재 cost를 저장
+ 화살표는 한번반 변경 가능. 그런데 여러번 바꾸는 경우는 cost가 올라가기 떄문에 코드상에서는 따로 고려 안함.
## 1400. Construct K Palindrome Strings
+ prefix sum을 이용하여 풀이, O(n)
+ 문자열의 길이가 k보다 작으면 false
+ 문자열에서 홀수개의 문자가 k보다 많으면 false
  + 홀수개의 문자의 수보다 더 적게 Palindrome String을 만들 수 없음
+ 나머지 경우는 true
## 1422. Maximum Score After Splitting a String
+ `l[i]`는 0\~i까지 0의 개수 를 구한다. `r[i]`는 i\~n-1까지 1의 개수 를 구한다.
+ 그리고 `l[i]+r[i+1] (0<=i<n-1)`의 최대값을 구하면 된다
+ boundary test cases
  ```
  Input: s = "00"
  Output: 1

  Input: s = "01"
  Output: 2

  Input: s = "10"
  Output: 0
  ```
## 1462. Course Schedule IV
+ cycle이 없는 경우가 주어지니까 편안하게 위상 정렬로 구현
+ 위상정렬을 통해서 특정 course를 수강하기 전에 먼저 수강해야하는 course를 구한다.
  + 스택으로 탐색하며 스택에는 수강이 가능한 course 를 넣으면 된다.
## 1475. Final Prices With a Special Discount in a Shop
+ 본문에 있는대로 코드를 짜면 된다. prices의 길이가 길지 않아서 O(n**2)로 통과된다.
## 1492. The kth Factor of n
+ factors의 배열을 생성하고 해당 값을 출력하게 함
## 1493. Longest Subarray of 1's After Deleting One Element
+ sliding window에서 0하나만 허용한다.
## 1639. Number of Ways to Form a Target String Given a Dictionary
vscode의 코파일럿(무료)가 알려주는데 cutting하는 조건을 처음에 다 알려주지 않는다.
그리고 제시한 코드가 왜 정답이 나오게 되는지 이해하는데 시간이 걸림.

+ 각 문자열에 대한 각 문자의 개수를 하나의 객체로 만든다.
  - 코파일럿의 코드는 이 방법이다. 나는 각 word별로 만들려고 생각함
+ memoization를 사용한다.
  - 시간 초과라고 나와서 추가함.
+ words의 남은 문자열이 target의 남은 문자열보다 작으면 0을 반환한다.
  - 시간 초과라고 나와서 추가함.
## 1695. Maximum Erasure Value
+ 오른쪽에 넣을 숫자랑 같은 숫자가 이미 sliding window에 있는 경우 -> 같은 숫자가 없을 때 까지 sliding window를 축소, 축소 할 때는 왼쪽에서 축소한다.
## 1717. Maximum Score From Removing Substrings
- greedy, stack
## 1718. Construct the Lexicographically Largest Valid Sequence
+ 큰 수 부터 채워 나가면 처음에 찾은 배열이 가장 사전순으로 큰 시퀀스.
## 1726. Tuple with Same Product
+ nums안에 숫자를 서로 곱한다. 곱한 결과의 빈도수를 계산. 이때 a와 b가 같은 경우를 제외한다.
  + 곱한 결과의 빈도수가 4개가 나온다면, 조건에 맞는 [a,b,c,d]로 8개이며 tuple를 만들 수 있다. 이떄 곱이 같은 pair가 2개가 있다고 본다. 
  + 곱한 결과의 빈도수가 6개가 나온다면, 곱이 같은 pair가 3개이며 24개의 tuple를 만들 수 있다. 
  + 곱한 결과의 빈도수가 8개가 나온다면, 곱이 같은 pair가 4개이며 48개의 tuple를 만들 수 있다. 
+ 두 수의 곱의 빈도수로 몇개의 tuple을 만들 수 있는지 계산해서 전부 더해서 출력
## 1765. Map of Highest Peak
+ editorial에서 water까지 최단거리를 구하는 방식으로 함
+ priority queue로 탐색을 해서 여러 지점 에서 출발해서 각 cell의 최단거리를 구하게 변경
+ cell에서 가장 가까운 water까지 거리를 구하는 셈
## 1769. Minimum Number of Operations to Move All Balls to Each Box
+ 공의 개수를 세고, 이동 횟수를 세는 방식으로 풀이 (prefix sum)
+ 양쪽 구간으로 나누어서 함
  + l[i]는 0\~i까지 1의 개수, r[i]는 i\~n-1까지 1의 개수
  + i까지 0\~i-1 공의 이동 횟수, i까지 i+1\~n-1 공의 이동 횟수
## 1790. Check if One String Swap Can Make Strings Equal
+ 글자 빈도수가 같고 2군데만 다른 문자열인 경우에 한번에 swap으로 같은 문자열이 될 수 있다.
+ 이미 같은 경우와 한번 swap으로 같아질 수 있는 경우에 true로 출력
## 1792. Maximum Average Pass Ratio
+ 각 class의 합격율(ratio)의 평균을 최대화
  - extra 한명이 추가될때 마다 추가된 class의 ratio 가 변한다
  - 1명의 extra가 들어갔을때 가장 ratio의 변화가 높은 class에 집어넣음
    - 위를 extraStudents번 반복한다, 최대 우선순위 큐를 활용
+ leetcode에 기본적으로 javascript에서 우선순위 큐 라이브러리를 사용할 수 있다.
  + https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages
## 1845. Seat Reservation Manager
+ 비어있는 자리를 우선순위 큐에 넣는 것이 간단하다.
## 1863. Sum of All Subset XOR Totals
+ nums의 수가 적어서 backtracking으로 모든 경우를 탐색
## 1922. Count Good Numbers
+ 각 자리 별로 경우의 수가 정해저 있다.
+ 연산에서 오차가 생겨서 BigInt (javascript)를 사용함
## 1930. Unique Length-3 Palindromic Subsequences
+ 양 옆의 구간의 개수를 보고 palindrome이 되는지 확인 (prefix sum, O(n))
  + 1\~s-1의 루프에서 같은 문자가 왼쪽에 하나라도 있고 오른쪽에 하나라도 있으면 palindrome이 됨
+ editorial는 양 끝을 잡고 중간에 문자의 수를 확인. 중복되는 문자는 한번만 센다
## 1976. Number of Ways to Arrive at Destination
+ floyd에서 loop를 돌릴때 mid -> src -> desc 로 돌려야함
+ 풀이방법을 보니 경로의 가중치 뿐만 아니라 가지수를 곱하거나 더하는 방법이 있어서 참고함
## 1980. Find Unique Binary String
+ 정렬을 하고나서 최대 n번 루프를 돌림
  + 답 중에서 가장 작은 수가 나오게됨
## 2033. Minimum Operations to Make a Uni-Value Grid
+ 처음에는 바이너리 서치를 생각함.
  + 정렬 후에 m,n을 grid에서 제일 작은수랑 제일 큰 수로 해서 mid=(m+n)/2 를 통해서 찾는것임.
  + 그런데 예재를 계산해보니 가운데 있는 숫자가 될 때 x가 최소화가됨.
+ grid에 있는 숫자중 하나를 고르는 것 까진 알겠는데 왜 정렬하고 가운데 있는 숫자를 고르면 되는지?
+ 짝수개라서 중앙값이 양옆으로 2개 나오는데 그 중에서 n/2, n/2+1중 하나만 고르면 되는것 까진 알겠음
## 2054. Two Best Non-Overlapping Events
+ DP로 푸는 경우: max(현재 이벤트 이전까지 1개만 선택하는 경우의 최대 value + 현재 이벤트의 value, 현재 이벤트의 끝나는 time까지 다른 이벤트를 2개 선택한 경우의 최대 value)
## 2115. Find All Possible Recipes from Given Supplies
+ dfs + memoization and mark visited
  + 그래프 탐색에 visited를 채크해서 풀리면 위상정렬로 될 수도?
## 2116. Check if a Parentheses String Can Be Valid
+ stack으로 뭔가 해보려다가 잘 안됨
+ 앞에서 뒤로, 뒤에서 앞으로 2-pass로 검증
+ hint 3가지를 참고함, 2-pass로 그중에 2가지를 검증
+ false되는 경우는 hint 1까지 포함해서 총 3가지.
+ locked일때 '(', ')'와 unlocked일때, 총 3가지의 개수로 판단
## 2131. Longest Palindrome by Concatenating Two Letter Words
+ 길이가 2인 word의 앞뒤가 같은 경우 가운데에 word가 오는게 가능
+ 앞뒤가 다른 word는 각각 양 옆에 배치 가능하고 하나만 있으면 배치 못함
## 2133. Check if Every Row and Column Contains All Numbers
+ lodash zip과 set을 이용함
## 2140. Solving Questions With Brainpower
+ O(n) 1D DP
  + 배열 에서 0인 인덱스 부터 계산하니 bottom-up DP인듯
## 2145. Count the Hidden Sequences
+ 원래 수열의 가장 큰 수와 가장 작은 수로 lower와 upper사이에 있는지 판단한다.
## 2161. Partition Array According to Given Pivot
+ 배열로 각각 pivot보다 작은수, 같은수, 큰수를 담고 나서 합쳐서 리턴해서 순서를 유지.
## 2182. Construct String With Repeat Limit
+ 입력값의 순서와 출력값의 순서가 관련이 없어서 각 문자의 빈도수를 채크해서 처리함
## 2206. Divide Array Into Equal Pairs
+ 배열에 숫자가 짝수개 들어가 있는지 판별한다
+ editorial에 있는 방법만 4가지
  + 정렬 - 1가지
  + 빈도수 - 1가지
  + 빈도가 홀수 인지 짝수인지 2가지 상태로 판별 - 2가지
## 2270. Number of Ways to Split Array
+ 1422와 유사한 문제
+ 0\~i 와 i+1\~n-1의 두 구간의 합을 비교한다.
## 2300. Successful Pairs of Spells and Potions
+ potions 배열에 있는 각 potion에 spell을 곱하는 방법은 느리다, 대신 나누기를 사용함
## 2337. Move Pieces to Obtain a String
+ 이중 루프 대신 단일 루프를 사용. 안되는 경우를 거른다.
+ 예제 테스트 케이스에 없는 L과 R이 번갈아서 나오는 경우를 테스트 케이스로 생각하는 것도 시간이 걸림.
  ```
  Input: start = "___L____R____L", target = "__L______RL___"
  Output: true

  Input: start = "___L____L___R_", target = "__L______RL___"
  Output: false
  ```
## 2349. Design a Number Container System
+ Object를 2개 사용함. 숫자별로 가장 작은 index를 저장, 각 index에 있는 숫자를 저장
+ 테스트 하는 코드 (JS)
  ```js
  ;(()=>{
    let obj
    // const arr1=["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
    // const arr2=[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
    const arr1=["NumberContainers","change","find","change","find","find","find"]
    const arr2=[[],[1,10],[10],[1,20],[10],[20],[30]]
    const r=[]

    for(let i=0;i<arr1.length;i++){
      if(arr1[i]==='NumberContainers') {
        obj = new NumberContainers()
        r.push(null)
      } else if(arr1[i]==='find'){
        r.push(obj.find(arr2[i][0]))
      } else if(arr1[i]==='change'){
        obj.change(arr2[i][0],arr2[i][1])
        r.push(null)
      }
    }

    console.log(r);
  })();
  ```
## 2364. Count Number of Bad Pairs
+ 모든 pair중에서 good pair의 수를 뺀다.
## 2375. Construct Smallest Number From DI String
+ 편의상 왼쪽부터 채운다. 조건에 맞으면 계속 오른쪽 까지 채워 나간다.
  + 채울때 1부터 n+1 까지의 수 중에서 조건에 맞는지 확인한다.
## 2379. Minimum Recolors to Get K Consecutive Black Blocks
+ 길이가 k인 sliding window를 이용
## 2410. Maximum Matching of Players With Trainers
+ sort후 greedy
## 2415. Reverse Odd Levels of Binary Tree
+ Editorial을 참고해서 BFS 로 탐색을 함. 
+ 다음 level를 탐색하기 직전에는 큐에 같은 레벨의 노드만 있음. 짝수 레벨만 큐에 있을때 순서를 뒤집어서 값을 넣는다.
## 2425. Bitwise XOR of All Pairings
+ xor 연산의 법칙을 활용 O(n*m) -&gt; O(n+m) 으로 변경함
  + 교환법칙, 결합법칙등  
## 2466. Count Ways To Build Good Strings
+ 1D DP로 각 길이에 대한 경우의 수를 구한다.
  - 길이가 0인 경우의 수는 1가지.
+ 그리고 길이가 low부터 high까지인 문자열의 각 경우의 수를 더하면 된다.
## 2467. Most Profitable Path in a Tree
+ bob의 경로 alice경로 총 2번 탐색을 함
+ leaf노드인지 확인하는 부분을 습관대로 array로 하다가 timeout나옴, Set으로 바꿈.
## 2471. Minimum Number of Operations to Sort a Binary Tree by Level
+ 같은 레벨의 노드들을 찾는것은 2415. Reverse Odd Levels of Binary Tree에서 활용한 BFS를 가지고 옴. 큐에 같은 레벨의 노드가 있을때 swap 횟수를 구하고 해당 레벨을 채크해서 한 레벨에서 swap횟수를 중복으로 구하지 않게함.
+ SWAP횟수를 확인하는 알고리즘은 editorial를 참고. 여기서는 같은 값은 트리에서 한번만 나오기 떄문에 위치를 저장해서 활용함
## 2529. Maximum Count of Positive Integer and Negative Integer
+ 크기 순으로 정렬이 되어 있고 hint에 binary search라고 쓰여 있다. 그렇지만 O(n)으로 진행함.
## 2554. Maximum Number of Integers to Choose From a Range I
+ 여러 제약 조건을 고려하면 단일 루프로 가능하다. 조건에 맞는 다른 경우의 수를 볼 필요가 없기 때문
    + 조건: 최대 숫자인 경우만 출력, 숫자는 한번만 선택, maxSum 이하면 됨.
+ banned에 한 숫자가 2번 들어갈 수 있음
## 2558. Take Gifts From the Richest Pile
+ 가장 큰 수의 위치를 찾을때 단순히 `findLastIndex`로 찿아도 타임 아웃이 안난다. O(gifts.length * k)
## 2559. Count Vowel Strings in Ranges
+ 조건을 만족하는 단어는 1 아니면 0으로 본다.
+ words의 index를 기준으로 0\~0, 0\~1, 0\~2, 0\~i, ..., 0\~n-1까지 조건을 만족하는 단어의 숫자를 구한다.
+ 각 queries에 지정된 구간에서 조건을 만족하는 단어의 수를 출력한다. 예를 들면 1\~4 구간은 0\~4 에서 0\~0을 빼면 된다.
## 2570. Merge Two 2D Arrays by Summing Values
+ 두 배열이 정렬되어 있어서 merge sort를 응용
## 2593. Find Score of an Array After Marking All Elements
+ indexing 으로 가장 작은 수 (같으면 가장 작은 index) 를 찾는 것을 빠르게 함
## 2594. Minimum Time to Repair Cars
+ rank의 숫자가 낮은사람부터 수리할 차를 할당함
  + rank의 숫자가 낮은사람이 같은 시간에 더 많은 차를 수리 가능.
+ m분에 몇대의 차를 수리할 수 있는지 대입해 보는 관점으로 푼다.
## 2658. Maximum Number of Fish in a Grid
+ bfs
+ 이미 물고기를 전부 낚은 cell은 다시 가지 않음
+ land라서 물고기가 없는 cell은 이미 방문 한 것으로 가정
## 2685. Count the Number of Complete Components
+ 처음에는 3중 for문으로 floyd를 돌려서 거리가 2 이상인지 판별함.
+ 그런데 서로 연결이 되어 있는 집합을 구하는 과정에서 간접적으로도 연결되어 있는 노드도 파악됨.
+ 그래서 두 노드 사이에 간선이 있는지 아님 없는지 판별하는 것으로 변경함
## 2698. Find the Punishment Number of an Integer
+ 힌트에서 recursion으로 모든 경우의 수를 구하면 된다고 함. 그렇지만 익숙하지 않은 알고리즘이라 계속 햇갈림.
  + fn(나누어지는 구간, 다른 구간의 숫자의 합), fn(n,s)
    + n+s를 집합에 넣는다.
    + n을 n1, n2로 나눔
    + fn(n1, n2+s), fn(n2, n1+s) 실행
  + 집합에서는 fn의 실행이 끝나고 나서 n**2가 있는지 확인한다.
## 2661. First Completely Painted Row or Column
+ 왠지 하나씩 칠할때 마다 행이나 열이 완성되었는지 확인 하는 방법은 아닐거 같다.
+ 각 행과 각 열이 완성되는 순서를 먼저 보는 방식으로 해봐야겠다
## 2683. Neighboring Bitwise XOR
+ xor 연산의 법칙을 활용
  + 교환법칙, 결합법칙등  
## 2762. Continuous Subarrays
+ object를 사용해서 최대값과 최소값을 구하는 범위를 줄인다.
  + 현재 구간이 i1\~i2라면 i1과 i2사이에서(`[i1, i2]`) 나오는 숫자의 수를 object로 저장한다. 이 object에서 subarray의 최대값과 최소값을 구한다.
+ 구간의 길이에 따라 subarray의 개수를 계산해서 더해줌. 
  + i2를 증가시킴. 이떄 최대값과 최소값이 차이가 2가 넘으면 i1을 증가 시킨다. 이 경우에는 먼저 i1\~i2까지의 subarray의 개수를 구하고 ii를 증가시킨 후에 i1\~i2까지의 subarray의 개수를 구해서 뺀다.
## 2825. Make String a Subsequence Using Cyclic Increments
+ str1이 str2의 subsequence가 될 수 있다. -&gt; str1에서 일부 문자가 없어도 str2를 만들 수 있다. -&gt; 한번의 loop로 확인 가능
## 2844. Minimum Operations to Make a Special Number
+ hint를 보니 75, 50, 25, 00로 숫자가 끝나면 25로 나누어 떨어진다고 함.
+ 75, 50, 25, 00로 끝나는 수로 만드는 연산의 횟수를 구함.
  + 75로 끝나는 수가 되는 경우
    + 여러 `5`중에 가장 뒤에 있는 `5`와 그 `5`의 왼쪽 중에서 가장 오른쪽에 있는 `7`로 판단
    + 그리고 `7` 뒤에 있는 숫자중에서 `5`를 제외한 숫자의 개수가 연산의 횟수가 됨.
+ 75, 50, 25, 00로 끝나는 수로 만들지 못하는 경우 0이 아닌 digit를 전부 삭제하기 때문에 0이 아닌 숫자의 개수가 연산의 횟수가 됨.
+ 위의 5가지 중에서 가장 적은 수를 출력
## 2872. Maximum Number of K-Divisible Components
+ Topics 참고해서 DFS, 그리고 Hints 참고
  + 힌트 2: 서브 트리의 모든 노드의 합이 k로 나누어 떨어지지 않으면 상위 노드와 합친다.
  + 힌트 3: 서브 트리의 모든 노드의 합이 k로 나누어 떨어지면 상위 노드와 합치지 않는다.
  + 힌트 4: 굳이 각 그룹에 어떤 노드가 들어가 있는지 저장하지 않아도 된다.
+ edges 검색 부분을 빨리 찾도록 변형
## 2873. Maximum Value of an Ordered Triplet I
+ 입력값의 크기가 작아서 3단 루프를 사용
## 2874. Maximum Value of an Ordered Triplet II
+ j를 기준으로 0~j-1에서 최대 값 / j+1~n에서 최대값 을 찾는다
 + 두 구간의 최대값은 미리 계산한다
## 2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
+ 모든 0을 양의 정수로 대체해야 한다.
  + 우선 양의 정수중에 최소값인 1로 replace (hint 1)
+ 0을 양의 정수로 대체하는 데에 크기에 제한이 없다.
  + 모든 0을 1로 대체한 후에 합계를 구하고 나서 판단
  + 0이 하나 이상 있는 경우에도 하나의 0만 값을 대체한다고 가정하고 판단 (hint 2)
## 2929. Distribute Candies Among Children II
+ 2명에게 나누는 횟수를 구하는 로직을 min(n,limit)번 돌린다
## 2940. Find Building Where Alice and Bob Can Meet
+ Editorial 참고함. 그런데 Monotonic Stack 사용시 왜 되는지 알아보는걸 하기 싫다. 그냥 왠지 그럴 기분이 아님. 뇌가 거부함
+ 당연하게도 O(queries * heights)는 타임 아웃 나옴
## 2948. Make Lexicographically Smallest Array by Swapping Elements
+ editorial에서 limit가 2면 1,3이 이동 가능하고 2,5가 이동가능해서 결국 1,3,5 3개의 숫자가 위치를 바꾸는게 가능하다고 함
  + 1,3,5 3가지 숫자를 하나의 그룹으로 보고 그룹별로 index를 모아 정렬해서 앞에 index부터 작은 수를 넣어줌
## 2981. Find Longest Special Substring That Occurs Thrice I
+ object에 substring의 개수를 카운트, 그리고 3번 이상 나온 substring중에서 가장 긴 substring의 길이를 출력.
## 3066. Minimum Operations to Exceed Threshold Value II
+ 배열에서 연속으로 가장 작은 수 2개를 꺼낸다? 우선 순위 큐?
## 3108. Minimum Cost Walk in Weighted Graph
+ 다른 노드로 이동할때 이어저 있는 모든 간선을 지나처서 이동한다.
  + 간선을 중복으로 이동이 가능하고 가중치에 비트 and 연산을 하기 때문
## 3147. Taking Maximum Energy From the Mystic Dungeon
1. 각 i별로 해당 위치에서 시작했을때 결과값을 구함
2. 그 결과값 중에서 가장 큰 값을 출력
## 3152. Special Array II
+ queries가 어려개 라서 양옆이 같은 parity인 경우를 미리 구해서 저장
  - 시간 초과라고 나와서 추가함.
## 3160. Find the Number of Distinct Colors Among the Balls
+ 현재 한개의 공에만 칠해저 있는 색이 몇개인지 알기위해 머리를 썼다. queries마다 모든 공에서 색을 카운트 하면 시간이 많이 들기 때문이다.
  + 3개의 Object를 사용. 각 ball의 색, 1개만 칠해저 있는 색의 숫자, 색 별 총 개수
  + O(queries * balls) -&gt; O(balls)
## 3169. Count Days Without Meetings
+ 거의 유사한 문제를 예전에 본 것 같다.
+ 정렬을 한다. 그리고 1일 부터 처음 미팅 과 간격 + 각 미팅의 간격 + 마지막 미팅 종료 후 끝 날짜 까지 간격을 더해서 출력.
## 3174. Clear Digits
+ 처음에는 문자를 string에서 지워가는 방법과 배열을 놓고 지워진 non-digit를 표시하는 되겠다는 생각을 했다.
+ 그런데 topics에서 stack이라는 키워드를 보자마자 방법이 문득 떠올랐다.
## 3223. Minimum Length of String After Operations
+ 같은 문자가 문자열에 3개 이상 들어있을때 그 중에서 2개를 뺼 수 있다.
## 3264. Final Array State After K Multiplication Operations I
+ 1792에서 priorityqueue 라이브러리를 사용해 봐서 그런지 여기서도 익숙하게 사용함
## 3307. Find the K-th Character in String Game II
+ operations는 최대 100개지만 50번 정도면 이미 최대 k를 넘어감
  + k <= 10**14 < 2**50 < Number.MAX_SAFE_INTEGER
## 3341. Find Minimum Time to Reach Last Room I
+ 최단 경로를 찾을때 우선순위큐에 다음 경로를 추가할 때 조건에 맞는 경로만 추가한다
  + 다음 room에서 이동을 시작 할 수 있는 사간을 보고 판단해서 queue에 넣음
## 3375. Minimum Operations to Make Array Values Equal to K
+ 앞과 뒤의 숫자의 크기가 서로 2이상 차이가 나야 하는줄 착각해서 시간이 더 걸림.
## 3412. Find Mirror Score of a String
+ 문자별로 인덱스를 배열로 저장. 배열안에 숫자는 unmarked index이다.
+ j&lt;i인 j를 찾기 때문에 i앞에 있는 index 만 배열에 들어가 있으면 된다. 미리 넣어놓을 필요가 없다.
+ j를 찾을떄 stack처럼 FILO방식으로 pop을 한다. i랑 가장 가까운 j를 찾기 떄문이다.
+ 해당하는 j가 없으면 i를 push한다.
## 3487. Maximum Unique Subarray Sum After Deletion
- 입력받는 배열에서 음수밖에 없는 경우랑 그 외의 경우를 나누어서 처리해야함
- [-1], [-1,-1], [-1,-1,0], [-1,0], [0]
## 3554. Find Category Recommendation Pairs
+ ProductInfo 에서 product_id가 달라도 같은 category인 경우가 있음. ProductPurchases 에서 quantity는 상관 없다. user의 수를 구하기 때문.
## 3601. Find Drivers with Improved Fuel Efficiency
+ 각 trip에 대해 efficiency를 구해야함
+ first_half_avg, second_half_avg, efficiency_improvement 3가지 다 마지막 까지 계산 후에 round
+ efficiency_improvement > 0 조건으로 null인 경우와 낮아진 경우도 필터링