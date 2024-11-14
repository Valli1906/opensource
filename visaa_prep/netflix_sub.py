x,y,z,a=map(int,input().split())
if(x+y>=a or x+z>=a or z+y>=a ):
    print("YES")
else:
    print("NO")
