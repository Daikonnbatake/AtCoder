N,K=map(int,input().split())
a=sorted(list(map(int,input().split())))
box = [-1]*K
before = -1
point = 0
max_range = 0

for i in a:
    if i==before: point=min(point+1,K-1)
    else: point = 0
    before = i
    if i-1==box[point]: box[point] = i
    max_range = max(max_range, point)

print(sum(box[0:max_range+1])+max_range+1 if 0<max_range else box[0]+1)