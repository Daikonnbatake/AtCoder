V,T,S,D=map(int,input().split())
print('No' if (V*T <= D and D <= V*S) else 'Yes')