N,A,B=map(int,input().split());ans=0
for i in range(N):s,d=input().split();d=int(d);ans+=(max(-B,-d) if d>=A else -A) if s=='West' else (min(B,d)if d>=A else A)
print(0 if ans==0 else ('West '+str(ans*-1) if ans<0 else 'East '+str(ans)))