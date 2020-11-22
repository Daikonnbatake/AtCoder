N=int(input())
ac,wa,tle,re=0,0,0,0
for i in range(N):
    s=input()
    if s=='AC': ac+=1
    if s=='WA': wa+=1
    if s=='TLE': tle+=1
    if s=='RE': re+=1
print('AC x '+str(ac))
print('WA x '+str(wa))
print('TLE x '+str(tle))
print('RE x '+str(re))