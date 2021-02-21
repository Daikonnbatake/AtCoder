N,Card,i,O = int(input()),[1,2,3,4,5,6],0,""
N = N%60
while i < N:
    mod1,mod2 = i%5,i%5+1
    Card[mod1],Card[mod2]=Card[mod2],Card[mod1]
    i+=1
for i in range(6):
    O = O+str(Card[i])
print(O+"\n")