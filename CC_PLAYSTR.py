# cook your dish here
for _ in range(int(input())):
    l=int(input())
    x=input()
    y=input()
    
    cx=cy=0
    
    for i in range(l):
        if x[i]=='1':
            cx+=1
        if y[i]=='1':
            cy+=1
    if cx==cy:
        print("YES")
    else:
        print("NO")
