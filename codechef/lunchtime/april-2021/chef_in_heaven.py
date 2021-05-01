#https://www.codechef.com/LTIME95C/problems/CCHEAVEN


def isGood(s,l):
    if s.count('1')>=l/2:
        return True
    else:
        return False


t=int(input().strip())
while t>0:
    t-=1
    l=int(input())
    s=input()
    n=len(s)
    countof1=0
    if isGood(s,l):
        print("YES")
    else:
        for i in range(n):
            if s[i]=='1':
                countof1+=1
                if countof1>=(i+1)/2:
                    print("YES")
                    break
        else:
            print("NO")


