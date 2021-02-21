K,X=map(int,input().split())
ans=[]
for i in range((K*-1)+1,K): ans.append(X+i)
ans.sort(key=int)
print(' '.join(str(i)for i in ans))