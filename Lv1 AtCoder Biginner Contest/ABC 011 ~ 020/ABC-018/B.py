S,N=list(input()),int(input())
for i in range(N):
    l,r=map(int,input().split())
    s=S[l-1:r]
    s.reverse()
    S=S[:l-1]+s+S[r:]
print(''.join(S))