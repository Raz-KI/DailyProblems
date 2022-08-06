# cook your dish here
for _ in range(int(input())):
    x=input()
    flag=0
    ans='NO'
    for i in x:
        if i=='1' and flag==0:
            flag+=1
        if i=='0' and flag==1:
            flag+=1
        if i=='1' and flag==2:
            flag+=1
    if flag==1 or flag==2:
        ans='YES'
    
    print(ans)
