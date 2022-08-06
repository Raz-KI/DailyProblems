#1999
for _ in range(int(input())):
    x=int(input())
    l=list(map(int,input().split()))
    for i in l:
        if i==0:
            l.remove(0)
    l=set(l)
    if sum(l)==0:
        print(0)
    else:
        print(len(l))
