n=int(input())
arr=list(map(int,input().split()))
s=int(input())
flag=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            continue
        else:
            if arr[i]+arr[j]:
                flag=1
                break;
    if flag==1:
        break;
if(flag==0):
    print("false")
else:
    print("true")
            
            
