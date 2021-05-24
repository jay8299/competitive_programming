# https://www.codechef.com/COOK129C/problems/VACCINE3

t=int(input())

while t>0:
    t-=1
    g,p,*x=list(map(int,input().split()))
    r=sum(x[g:])
    rem=r%p
    mindays=r//p
    #print(mindays,g,"uyg")
    net=x[g-1]+rem
    #print(net,p,"ve")
    count=net//p
    if net%p>0:
        count+=1
    #print(net,count,"jh")
    print(mindays+1,mindays+count)
    