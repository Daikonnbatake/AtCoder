A,B,K=map(int,input().split())
l=[]
for i in range(min(A,B)):
    if A%(i+1)==0 and B%(i+1)==0: 
        l.append(i+1)
print(l[-K])