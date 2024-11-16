n=int(input())
arr=list(map(int,input().split()))
a=arr[1:]
a.append(arr[0])
for i in range(0,n):
    print(a[i],end=" ")
