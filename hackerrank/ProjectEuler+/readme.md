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
*Number.MAX_SAFE_INTEGER in javascript < 10^10 < 2^63 (long long in c) < BigInteger in java*
```java
// java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static BigInteger px(int n,int e){
        int x=n-(n%e);
        x=x/e;
        BigInteger x1=BigInteger.valueOf(x);        
        x1=x1.multiply(x1.add( BigInteger.valueOf(1) ));
        x1=x1.divide( BigInteger.valueOf(2) );
        return x1.multiply( BigInteger.valueOf(e) );
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            System.out.println( (px(n-1,3).add( px(n-1,5) )).subtract( px(n-1,15) ) );
        }
    }
}
```
```c
// c
#include <stdio.h>

long long px(int n,int e){
    int x=n-(n%e);
    x=x/e;
    long long x1=x;
    x1=x1*(x1+1)/2;
    return x1*e;
}

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        scanf("%d",&n);
        printf("%lld\n", px(n-1,3)+px(n-1,5)-px(n-1,15));
    }
    return 0;
}
```
