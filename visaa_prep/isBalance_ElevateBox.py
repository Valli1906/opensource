n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    lw= sum(a[:i]) if i>0 else 0
    rw=sum(a[i+1:]) if i<n-1 else 0
    temp=abs(lw-rw)
    b.append(temp)
for i in range(n):
    print(b[i],end=" ")
