#https://www.codechef.com/LTIME95C/problems/BENCHP



from collections import defaultdict
t=int(input())
while t>0:
    t-=1
    n,w,wr=map(int,input().split())
    warr=list(map(int,input().split()))
    if wr>=w:
        print("YES")
    else:
        wnet=w-wr
        wdict=defaultdict(int)
        for i in warr:
            wdict[i]+=1
        for i in warr:
            if(wdict[i]>=2):
                #for odd
                if wdict[i]%2:
                    wnet-=(wdict[i]-1)*i
                #for even
                elif not wdict[i]%2:
                    wnet-=wdict[i]*i
                wdict[i]=0
            if wnet<=0:
                print("YES")
                break
        else:
            print("NO")