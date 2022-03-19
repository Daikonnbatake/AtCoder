N=int(input())
A=list(map(int,input().split()))
ans=0

s=set([A[-1]])
d={A[-1]:1}

for i in range(1,N):
    j=N-i-1
    if A[j] in s:
        ans+= i-d[A[j]]
        d[A[j]]+=1
    else:
        d[A[j]]=1
        ans += i
    s.add(A[j])

print(ans)