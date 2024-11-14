x=int(input())
sum1=0
while(x!=0):
    temp=x%10
    sum1=sum1+temp
    x=x//10
if(sum1 % 2)==0:
    print("Vignesh")
else:
    print("Charan")
