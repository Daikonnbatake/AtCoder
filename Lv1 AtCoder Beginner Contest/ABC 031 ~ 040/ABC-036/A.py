A,B=map(int,input().split())
print(int(B/A) if B%A==0 else int(B/A)+1)