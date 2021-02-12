try:
    T=int(input())
    a=1
    for i in range(2,10):
        if T%i==0:
            a=i
    print(a)
except Exception:
    pass
