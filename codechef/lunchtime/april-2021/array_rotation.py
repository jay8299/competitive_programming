#https://www.codechef.com/LTIME95C/problems/ARRROT

mod=(10**9)+7
n=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
q=int(input())
a=list(input().split())
l=len(a)

for i in a:
    s=s*2
    print(s%(mod))