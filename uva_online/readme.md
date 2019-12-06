# Index
[100 - The 3n + 1 problem](#100---the-3n--1-problem)  
[193 - Graph Coloring](#193---Graph-Coloring)  
[374 - Big Mod](#374---big-mod)  
[469 - Wetlands of Florida](#469---Wetlands-of-Florida)  
[495 - Fibonacci Freeze](#495---Fibonacci-Freeze)  
[530 - Binomial Showdown](#530---Binomial-Showdown)  
[665 - False coin](#665---False-coin)  
[893 - Y3K Problem](#893---Y3K-Problem)  
[924 - Spreading the News](#924---Spreading-the-News)  
[10013 - Super long sums](#10013---Super-long-sums)  
[10023 - Square root](#10023---Square-root)  
[10106 - Product](#10106---Product)  
[10494 - If We Were a Child Again](#10494---if-we-were-a-child-again)  
[10523 - Very Easy !!!](#10523---Very-Easy-!!!)  
[10551 - Basic Remains](#10551---Basic-Remains)  
[10905 - Children's Game](#10905---Children's-Game)  
[10943 - How do you add?](#10943---How-do-you-add?)  
[11121 - Base -2](#11121---Base--2)  
[11636 - Hello World!](#11636---Hello-World!)  
[11850 - Alaska](#11850---Alaska)  
[11984 - A Change in Thermal Unit](#11984---A-Change-in-Thermal-Unit)  
[12293 - Box Game](#12293---Box-Game)  
# 100 - The 3n + 1 problem
<pre>
일단 답이 나오는 소스 대략 0.6초걸림
</pre>
```cpp
/*
2010-12-29
//
//
100
The 3n + 1 problem
//
0.592s
*/
#include<iostream>

#define For(X,START,END) for(X = START; X <= END; X++)

using namespace std;

int cycle(int N){
    int cnt = 1;//including number 1
    while(N!=1){
        if(N%2){
            N = 3* N + 1;
        }
        else{
            N >>= 1;
        }
        cnt++;
    }
    return cnt;
}

int main()
{
    //****************
    //start of process
    //****************
    int a,b;
    while(cin >> a >> b){
        cout << a << ' ' << b << ' ';
        if(a>b){
            swap(a,b);
        }
        int ret = 0;
        int n;
        For(n,a,b){
            ret = max(ret,cycle(n));
        }
        cout << ret << endl;
    }
    //****************
    //end of process
    //****************
#ifndef _useCpp
    fcloseall();
#endif
    return 0;
}
```

<pre>
수열을 계산할때 반복하는 부분을 최소화
</pre>
```cpp
/*
2010-12-29
//
//
100
The 3n + 1 problem
//
use more memory
//
0.036s
*/
#include<iostream>
#include<vector>

#define For(X,START,END) for(X = START; X <= END; X++)

using namespace std;

vector<int> pre(1000001);

int cycle(int N){
    int cnt = 1;//including number 1
    while(N>1){
        if( N<=1000000){
            if(pre.at(N) !=0){
                return cnt+pre.at(N)-1;
            }
        }
        if(N%2){
            N = 3* N + 1;
        }
        else{
            N >>= 1;
        }
        cnt++;
    }
    return cnt;
}

int main()
{
    //****************
    //start of process
    //****************
    int a,b;
    while(cin >> a >> b){
        cout << a << ' ' << b << ' ';
        if(a>b){
            swap(a,b);
        }
        int ret = 0;
        int n;
        For(n,a,b){
            if( pre.at(n)==0 ){
                pre.at(n) = cycle(n);
            }
            ret = max(ret,pre.at(n));
        }
        cout << ret << endl;
    }
    //****************
    //end of process
    //****************
    return 0;
}
```

<pre>
cycle함수를 수정함.
현재의 N값을 기억한다. 그리고 그 다음 N값을 구한다.
다음 루프에서 만약 pre에서 N값에 해당하는 값이 있을경우
그 값에다 1을 더해서 이전에 N값에 해당하는 pre배열에다가 값을 대입한다.
이전에 N값에서 한번 더 루프를 돌아서 현재 N값으로 왔기 때문이다.
</pre>
```cpp
/*
2010-12-29
//
//
100
The 3n + 1 problem
//
use more memory
//
0.036s
2015-09-10
*/
#include<iostream>
#include<vector>

#define For(X,START,END) for(X = START; X <= END; X++)

using namespace std;

vector<int> pre(1000001);

int cycle(int N) {
    int cnt = 1;//including number 1
    int before = N;
    while (N>1) {
        before = N;
        if (N % 2) {
            N = 3 * N + 1;
        }
        else {
            N >>= 1;
        }
        cnt++;
        if (N <= 1000000) {
            if (pre.at(N) != 0) {
                if (before <= 1000000) {
                    pre.at(before) = pre.at(N) + 1;
                }
                return cnt + pre.at(N) - 1;
            }
        }
    }
    return cnt;
}

int main()
{
    //****************
    //start of process
    //****************
    int a,b;
    while(cin >> a >> b){
        cout << a << ' ' << b << ' ';
        if(a>b){
            swap(a,b);
        }
        int ret = 0;
        int n;
        For(n,a,b){
            if( pre.at(n)==0 ){
                pre.at(n) = cycle(n);
            }
            ret = max(ret,pre.at(n));
        }
        cout << ret << endl;
    }
    //****************
    //end of process
    //****************
    return 0;
}

```

# 374 - Big Mod
<pre>
P번을 곱하면 시간이 많이 걸린다.
P번 곱하는건 결국 P/2번 곱한걸 제곱하고 P%2번 곱한걸 곱해주면 같은 값이 나온다.(P/2에서 소숫점은 버림.) 물론 곱할때마다 %M연산이 추가로 들어간다. P번을 곱하는 것보다 시간차이가 엄청 많이 난다.
P/2번 곱한걸 제곱 하니까 이미 구한 해를 재활용하는 동적계획법같다.
</pre>
```cpp
/*
374 - Big Mod
2015-09-14
*/
#include<stdio.h>
int mulmod(int B, int P, int M) {
    if (P == 1) {
        return B%M;
    }
    else if (P == 0) {
        return 1;
    }
    int ret;
    ret = mulmod(B, P/2, M);
    ret = (ret*ret)%M;
    ret = ret * mulmod(B, P % 2, M);
    return ret%M;
}
int main() {
    int B, P, M;
    while (3 == scanf("%d %d %d", &B, &P, &M)) {
        int ans;
        B %= M;
        ans = mulmod(B, P, M);
        printf("%d\n", ans);
    }
    return 0;
}
```

# 495 - Fibonacci Freeze
<pre>
해당 순서의 피보나치 수를 출력한다. (문제에서 순서는 0부터 시작함)

배열을 이용해서 피보나치 수를 입력값만큼 구한다. 다만 이미 구해저 있으면 그 값을 바로 출력해준다. 이전에 입력중에 최대값을 기억한후 현재 입력이 최대값보다 같거나 작으면 구해저 있으니 바로 출력한다.
다만 아주 쉽게 64비트 정수형을 넘어가서 n이 5000일경우 1045자리의 정수가 된다. 그래서 큰 정수의 덧셈을 처리하는 클레스를 만들던지 아니면 자바에서 라이브러리를 써야한다.
</pre>
```cpp
/*
495 - Fibonacci Freeze
2015-09-17
*/
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
class verylonginteger {
public:
    std::vector<long long> i;//max : 18446744073709551615
    long long reversestoi(std::string s) {
        long long digit = 1;
        long long ret = 0;
        for (auto it = s.begin(); it < s.end(); it++) {
            ret += ((*it) - '0')*digit;
            digit *= 10;
        }
        return ret;
    }
    long long get(int idx) {
        if (this->i.size() > idx) {
            return this->i[idx];
        }
        return 0;
    }
    bool set(int idx, long long v) {
        if (this->i.max_size() <= idx)
            return false;
        if (this->i.size() <= idx) {
            this->i.resize(idx + 1);
        }
        this->i[idx] = v;
        return true;
    }
    verylonginteger() {
        this->i.resize(10);
        for (long long &l : this->i)l = 0;
    }
    verylonginteger(std::string s) {
        this->i.resize(10);
        for (long long &l : this->i)l = 0;
        std::reverse(s.begin(), s.end());
        std::string t;
        int digits = 18;
        for (int i = 0;i<this->i.max_size(); i++) {
            if (s.size() > digits * i) {
                t = s.substr(digits * i, digits);
                this->set(i, this->reversestoi(t));
            }
            else {
                break;
            }
        }
    }
    ~verylonginteger() {
    }
    bool operator=(long long b) {
        for (long long &l : this->i)l = 0;
        return this->set(0, b);
    }
    bool operator=(verylonginteger b) {
        this->i.resize(b.i.size());
        std::copy(b.i.begin(), b.i.end(), this->i.begin());
        return true;
    }
    friend bool operator==(verylonginteger a, long long b) {
        if (a.i[0] == b && std::all_of(a.i.begin() + 1, a.i.end(), [](long long i) {return i == 0; }))return true;
        return false;
    }
    friend verylonginteger operator+(verylonginteger a, verylonginteger b) {
        lldiv_t c;
        long long carry = 0;
        verylonginteger ret;
        ret.i.resize(std::max(a.i.size(),b.i.size()));
        for (int i = 0;i<ret.i.max_size(); i++) {
            long long na=0, nb=0;
            na = a.get(i);
            nb = b.get(i);
            c = lldiv(na+nb + carry, 1000000000000000000LL);
            if (na + nb + carry == 0)break;
            ret.set(i, c.rem);
            carry = c.quot;
        }
        return ret;
    }
    std::string tostring() {
        std::string ret;
        char buf[21];
        auto it = this->i.rbegin();
        bool first = true;
        for (; it < this->i.rend(); it++) {
            if (!first) {
                sprintf(buf, "%018lld", *it);
                ret.append(buf);
            }
            else if (*it > 0) {
                sprintf(buf, "%lld", *it);
                ret.append(buf);
                first = false;
            }
        }
        if (first) {
            sprintf(buf, "%lld", 0LL);
            ret.append(buf);
        }
        return ret;
    }
};
verylonginteger fibonaccin[5001];
int calculated;
int main() {
    fibonaccin[1] = 1;
    calculated = 1;
    int n = 5;
    while (1== scanf("%d", &n)) {
        while (n > calculated) {
            calculated++;
            fibonaccin[calculated]=fibonaccin[calculated - 1] + fibonaccin[calculated - 2];
            //printf("The Fibonacci number for %d is %s\n", calculated, fibonaccin[calculated].tostring().data());
        }
        printf("The Fibonacci number for %d is %s\n", n, fibonaccin[n].tostring().data());
    }
    return 0;
}
```

# 10106 - Product
```java
/*
10106 - Product

2015-09-20
*/
import java.io.*;
import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            System.out.println(sc.nextBigInteger().multiply(sc.nextBigInteger()));
        }
    }
}
```

# 10494 - If We Were a Child Again
```java
/*
10494 - If We Were a Child Again

2015-09-20
*/
import java.io.*;
import java.util.*;
import java.math.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            BigInteger N1 = sc.nextBigInteger();
            String Op = sc.next();
            BigInteger N2 = sc.nextBigInteger();
            BigInteger ret;            
            if(Op.equals("/")){//compare string by value
                ret = N1.divide(N2); 
            }
            else {
                ret = N1.mod(N2);
            }
            System.out.println(ret);
        }
    }
}
```

# 10551 - Basic Remains
<pre>
p,m은 양의 정수
p % m
b 진수(2~10)
p는 1000자리며 0에서 b-1까지
m은 9자리, 0에서 b-1까지

입력
b p m
마지막 줄에는 0이 있음.
</pre>
```java
/*
10551 - Basic Remains

2015-09-20
*/
import java.io.*;
import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            int b = sc.nextInt();
            if(b==0)break;
            System.out.println(sc.nextBigInteger(b).mod(sc.nextBigInteger(b)).toString(b));
        }
    }
}
```

# 11636 - Hello World!
<pre>
log2에서 나온 숫자를 ceil등을 이용해서 같거나 큰 정수를 구하면 그게 곱한 횟수다.
</pre>
```cpp
/*
11636 - Hello World!

한 문장을 복사해서 원하는 갯수만큼 만드는 최소한의 ctrl+c,ctrl+v의 횟수.
연속해서 2를 곱하면서 원하는 갯수 이상이 나오면 곱한 횟수를 출력하면 된다.
이때 곱한 횟수를 루프를 이용하지 않고 log2를 사용한다.
log2에서 나온 숫자를 ceil등을 이용해서 같거나 큰 정수를 구하면 그게 곱한 횟수다.
2015-09-07
*/
#include<iostream>
#include<cmath>
int main() {
    int iCase = 1;
    while (1) {
        int N;
        std::cin >> N;
        if (N < 0)
            break;
        std::cout << "Case " << iCase++ <<": "<< (int)std::ceil(std::log2(N)) << std::endl;
    }
}
```

# 12293 - Box Game
<pre>
n개의 공이 있다고. 문제의 그림에는 n이 5인경우. Alice가 승리.
그러니까 (1,1)로 만드는 인간이 승리한다고. 승리하는 경우의 수를 찾아야 한다. 음 그 뭐더라 30인가 15인가 먼저 부르는사람이 지는건지 이기는건지 햇갈리는데 그런 게임이 생각난다.
각 단계에서 가장 많이 들어가 있는 박스의 공 수만 중요해 보인다. 적은 수가 들어간 박스의 공은 버리니까.

(2,1) -> (1,1) : alice win
(3,1) -> (2,1),(1,2) ... : bob win
(4,1) -> (3,1) ... : alice win
(4,1) -> (2,2) ... : bob win: 그래서 이 루트는 alice가 안함.
(5,1) -> (4,1) ... : bob win: 그래서 이 루트는 alice가 안함.
(5,1) -> (3,2) ... : alice win
(6,1) -> (5,1) ... : bob win: 그래서 이 루트는 alice가 안함.
(6,1) -> (4,2) ... : bob win: 그래서 이 루트는 alice가 안함.
(6,1) -> (3,3) ... : alice win
(7,1) -> (6,1) ... : bob win
(7,1) -> (5,2) ... : bob win
(7,1) -> (4,3) ... : bob win
(8,1) -> (7,1) ... : alice win
(8,1) -> (6,2) ... : bob win: 그래서 이 루트는 alice가 안함.
(8,1) -> (5,3) ... : bob win: 그래서 이 루트는 alice가 안함.
(8,1) -> (4,4) ... : bob win: 그래서 이 루트는 alice가 안함.
(9,1) -> (8,1) ... : bob win: 그래서 이 루트는 alice가 안함.
(9,1) -> (7,2) ... : alice win
(9,1) -> (6,3) ... : bob win: 그래서 이 루트는 alice가 안함.
(9,1) -> (5,4) ... : bob win: 그래서 이 루트는 alice가 안함.
(15,1) -> 
(31,1) -> (30,1)
(31,1) -> (16,15)

alice가 승리하는 공의 갯수 : 2, 4 5 6, 8 9 10 11 12 13 14, 16~30,
bob이 승리하는 공의 갯수 : 3 7 15 31

bob의 승리하는 n의 숫자가 앞의 숫자보다 2를 곱하고 1을 더하면 된다. 그러니까 3*2+1=7, 7*2+1=15, 15*2+1=31

function a(b){ while(b>1){b=b-1;b=b/2;}return b} 1을 리턴하면 bob의 슨리
n이 2의 정수승보다 1작으면 bob이 승리하는 숫자다.

위의 코드를 c로 넣으니 값이 잘 안나온다. int여서 그런가 보다. 실수형으로 연산을 반복하긴 찝찝하다. (다시 보니 1을 더하고 shift연산을 하면 됩니다.)
n에 1을 더하고 bitset에 =연산자로 바로 대입. count함수로 비트의 개수를 구함.
(NOTE: sizeof (decltype (N))*8 = sizeof(int)*8)
</pre>
```cpp
/*
12293 - Box Game
2015-09-07
*/
#include<iostream>
#include<bitset>
int main() {
    while (1) {
        int N;
        std::cin >> N;
        if (N == 0)
            break;
        std::bitset<sizeof(decltype(N))*8> b;
        b = N+1;
        if (b.count() == 1) {
            std::cout << "Bob\n";
        }
        else {
            std::cout << "Alice\n";
        }
    }
}
```

# 11984 - A Change in Thermal Unit
<pre>
초기의 섭씨 온도와 변화한 온도가 화씨로 입력된다. 최종 섭씨 온도는 ?

단순하게 화씨로 표시된 온도의 변화량을 섭씨로 변경해서 더해주면 정답이 나오지 않음.
전부 화씨로 변경해서 더해준후 섭씨로 변환해야 원하는 답이 나옴.
</pre>

# 893 - Y3K Problem
<pre>
400년간의 날의 수는 146097로 일정하다.
이 성질을 이용해서 루프를 돌리는 수를 줄인다.
</pre>

# 469 - Wetlands of Florida
<pre>
이미 넓이를 구한 호수의 좌표면 구해 놓은 해당 호수의 넓이를 출력.
</pre>

# 10013 - Super long sums
<pre>
1000000자리수의 두 숫자의 덧셈.

왼쪽의 자리수부터 들어온다. 그래서 전부 메모리에 저장함.
오른쪽자리부터 덧셈을 계산해서 저장.
결과에서 왼쪽 자리부터 출력.

메모리 관점에서 보면 배열 3개가 아닌 결과를 저장할 배열 하나만 필요한게 포인트인 문제같음.
</pre>

# 11121 - Base -2
<pre>
-2진수
-2진수라서 -가 필요없다고 한다.

진법을 변환할때 나머지는 음수가 아닌 양수로 나오게 해야 한다. 그 나머지를 빼주는 것은 같다.
-2가 아닌 2의 나머지를 구하면 됨.
-2진수라도 digit는 0,1이라서 그런거 같음. (0, -1이 아니라)
</pre>

# 530 - Binomial Showdown
<pre>
n개중 r개와 n개중 (n-r)개는 가짓수가 같다. 그래서 k번 루프를 돌때 r과 (n-r)중 적은 수로 돌리면됨.
</pre>

# 10905 - Children's Game
<pre>
숫자중에서 가장 긴 길이가 아닌 그 2배를 기준으로 정렬함.
</pre>

# 193 - Graph Coloring
<pre>
출력인 블랙인 노드의수.
블랙인 노드의 숫자. : 제대로만 출력하면 된다. udebug결과랑 달라도 무관.
</pre>

# 10943 - How do you add?
<pre>
동적 프로그래밍.
</pre>

# 924 - Spreading the News
<pre>
간선에 방향이 있음.
희소 그래프(sparse graph), 친구를 파악할때 set 자료구조를 쓰는걸 추천.
</pre>

# 10523 - Very Easy !!!
<pre>
파이썬에서는 루프 한번에 곱셈을 두번하는 방법보다 한번 하는게 더 빠르다.  
</pre>

# 11850 - Alaska
<pre>
목적지에는 충전소가 없다.  
</pre>

# 665 - False coin
<pre>
완전 탐색.
</pre>

# 10023 - Square root
<pre>
Babylonian method.
</pre>
