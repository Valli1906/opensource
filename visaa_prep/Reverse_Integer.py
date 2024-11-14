x=int(input())
sum=0
while(x!=0):
    temp=x%10
    sum=sum*10+temp
    x=x//10
if sum>2**31-1:
    print("0")
else:
    print(sum)
    
