# 문제별
[Problems](https://leetcode.com/problemset/)
## 18. 4Sum
+ `15. 3sum`에서 루프문 하나를 더 추가.
  + 이중 루프로 모든 경우의 수를 처리해야함.
## 35. Search Insert Position
+ binary search
## 63. Unique Paths II
+ 시작 지점에도 장애물이 있을 수 있다.
## 183. Customers Who Never Order
+ 서브쿼리보다 left join이 속도가 빠르다.
## 515. Find Largest Value in Each Tree Row
+ binary tree가 나오는 이전 문제(2471, 2415등)에서 사용한 BFS 코드를 재활용. 마찬가지로 다음 레벨을 탐색하기 직전에는 큐에 다음 레벨의 노드만 들어가 있다는 점을 활용함.
+ 트리가 빈 경우를 채크하는 부분 추가.
## 769. Max Chunks To Make Sorted
+ 정렬은 오름차순으로 하면 된다.
## 983. Minimum Cost For Tickets
+ 1D DP 이며 2466과 거의 유사
+ 여행을 가지 않는 날인 경우 cost를 이전 날의 cost와 같게 한다.
## 1475. Final Prices With a Special Discount in a Shop
+ 본문에 있는대로 코드를 짜면 된다.
## 1639. Number of Ways to Form a Target String Given a Dictionary
vscode의 코파일럿(무료)가 알려주는데 cutting하는 조건을 처음에 다 알려주지 않는다.
그리고 제시한 코드가 왜 정답이 나오게 되는지 이해하는데 시간이 걸림.

+ 각 문자열에 대한 각 문자의 개수를 하나의 객체로 만든다.
  - 코파일럿의 코드는 이 방법이다. 나는 각 word별로 만들려고 생각함
+ memoization를 사용한다.
  - 시간 초과라고 나와서 추가함.
+ words의 남은 문자열이 target의 남은 문자열보다 작으면 0을 반환한다.
  - 시간 초과라고 나와서 추가함.
## 2054. Two Best Non-Overlapping Events
+ DP로 푸는 경우: max(현재 이벤트 이전까지 1개만 선택하는 경우 + 현재 이벤트 선택)
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
## 2466. Count Ways To Build Good Strings
+ 1D DP로 각 길이에 대한 경우의 수를 구한다.
  - 길이가 0인 경우의 수는 1가지.
+ 그리고 길이가 low부터 high까지인 문자열의 각 경우의 수를 더하면 된다.
## 2471. Minimum Number of Operations to Sort a Binary Tree by Level
+ 같은 레벨의 노드들을 찾는것은 2415. Reverse Odd Levels of Binary Tree에서 활용한 BFS를 가지고 옴. 큐에 같은 레벨의 노드가 있을때 swap 횟수를 구하고 해당 레벨을 채크해서 한 레벨에서 swap횟수를 중복으로 구하지 않게함.
+ SWAP횟수를 확인하는 알고리즘은 editorial를 참고. 여기서는 같은 값은 트리에서 한번만 나오기 떄문에 위치를 저장해서 활용함
## 2554. Maximum Number of Integers to Choose From a Range I
+ 여러 제약 조건을 고려하면 단일 루프로 가능하다.
    + 최대 숫자인 경우만 출력, 숫자는 한번만 선택, maxSum 이하면 됨.
+ banned에 한 숫자가 2번 들어갈 수 있음
## 2593. Find Score of an Array After Marking All Elements
+ indexing 으로 가장 작은 수 (같으면 가장 작은 index) 를 찾는 것을 빠르게 함
## 2940. Find Building Where Alice and Bob Can Meet
+ Editorial 참고함. 그런데 Monotonic Stack 사용시 왜 되는지 알아보는걸 하기 싫다. 그냥 왠지 그럴 기분이 아님. 뇌가 거부함
+ 당연하게도 O(queries * heights)는 타임 아웃 나옴
