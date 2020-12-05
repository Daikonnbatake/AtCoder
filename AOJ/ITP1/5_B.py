while True:
    H,W=map(int,input().split())
    if H==0 and W==0:
        break
    a=['#'+'.'*(W-2)+'#']*(H-2)
    a.insert(0,'#'*W);a.extend(['#'*W,''])
    for i in a:print(i)