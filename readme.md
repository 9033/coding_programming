## Profiles
[hackerrank](https://www.hackerrank.com/kkangnet)  
[UVa Online Judge](https://uhunt.onlinejudge.org/id/82804)  

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
