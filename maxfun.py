try:
    T=int(input())
    for i in range(T):
        a=int(input())
        li=list(map(int,input().split(" ")))
        li.sort()
        x=li[0]
        y=li[len(li)//2]
        z=li[-1]
        print(abs(x-y)+abs(x-z)+abs(y-z))
    
except Exception:
    pass
