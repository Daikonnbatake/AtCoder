A,B=input().split()
B=B[0]+B[2:]
i=len(B)-1
ans=str(int(A)*int(B))
print(ans[:-i] if ans[:-i]!='' else 0)