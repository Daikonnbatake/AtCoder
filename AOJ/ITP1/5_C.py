while True:
    H,W=map(int,input().split())
    if H==0 and W==0:break
    o=[''.join([['#','.'][i%2] for i in range(W)]),''.join([['.','#'][i%2] for i in range(W)])]
    for i in range(H):print(o[i%2])
    print('')