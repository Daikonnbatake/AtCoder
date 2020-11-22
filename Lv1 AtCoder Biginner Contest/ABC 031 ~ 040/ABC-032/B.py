s,k=input(),int(input())
a=set()
if len(s)<k:print(0)
else:
    for i in range(len(s)-k+1):a.add(s[i:i+k])
    print(len(a))