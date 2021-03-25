import math as m
D,G=map(int,input().split())
p,c=[0]*D,[0]*D
for i in range(D):p[i],c[i]=map(int,input().split())
ans=10**9

for i in range(1,1<<D):
    a,b=[],[]
    score=0
    problems=0
    for j in range(D):
        if i>>j&1:a.insert(0,[p[j],c[j],(j+1)*100])
        elif b==[]:b=[p[j],c[j],(j+1)*100]
    for P,C,S in a:
        if score+(P*S)<=G:
            score+=(P*S)+C
            problems+=P
        if G<=score:break
    if score<G and b!=[]:
        k=0
        while k<b[0] and score<G:
            score += b[2]
            problems+=1
            k+=1
    elif score<G:problems=10*9

    ans=min(ans,problems)
print(ans)