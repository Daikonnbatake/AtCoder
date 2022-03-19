import itertools as itr

N=int(input())
P=tuple(map(int,input().split()))
Q=tuple(map(int,input().split()))

p = list(itr.permutations([i+1 for i in range(N)]))

print(abs(p.index(P) - p.index(Q)))