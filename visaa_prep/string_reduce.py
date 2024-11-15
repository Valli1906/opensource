a=str(input())
b=[]
count=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        count+=1
    else:
        b.append(a[i-1]+str(count))
        count=1
b.append(a[-1]+str(count))

print(''.join(b))
            
