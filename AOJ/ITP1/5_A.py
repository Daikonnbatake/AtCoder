while True:
    H,W=map(int,input().split())
    if H==0 and W==0:break
    for i in ['#'*W]*H:print(i)
    print('')