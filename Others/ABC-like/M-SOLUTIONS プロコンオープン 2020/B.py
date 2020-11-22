R,G,B=map(int,input().split())
K=int(input())
while 0<K:
    if G<=R:G+=G
    elif B<=G:B+=B
    else:break
    K-=1
print('Yes'if(R<G and G<B)else'No')