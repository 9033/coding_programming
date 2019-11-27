# 알고리즘별 코드
## Longest Increasing Subsequence
```py
def CeilIndex(A, l, r, key): # 내림차순일때 사용하는 binary search.
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 

def LIS(l):
    mm=[0]*len(l)
    pos=[0]*len(l)
    end=0
    maxend=0
    lenmm=0
    for j in range(len(l)):
        if end>0:
            lenmm=max(lenmm,end)
            r=CeilIndex(mm,-1,lenmm-1,l[j])
            if mm[r]>=l[j]:
                mm[r]=l[j]        
                pos[j]=r
                end=r+1
            else:
                mm[r+1]=l[j]
                pos[j]=r+1
                end=r+2
            maxend=max(maxend,end)
        else:
            mm[end]=l[j]
            pos[j]=end
            end+=1
    maxend=max(maxend,end)

    s=[]
    t=maxend-1
    for i in range(len(pos)-1,-1,-1):
        if t==pos[i]:
            s.append(l[i])
            t-=1

    return maxend, reversed(s)
```
## 최소신장트리
### Prim
```py
l=None

def findroot(a):
    global l
    _root=a
    while l[_root]!=_root:
        _root=l[_root]
    l[a]=_root#제출결과로 보면 있는게 더 빠름. (Path Compression)
    return _root

def setroot(a,b):#union
    global l#,l_size
    root_a=findroot(a)
    root_b=findroot(b)
    if root_a != root_b:
        l[root_b]=root_a

"""
v = [] # 간선들.
v.append( [노드번호,노드번호,가중치] )
m # 노드의 수.
"""
def mst(v,m):
    global l#,l_size
    l = [i for i in range( m )] # disjoint set
    i=0
    totalLen = 0
    v.sort(key=lambda x:x[2] ) # 가중치로 정렬.

    c = 0 # 선택한 간선의 수.
    while c < m - 1:
        a = v[i][0]
        b = v[i][1]
        if findroot(a) != findroot(b): #집합을 합치는 간선을 선택.
            setroot(a,b)
            totalLen += v[i][2]
            
            c += 1
        i+=1 
    return totalLen
```
## 최단거리
### Dijkstra by heap
```py
import heapq
e = 10 # 노드의 수.
source = 0 # 시작지점
v=[set() for _ in range(e)]#간선 : 희소 그래프일떄 set()을 쓰면 빠름.
dis=[[inf]*e for _ in range(e)]#시작 지점에서 각 지점까지의 거리

inf=9999999

h=[]#heap

heapq.heappush(h,(0,source))

while len(h)>0:
    dmin=inf
    k=-1#최단 거리가 확정 되자 않은 집합 C 중에서 시작 노드에서 가장 가까운 노드
    
    dmin,k=heapq.heappop(h)

    dis[source][k]=dmin
    t=dmin+1
    for node in (  v[k] ):
        if t<dis[source][node]:
            dis[source][node]=t
            heapq.heappush(h, (t,node) )
```
### Floyd Warshall
```py
"""
for문의 변수에 유의.

k가 i부터 j까지의 최단거리 위의 노드라면
i->k k->j의 부분의 최적이 되어야함.

k를 지나가는 모든 노드의 쌍.

가중치가 음이면 안됨.
"""
#Floyd Warshall
for k in range(1,20+1):
    for i in range(1,20+1):
        for j in range(1,20+1):
            if dis[i][j]>dis[i][k]+dis[k][j]:
                dis[i][j]=dis[i][k]+dis[k][j]
                dis[j][i]=dis[i][k]+dis[k][j]
```
# 수학
## n과 n의 약수들을 오름차 순으로 출력
```py
def divisors(n):#n과 n의 약수들을 오름차 순으로 출력
    r1=[]
    r2=[]
    sqrtn=int(n**(1/2))
    a = 1
    while a * a < n:
        if not n % a:
            r1.append(a)
            r2.append(n // a)
        a += 1
        
    if sqrtn * sqrtn == n:
        r1.append(sqrtn)
    r2.reverse()
    return r1+r2

print(divisors(244324**2))
```
## n을 r진법으로 출력
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
## 소수
1 은 소수가 아님.  
### 1부터 N까지 소수를 출력.
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
### 소수인지 판별.
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
# 기타
## Search
### 이분탐색 : 오름차순, Lower bound
```py
#binary search (lower bound : 크거나 같은 값의 위치)
a=0
b=len(y)-1
while a<b:
    m=(a+b)//2
    if y[m]<q:
        a=m+1
    else:
        b=m
        
print(y[a])#크거나 같은 값
```
## Flood-fill
```py
"""
W인 곳의 갯수를 출력.
"""
def sol(img,i,j):# (i,j) : 시작 위치.
    
    rBound=len(img)
    cBound=len(img[0])
    
    v=[[0]*cBound for _ in range(rBound)]#visted, count war eagles
    q=[]#queue
    cnt=0

    q.append([i,j])
    while len(q)>0:
        ii,jj=q.pop(0)
        if ii<0 or jj<0 or rBound<=ii or cBound<=jj:#out of bound
            continue
        if img[ii][jj]=='W' and v[ii][jj]==0:
            v[ii][jj]=1
            cnt+=1
            for qq in [ii-1,ii,ii+1]:
                for ww in [jj-1,jj,jj+1]:
                    q.append([qq,ww])

    return cnt

```
## Disjoint set
```py
n=10
l=[i for i in range(n)]

def findroot(a):#root를 찾는다.
    global l
    _root=a
    while l[_root]!=_root:
        _root=l[_root]
    l[a]=_root#제출결과로 보면 있는게 더 빠름. (Path Compression)
    return _root

def setroot(a,b):#union
    global l
    root_a=findroot(a)
    root_b=findroot(b)
    if root_a != root_b:
        l[root_b] = root_a
        #setsize[root_a] += setsize[root_b]
    
def cntsets():# 집합의 수. (출력은 n개에서 1개)
    global l
    ll=map(findroot,l)
    return len(set(ll))    
```
```cpp
vector <int> l(5001);
vector <int> setsize(5001);
int n=0;//사람수

auto findroot=[&](int i){//root를 찾음.
    int _i=i;
    while (l[_i]!=_i){
        _i=l[_i];
    }
    l[i]=_i;
    return _i;
};

auto setroot=[&](int a,int b){//둘의 root를 일치시킴. b의 루트로 일치시킴. (union)
    a=findroot(a);
    b=findroot(b);
    if(a!=b){
        setsize[b]=setsize[a]+setsize[b];//각 집합의 elements의 수를 union할때마다 계산.
        l[a]=b;
    }
};

auto cntsets=[&](int e){//root가 e의 root인 elements의 갯수.
    int root=findroot(e);
    return setsize[root];
};
```
## 이진 트리 생성
```py
class f:
    def __init__(self, n,LIS):
        self.n=n
        self.l=None
        self.r=None
    
btree=f(l[0],1)
maxn=-9999999
for j in range(1,len(l)):
    node=btree
    new_node=f(l[j],1)
    while True:
        if new_node.n<node.n:
            if node.l:
                node=node.l
            else:
                node.l=new_node
                break
        elif new_node.n>node.n:
            if node.r:                     
                node=node.r                
            else:
                node.r=new_node                
                break
  
```
## 좌표평면상의 점을 완전 그래프로 보고 간선을 생성.
```py
#좌표 -> 완전그래프
"""
각점의 좌표를 입력받음.

각 좌표를 노드로 취급.
모든 노드와 노드 사이에 간선이 있다고 가정. 각 간선이 잇는 노드와 길이를 출력.
"""
import math
def distance(x1,y1,x2,y2):
    return math.sqrt( (x1-x2)**2+(y1-y2)**2 )
    
def pointsToGraph(points,n):    
    distances=[]#각 points 거리.

    for i in range(n-1):
        for j in range(i+1,n):
            d=distance( points[i][0],points[i][1],points[j][0],points[j][1] )
            distances.append([i,j,d])    
    
    return distances
```
## 두 점의 거리
```py
import math
def distance(x1,y1,x2,y2):
    return math.sqrt( (x1-x2)**2+(y1-y2)**2 )
```