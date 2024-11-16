n=int(input())
att=list(map(int,input().split()))
count=0
num=[]
for i in range(0,n):
    if att[i]==0:
        count+=1
    if att[i]==1:
        num.append(count)
        count=0
print(max(num))
