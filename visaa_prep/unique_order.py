x=int(input())
a=list(map(int,input().split()))
uni=[]
seen=set()
for num in a:
    if num not in seen:
        uni.append(num)
        seen.add(num)
for i in range(0,len(uni)):
    print(uni[i],end=" ")
