x,y,z=map(int,input().split())
count=0
u=y
while(u<=z):
    u=u+x
    if(u<=z):
        count=count+1
    else:
        print(count)
