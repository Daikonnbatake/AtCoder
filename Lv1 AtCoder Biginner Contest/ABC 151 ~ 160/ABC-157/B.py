A=[]
m=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    A.append(list(map(int,input().split())))
N=int(input())
def add(n):
    for i in range(3):
        if n in A[i]:
            m[i][A[i].index(n)]=1

def check():
    for i in m:
        if i == [1,1,1]:
            return True
    for i in range(3):
        if m[0][i]+m[1][i]+m[2][i]==3:
            return True
    if m[0][0]+m[1][1]+m[2][2]==3:
        return True
    if m[2][0]+m[1][1]+m[0][2]==3:
        return True
    return False

for i in range(N):
    inp=int(input())
    add(inp)
    if check():
        print("Yes")
        exit()
print("No")