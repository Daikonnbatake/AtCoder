B,C=map(int,input().split())

# C-1円で作れる絶対値の最大値を求める
if B-((C-1)//2)<0: a=max(B,abs(B-((C-1)//2)))
else: a=(C-1)//2

# 愚直に 負の方向にのみお金を使った場合の絶対値の最大値を求める
b = 1 if a < C//2 else 0
a+= 1 if B else 0
c = 0 if B else 1

print(a*2+b+c)