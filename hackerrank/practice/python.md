# Practice > Python
## Introduction
### Loops
```py
if __name__ == '__main__':
    n = int(input())
    print(*map(lambda x: x*x,range(n)), sep='\n')
```
### print function
```py
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1), sep='',end='')
```
## Basic Data Types
### List Comprehensions
```py
if __name__ == '__main__':
    x,y,z,n = int(input()),int(input()),int(input()),int(input())
    r=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(r)
```
