# ProjectEuler+
## Project Euler #1: Multiples of 3 and 5
<pre>
let's use formula for sum-of-numbers.

n   : 1 2 3 4 5 6 7 8  9 10  
n/3 : 0 0 1 1 1 2 2 2  3  3 - count of 3 in number  
    : 0 0 1 1 1 3 3 3  6  6 - sum of below 
*3  : 0 0 3 3 3 9 9 9 18 18  

thus

below 10 : 1~9

1~9 : sum of multiples of 3
1. 9-(9%3)=9
2. 9/3=3
3. n(n+1)/2=3*4/2=6
4. 6*3=18

1~9 : sum of multiples of 5
1. 9-(9%5)=5
2. 5/5=1
3. n(n+1)/2=1*2/2=1
4. 1*5=5

18+5=23
</pre>
```
code
```
