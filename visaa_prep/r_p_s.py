v,c=map(str,input().split())
r='R'
p='P'
s='S'
if((v==p and c==r) or (v==s and c==p) or (v==r and c==s)):
    print("Vignesh")
elif((c==p and v==r) or (c==s and v==p) or (c==r and v==s)):
    print("Charan")
else:
    print("NULL")
