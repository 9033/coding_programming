# readme
## Profiles
[LeetCode](https://leetcode.com/u/9033/)  
[hackerrank](https://www.hackerrank.com/kkangnet)  
[UVa Online Judge](https://uhunt.onlinejudge.org/id/82804)  
[freeCodeCamp.org](https://www.freecodecamp.org/9033)  
## [Problems by cases](case.md)  
문제 분류 - 알고리즘별, 시간 복잡도별, 자료구조별.  
비슷한 문제를 모아놓음.  
## [Code](code.md)  
알고리즘별 코드.  
수학 - Prime number등.  
기타 - 이분탐색 등.  
## My solutions
[LeetCode](leetCode.md)  
[hackerrank](hackerrank/readme.md)  
[UVa Online Judge](uva_online/readme.md)  
[USACO_Training_Program](USACO_Training_Program/readme.md)  
[programmers](programmers.md)  
# memo
## javascript
+ counter
    ```js
    let arr=[1,2,3,1,2,1,3,1,1,1,1]

    const counter = arr => arr.reduce((cnt, v) => {
      cnt[v] = (cnt[v] || 0) + 1
      return cnt
    }, {} )

    console.log(counter(arr))
    ```
## python
+ loop without for, while  
    ```py
    print(*map(lambda x: x*x,range(9)), sep='\n')
    ```
    ```py
    print(*range(1,9), sep='',end='')
    ```
+ list comprehension  
    ```py
    [[i,j] for i in range(9) for j in range(9) if i+j!=5]
    ```
    ```py
    print(*[str(i)+'x'+str(j)+'='+str(i*j) for i in range(2,10) for j in range(2,10) if i<=j])
    ```
+ using Counter  
    ```py
    import collections
    a=collections.Counter([1,2,3,4,5])
    b=collections.Counter([1,2,3,4])
    a-=b
    print([*a][0])
    ```
+ sort with multi keys  
    ```py
    name=["B","A","C","B","C"]
    score=[52,51,51.5,50,51]
    total=[*zip(name,score)]
    total.sort(key=lambda p:(-p[1],p[0]))#by tuple
    print(total)
    ```
+ insert sort  
    ```py
    import bisect
    sortedArr=[100,200,300,400,500,600,700]
    bisect.insort(sortedArr,550)
    bisect.insort(sortedArr,0)
    bisect.insort(sortedArr,1000)
    print(sortedArr)
    ```
+ bit counter
    ```py
    n=31
    b=bin( n )
    print(b.count('1'))
    ```
+ number of True
    ```py
    strs=['aa','BB','cC','dd']
    print( sum(map(str.islower,strs)))
    ```
+ permultation & combination
    ```py
    #순서무관 : 뽑는 순서는 상관이 없다.
    #순서상관 : 뽑는 순서가 다르면 다른경우다.    
    import itertools
    n=5
    r=3
    arr=[*range(0,n)]
    itertools.product(arr,repeat=r)#중복순열 : 순서상관, 중복허용
    itertools.permutations(arr,r)#순열 : 순서상관, 중복안됨
    itertools.combinations(arr,r)#조합 : 순서무관, 중복안됨
    itertools.combinations_with_replacement(arr,r)#중복 조합 : 순서무관, 중복허용
    ```
+ datetime from string and to string
    ```py
    import datetime
    r=datetime.datetime.strptime("2019-09-17 11:11:11.111","%Y-%m-%d %H:%M:%S.%f")
    print(r)
    t=r-datetime.timedelta(seconds=0.999)
    print(t)
    print(datetime.datetime.strftime(t,"%Y-%m-%d %H:%M:%S.%f"))
    ```
## c
+ modulo big integer
    ```c
    #include<stdio.h>
    int bigmod(char *num,int m){
        int ret=0;
        while(*num){
            ret=(ret*10+(*num)-'0')%m;
            num++;
        }
        return ret;
    }
    int main() {
        char num[1000]="324842959490294584920434765756745534524235445";
        int m=32854;
        printf("%d\n",bigmod(num,m));
    }
    ```
+ [set]
    ```c
    #include<stdio.h>
    int main()
    {
        char st[100];
        scanf("%[^\n]%*c", st);
        printf("%s",st);
        scanf("%[^\n]s", st);
        printf("%s",st);
    }
    ```

## regular expresion
+ `/(ok){3,}/`  
`okokok`, `okokokok`, etc.  

+ `/(\d)\1/`  
true : `11`, `22`  
false : `12`, `23`  
`/(\d)\1/` not eq `/\d\d/`  

+ `/(?<=a)x(?=b)/` : lookbehind, lookahead  
select `x` after `a` and before `b`  

## add value on last
```js
//javascript
a=[]//array object
a.push(1)
a.push(2)
a.push(3)
```
```py
#python
a=[]#list
a.append(1)
a.append(2)
a.append(3)
```
## spread operator
```py
#python
a=[1,2]
c=[5,6,*a]
```
```js
//javascript
a=[1,2]
c=[5,6,...a]
```
## swap
```js
//javascript
[a,b]=[b,a]
```
```py
#python
a,b=b,a
```
