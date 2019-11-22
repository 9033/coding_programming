# readme
## Profiles
[hackerrank](https://www.hackerrank.com/kkangnet)  
[UVa Online Judge](https://uhunt.onlinejudge.org/id/82804)  
## [Problems by cases](case.md)  
링크 참조.  
## My solutions
[hackerrank](hackerrank/readme.md)  
[UVa Online Judge](uva_online/readme.md)  
[USACO_Training_Program](USACO_Training_Program/readme.md)  
[programmers](programmers.md)  
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
+ isprime?
    ```py
    def isprime(n):
        if n==2:
            return True
        if n%2==0:
            return False
        if n==1:
            return False    
        sqrtN=int( pow(n,1/2) )
        for x in range(3,sqrtN+1,2):
            if n%x==0:
                return False
        return True
    ```
+ prime numbers to N
    ```py
    def primenum(N):
        cut=int(N**(1/2))
        primenums=[2]
        for i in range(3,N+1,2):
            p=True
            for c in primenums:
                if i%c==0:
                    p=False
                    break
                elif c>cut:
                    break
            if p:
                primenums.append(i)
            if i>cut:
                break
        #primenums.append(1)
        return primenums
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
+ number to string by radix
    ```py
    def radix(n,r):#n을 r진법으로 출력
        ret=""
        if n==0:
            return "0"
        while n>0:
            n,m=divmod(n,r)
            ret="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[m]+ret
        return ret
    ```
+ all divisors of the number
    ```py
    def divisors(n):#n과 n의 약수들을 오름차 순으로 출력
        r1=[]
        r2=[]
        sqrtn=int(n**(1/2))
        for a in range(1,sqrtn):
            if not n%a:
                r1.append(a)
                r2.append(n//a)
        if sqrtn*sqrtn==n:
            r1.append(sqrtn)
        r2.reverse()
        return r1+r2

    print(divisors(244324**2))
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
