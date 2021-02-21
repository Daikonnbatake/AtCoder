N=int(input())
a=list(map(int,input().split()))
a.sort(key=int,reverse=True)
A,B=[],[]
for i in a:
    if len(A)==len(B): A.append(i)
    else : B.append(i)
print(sum(A)-sum(B))