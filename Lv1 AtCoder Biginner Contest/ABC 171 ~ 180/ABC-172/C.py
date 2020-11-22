N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.reverse();B.reverse()
ans=0
while -1<K:
    if len(A)+len(B)==0: ans+=1;break
    if 0==len(A): K-=B.pop()
    elif 0==len(B): K-=A.pop()
    else:
        if A[0]<B[0]: K-=A.pop()
        else: K-=B.pop()
    ans+=1
print(ans-1)