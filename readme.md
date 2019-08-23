# readme
## Profiles
[hackerrank](https://www.hackerrank.com/kkangnet)  
[UVa Online Judge](https://uhunt.onlinejudge.org/id/82804)  
## My solutions
[hackerrank](hackerrank/readme.md)  
[UVa Online Judge](uva_online/readme.md)  
[USACO_Training_Program](USACO_Training_Program/readme.md)  
# memo
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
    total.sort(key=lambda p:(-p[1],p[0]))
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
    
## c
+ [set]
    ```c
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
