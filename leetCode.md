# 문제별
## 18. 4Sum
+ `15. 3sum`에서 루프문 하나를 더 추가.
  + 이중 루프로 모든 경우의 수를 처리해야함.
## 35. Search Insert Position
+ binary search
## 63. Unique Paths II
+ 시작 지점에도 장애물이 있을 수 있다.
## 183. Customers Who Never Order
+ 서브쿼리보다 left join이 속도가 빠르다.
## 769. Max Chunks To Make Sorted
+ 정렬은 오름차순으로 하면 된다.
## 1475. Final Prices With a Special Discount in a Shop
+ 본문에 있는대로 코드를 짜면 된다.
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
