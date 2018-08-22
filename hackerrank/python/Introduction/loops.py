if __name__ == '__main__':
    n = int(input())
    print(*map(lambda x: x*x,range(n)), sep='\n')