# https://www.codechef.com/MAY21C/problems/TCTCTOE


# cook your dish here
def validateTTT(a):
    countX=0
    countO=0
    winX=0
    winO=0
    count_=0
    
    #counting
    for i in range(3):
        for j in range(3):
            if a[i][j]=="X":
                countX+=1
            elif a[i][j]=="O":
                countO+=1
            elif a[i][j]=="_":
                count_+=1
    #check rows
    for i in range(3):
        if a[i][0]==a[i][1]==a[i][2]:
            if a[i][0]=="X":
                winX+=1
            elif a[i][0]=="O":
                winO+=1
    #check coloumns
    for i in range(3):
        if a[0][i]== a[1][i]==a[2][i]:
            if a[0][i]=="X":
                winX+=1
            elif a[0][i]=="O":
                winO+=1
    #check Diagonals
    if a[0][0]== a[1][1]==a[2][2]:
        if a[1][1]=="X":
            winX+=1
        elif a[1][1]=="O":
            winO+=1
            
    if a[0][2]== a[1][1]==a[2][0]:
        if a[1][1]=="X":
            winX+=1
        elif a[1][1]=="O":
            winO+=1
            
    #print(winX,winO,countX,countO,count_)
    if countO>countX or countX-countO>1:
        return 3
    elif countX>countO and (winX==1 and winO==0):
        return 1
    elif countX==countO and winO==1 and winX==0:
        return 1
    elif count_==0 and ((winX==0 and winO==0) or winX==2):
        return 1
    elif count_>0 and winX==0 and winO==0:
        return 2
    else:
        return 3
        
t=int(input())
while t>0:
    t-=1
    arr=[]
    for i in range(3):
        arr.append(list(input()))
    #print(arr)
    print(validateTTT(arr))