#difficulty 635
for _ in range(int(input())):
    x,y=map(int,input().split())
    mi=min(x,y)
    ma=max(x,y)
    r=-1
    while r!=0:
        r=ma%mi
        ma=mi
        mi=r
        #ma stores the hcf
    div1=x//ma
    div2=y//ma
    print(ma,ma*div1*div2)
