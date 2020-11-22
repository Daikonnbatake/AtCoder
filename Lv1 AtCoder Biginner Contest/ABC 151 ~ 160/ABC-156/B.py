N,K=map(int,input().split())
counter=0
mem=1
while N >= mem:
    mem=K*mem
    counter+=1
print(counter)