# https://www.codechef.com/MAY21C/problems/LKDNGOLF


def willFallInHole(n,x,k):
    if x%k==0:
        return "YES"
    elif ((n+1)-x)%k==0:
        return "YES"
    else:
        return "NO"

t=int(input())

while t>0:
    t-=1
    n,x,k=map(int,input().split())
    print(willFallInHole(n,x,k))