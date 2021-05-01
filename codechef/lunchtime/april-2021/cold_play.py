#https://www.codechef.com/LTIME95C/problems/SLOOP


t=int(input())
while t>0:
    t-=1
    m,s=map(int,input().split())
    print(m//s)