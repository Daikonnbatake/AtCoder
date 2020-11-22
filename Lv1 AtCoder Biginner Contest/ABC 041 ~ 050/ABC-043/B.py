s=input()
e=[]
for i in range(len(s)):
    if s[i]=="1":
        e.append("1")
    elif s[i]=="0":
        e.append("0")
    else:
        if not len(e)==0:
            e.pop(-1)
o=""
for i in e:
    o=o+i
print(o)