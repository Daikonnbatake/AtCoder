N,S,s=int(input()),input(),'b'
for i in range(N):
    if s==S:print(i);exit()
    s=('c'+s+'a'if i%3==1 else'b'+s+'b')if i%3 else'a'+s+'c'
print(-1)