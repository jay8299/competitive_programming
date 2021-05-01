#https://www.codechef.com/LTIME95C/problems/EQUINOX


t=int(input())
strarr=['E','Q','U','I','N','O','X']
while t>0:
    t-=1
    sar=0
    anu=0
    n,a,b=map(int,input().split())
    while n>0:
        n-=1
        s=input()
        if s[0] in strarr:
            sar+=a
        else:
            anu+=b
    if(sar>anu):
        print("SARTHAK")
    elif(anu>sar):
        print("ANURADHA")
    elif anu==sar:
        print("DRAW")