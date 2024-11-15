import math
x,y=map(int,input().split())
z=y/100
z=int(math.ceil(z))
print(z-x)
