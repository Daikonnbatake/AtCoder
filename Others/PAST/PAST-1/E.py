N,Q=map(int,input().split())
f=[['N']*N for i in range(N)]
for i in range(Q):
    # D=メタデータ, A=フォローしたユーザー , B=被フォローユーザー
    inp=list(map(int,input().split()))
    D=inp[0]
    if D == 1: A,B=inp[1]-1,inp[2]-1
    else: A=inp[1]-1
    
    # AがBをフォロー
    if D==1: f[A][B]='Y'

    # Aがフォロワー全員をフォロー
    if D==2:
        for j in range(len(f)):
            if f[j][A]=='Y': f[A][j]='Y'
    
    # Aがフォローしているユーザーがフォローしている全員をフォローする
    if D==3:
        a=''.join(f[A])
        for j in range(len(a)):
            if a[j]=='Y':
                for k in range(len(f[j])):
                    if f[j][k]=='Y' and k!=A:
                        f[A][k]='Y'
for i in f:
    print(''.join(i))