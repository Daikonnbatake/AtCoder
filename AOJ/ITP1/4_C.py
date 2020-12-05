while True:
    a,o,b=input().split()
    if o=='?':break
    a=int(a);b=int(b)
    print({'+':a+b,'-':a-b,'*':a*b,'/':(a//b if a and b else 0)}[o])