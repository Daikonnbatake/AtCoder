def binary_search(array, item):
   head = 0
   tail = len(array) - 1
   while tail>=item and head<item:
       center = (head + tail) // 2
       if array[center] == item:return center
       elif array[center] < item:head = center + 1
       else:tail = center - 1
   return None

N,K=map(int,input().split())
mod=10**9+7
for i in range(N):
    v=list(map(int,input().split()))
    if 0<i:print(binary_search(v,m[0]))
    m=v