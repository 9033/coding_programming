# Practice > C
## Conditionals and Loops
### Printing Pattern using Loops
<pre>
* n : 1
1

* n : 2

2 2 2
2 1 2 
2 2 2

* n : 3

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3

square is 2n-1 x 2n-1.


 x  3 2 1 2 3
y
3   3 3 3 3 3
2   3 2 2 2 3
1   3 2 1 2 3
2   3 2 2 2 3
3   3 3 3 3 3

square number : max(x,y)

</pre>
```c
#include <stdio.h>

int puty(int n,int x){
    int y;
    for(y=n;y>=1;y--){
        printf("%d ",x>y?x:y);
    }
    for(y=2;y<=n;y++){
        printf("%d ",x>y?x:y);
    }
    putchar('\n');
    return 0;
}

int main(){
    int x,n;
    scanf("%d", &n);
    for(x=n;x>=1;x--){
        puty(n,x);
    }
    for(x=2;x<=n;x++){
        puty(n,x);
    }
    return 0;
}
```
