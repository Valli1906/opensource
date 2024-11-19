def sor(n,a):
    for i in range(1,n):
        if a[i-1]>a[i]:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
flag=sor(n,a)
if flag==0:
    print("false")
else:
    print("true")
    
