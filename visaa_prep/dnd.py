n,m=map(int,input().split())
num1=0
num2=0
x=list(map(int,input().split()))
for i in range(0,n):
    if(x[i]%m==0):
        num1=num1+x[i]
    else:
        num2=num2+x[i]
print(num1-num2)
