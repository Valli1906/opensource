n=int(input())
a=[]
for i in range(n):
    row=list(map(int,input().split()))
    a.append(row)
b=[[a[j][i] for j in range(n)] for i in range(n)]
for r in b:
    print(" ".join(map(str,r)))
