N,C=map(int,input().split())
service = [list(map(int,input().split()))for i in range(N)]

def defaultCost(a,b,c): return (b-a+1)*c

day = set()
cost = dict()

for a,b,c in service:
    day.add(a)
    day.add(b+1)

    if a in cost: cost[a] += c
    else: cost[a] = c
    
    if b+1 in cost: cost[b+1] -=c
    else: cost[b+1] =  -c

day = sorted(list(day))
r = [0]*(len(day)+1)
m = day[0]-1
ans = 0

for i in range(1,len(day)+1):
    r[i] = r[i-1] + cost[day[i-1]]

for i in range(len(day)):
    ans += min(C*(day[i]-m),(day[i]-m)*r[i])
    m = day[i]

print(ans)