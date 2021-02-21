S=input();l=[0]*6
for i in range(len(S)):l[ord(S[i])-65]+=1
print(' '.join(map(str,l)))