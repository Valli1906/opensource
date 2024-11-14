t=int(input())
for _ in range(0,t):
    n,m=map(int,input().split())
    temp=n-m
    if(temp>=0):
        print(temp)
    else:
        print("0")
