n,a,f1,f2,ans=int(input()),list(map(int,input().split(" "))),["y","n"]*5,["y","n","y"]*3,0
for i in a:
    j=i
    while not (f1[j-1]==f2[j-1] and f1[j-1]=="y"):
        j-=1
    ans+=i-j
print(ans)