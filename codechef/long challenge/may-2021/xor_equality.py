# https://www.codechef.com/MAY21C/problems/XOREQUAL


# cook your dish here
def binaryExponentiation(n):
    m=10**9+7
    a=1
    b=2
    while(n>0):
        if(n%2==1):
           a=(a*b)%m
        b=(b**2)%m
        n=n>>1
    return a
    
t=int(input())
while t>0:
    t-=1
    n=int(input())
    print(binaryExponentiation(n-1))