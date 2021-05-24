# https://www.codechef.com/MAY21C/problems/MODEQ

def findPairsCount(n,m):
    arr = [ 1 for _ in range(n+1)]
    count=0
    for i in range(2,n+1):
        temp=m%i
        count+=arr[temp]
        for j in range(temp,n+1,i):
            arr[j]+=1
    return count
t=int(input())
while t>0:
    t-=1
    n,m=map(int,input().split())
    print(findPairsCount(n,m))
    