N,D,K=map(int,input().split())
lr = [list(map(int,input().split()))for i in range(D)]
st = [list(map(int,input().split()))for i in range(K)]

ans=[0]*K

for i in range(D):
    l,r=lr[i]
    # print(i+1,' 日目 ----')
    for j in range(K):
        s,t=st[j]
        if l<=s and s<=r and ans[j]==0:
            if s<t:
                st[j][0]=min(r,t)
            if s>t:
                st[j][0]=max(l,t)
            # print('民族',j+1,s,'→',st[j][0])

        if st[j][0]==t and ans[j]==0: ans[j] = i+1

for i in ans:print(i)