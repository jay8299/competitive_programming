# https://www.codechef.com/MAY21C/problems/SOLBLTY

# cook your dish here
t=int(input())
while t>0:
    t-=1
    x,a,b=map(int,input().split())
    amt=(100-x)*b+a
    print(amt*10)