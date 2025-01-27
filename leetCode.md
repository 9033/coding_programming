# 문제별
내가 풀이한 방법에 대한 설명  
LeetCode 문제 목록 링크: [Problems](https://leetcode.com/problemset/)  
## 18. 4Sum
+ `15. 3sum`에서 루프문 하나를 더 추가.
  + 이중 루프로 모든 경우의 수를 처리해야함.
## 35. Search Insert Position
+ binary search
## 63. Unique Paths II
+ 시작 지점에도 장애물이 있을 수 있다.
## 139. Word Break
+ wordDict에 있는 단어가 여러번 쓰일 수 있다. -&gt; s의 길이까지 문자열을 조합하는 도중에 현재 길이의 문자열을 생성한 적이 있으면 skip
## 183. Customers Who Never Order
+ 서브쿼리보다 left join이 속도가 빠르다.
## 515. Find Largest Value in Each Tree Row
+ binary tree가 나오는 이전 문제(2471, 2415등)에서 사용한 BFS 코드를 재활용. 마찬가지로 다음 레벨을 탐색하기 직전에는 큐에 다음 레벨의 노드만 들어가 있다는 점을 활용함.
+ 트리가 빈 경우를 채크하는 부분 추가.
## 769. Max Chunks To Make Sorted
+ 배열을 그냥 정렬할때와 chunk로 나누어서 각각 정렬 후에 합친 결과가 같다 -> 앞에 있는 chunk의 최대 숫자 < 뒤에 있는 chunk의 최소 숫자
+ 정렬은 오름차순으로 하면 된다.
## 802. Find Eventual Safe States
+ 모든 경로가 terminal node에 도달한다는 것을 계산하려고 보니 왠지 복잡하다
+ terminal node로 가지 않는 경로가 하나라도 있는 경우는 cycle이 되는경로로 하나라도 향하는 경로가 있는 경우다
+ DFS로 탐색하면서 terminal node와 cycle로 가는 경로가 있는 노드 이렇게 두가지를 채크 하면서 탐색해야 함.
  + terminal node거나 terminal node로만 가는 경로만 있는 노드를 채크해서 탐색하는 가지수를 줄인다.
  + cycle로 가는 경로가 하나라도 있는 경우도 채크해서 탐색하는 가지수를 줄이고 답을 출력하면 된다.
## 983. Minimum Cost For Tickets
+ 1D DP 이며 2466과 거의 유사
+ 여행을 가지 않는 날인 경우 cost를 이전 날의 cost와 같게 한다.
## 1217. Minimum Cost to Move Chips to The Same Position
+ DP: O(n^2) (position * position)
  + 위치의 범위는 넓지만 칩의 위치의 경우의 수가 1000개 때문에 가능
+ O(n)이 존재한다
## 1267. Count Servers that Communicate
+ N-queen하고 비슷해 보임, 그리고 2661하고도 비슷해 보임
+ 행에 대해서 2개 이상인지 확인, 2개 이상이면 전부 카운트
+ 열에 대해서 2개 이상인지 확인, 2개 이상이면 전부 카운트
+ 그리고 중복해서 카운트 하는 경우를 방지함
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
## 1639. Number of Ways to Form a Target String Given a Dictionary
vscode의 코파일럿(무료)가 알려주는데 cutting하는 조건을 처음에 다 알려주지 않는다.
그리고 제시한 코드가 왜 정답이 나오게 되는지 이해하는데 시간이 걸림.

+ 각 문자열에 대한 각 문자의 개수를 하나의 객체로 만든다.
  - 코파일럿의 코드는 이 방법이다. 나는 각 word별로 만들려고 생각함
+ memoization를 사용한다.
  - 시간 초과라고 나와서 추가함.
+ words의 남은 문자열이 target의 남은 문자열보다 작으면 0을 반환한다.
  - 시간 초과라고 나와서 추가함.
## 1765. Map of Highest Peak
+ editorial에서 water까지 최단거리를 구하는 방식으로 함
+ priority queue로 탐색을 해서 여러 지점 에서 출발해서 각 cell의 최단거리를 구하게 변경
+ cell에서 가장 가까운 water까지 거리를 구하는 셈
## 1769. Minimum Number of Operations to Move All Balls to Each Box
+ 공의 개수를 세고, 이동 횟수를 세는 방식으로 풀이 (prefix sum)
+ 양쪽 구간으로 나누어서 함
  + l[i]는 0\~i까지 1의 개수, r[i]는 i\~n-1까지 1의 개수
  + i까지 0\~i-1 공의 이동 횟수, i까지 i+1\~n-1 공의 이동 횟수
## 1792. Maximum Average Pass Ratio
+ 최대 우선순위 큐를 사용함
+ leetcode에 기본적으로 javascript에서 `@datastructures-js/priority-queue@5.4.0`를 사용할 수 있다.
  + https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages
## 1930. Unique Length-3 Palindromic Subsequences
+ 양 옆의 구간의 개수를 보고 palindrome이 되는지 확인 (prefix sum, O(n))
  + 1\~s-1의 루프에서 같은 문자가 왼쪽에 하나라도 있고 오른쪽에 하나라도 있으면 palindrome이 됨
+ editorial는 양 끝을 잡고 중간에 문자의 수를 확인. 중복되는 문자는 한번만 센다
## 2054. Two Best Non-Overlapping Events
+ DP로 푸는 경우: max(현재 이벤트 이전까지 1개만 선택하는 경우의 최대 value + 현재 이벤트의 value, 현재 이벤트의 끝나는 time까지 다른 이벤트를 2개 선택한 경우의 최대 value)
## 2116. Check if a Parentheses String Can Be Valid
+ stack으로 뭔가 해보려다가 잘 안됨
+ 앞에서 뒤로, 뒤에서 앞으로 2-pass로 검증
+ hint 3가지를 참고함, 2-pass로 그중에 2가지를 검증
+ false되는 경우는 hint 1까지 포함해서 총 3가지.
+ locked일때 '(', ')'와 unlocked일때, 총 3가지의 개수로 판단
## 2133. Check if Every Row and Column Contains All Numbers
+ lodash zip과 set을 이용함
## 2182. Construct String With Repeat Limit
+ 입력값의 순서와 출력값의 순서가 관련이 없어서 각 문자의 빈도수를 채크해서 처리함
## 2270. Number of Ways to Split Array
+ 1422와 유사한 문제
+ 0\~i 와 i+1\~n-1의 두 구간의 합을 비교한다.
## 2337. Move Pieces to Obtain a String
+ 이중 루프 대신 단일 루프를 사용. 안되는 경우를 거른다.
+ 예제 테스트 케이스에 없는 L과 R이 번갈아서 나오는 경우를 테스트 케이스로 생각하는 것도 시간이 걸림.
  ```
  Input: start = "___L____R____L", target = "__L______RL___"
  Output: true

  Input: start = "___L____L___R_", target = "__L______RL___"
  Output: false
  ```
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
## 2471. Minimum Number of Operations to Sort a Binary Tree by Level
+ 같은 레벨의 노드들을 찾는것은 2415. Reverse Odd Levels of Binary Tree에서 활용한 BFS를 가지고 옴. 큐에 같은 레벨의 노드가 있을때 swap 횟수를 구하고 해당 레벨을 채크해서 한 레벨에서 swap횟수를 중복으로 구하지 않게함.
+ SWAP횟수를 확인하는 알고리즘은 editorial를 참고. 여기서는 같은 값은 트리에서 한번만 나오기 떄문에 위치를 저장해서 활용함
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
## 2593. Find Score of an Array After Marking All Elements
+ indexing 으로 가장 작은 수 (같으면 가장 작은 index) 를 찾는 것을 빠르게 함
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
## 2940. Find Building Where Alice and Bob Can Meet
+ Editorial 참고함. 그런데 Monotonic Stack 사용시 왜 되는지 알아보는걸 하기 싫다. 그냥 왠지 그럴 기분이 아님. 뇌가 거부함
+ 당연하게도 O(queries * heights)는 타임 아웃 나옴
## 2948. Make Lexicographically Smallest Array by Swapping Elements
+ editorial에서 limit가 2면 1,3이 이동 가능하고 2,5가 이동가능해서 결국 1,3,5 3개의 숫자가 위치를 바꾸는게 가능하다고 함
  + 1,3,5 3가지 숫자를 하나의 그룹으로 보고 그룹별로 index를 모아 정렬해서 앞에 index부터 작은 수를 넣어줌
## 2981. Find Longest Special Substring That Occurs Thrice I
+ object에 substring의 개수를 카운트, 그리고 3번 이상 나온 substring중에서 가장 긴 substring의 길이를 출력.
## 3152. Special Array II
+ queries가 어려개 라서 양옆이 같은 parity인 경우를 미리 구해서 저장
  - 시간 초과라고 나와서 추가함.
## 3223. Minimum Length of String After Operations
+ 같은 문자가 문자열에 3개 이상 들어있을때 그 중에서 2개를 뺼 수 있다.
## 3264. Final Array State After K Multiplication Operations I
+ 1792에서 priorityqueue 라이브러리를 사용해 봐서 그런지 여기서도 익숙하게 사용함
## 3412. Find Mirror Score of a String
+ 문자별로 인덱스를 배열로 저장. 배열안에 숫자는 unmarked index이다.
+ j&lt;i인 j를 찾기 때문에 i앞에 있는 index 만 배열에 들어가 있으면 된다. 미리 넣어놓을 필요가 없다.
+ j를 찾을떄 stack처럼 FILO방식으로 pop을 한다. i랑 가장 가까운 j를 찾기 떄문이다.
+ 해당하는 j가 없으면 i를 push한다.