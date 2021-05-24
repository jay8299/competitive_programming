#https://www.codechef.com/COOK129C/problems/MARARUN

x=10
y=21
z=42
t=int(input())
while t>0:
    t-=1
    D,d,a,b,c=map(int,input().split())
    #print(d*D,"d")
    if d*D<x:
        print(0)
    elif x<=d*D<y:
        print(a)
    elif y<=d*D<z:
        print(b)
    elif d*D>=z:
        print(c)