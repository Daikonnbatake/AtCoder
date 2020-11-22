S=input()
up,low,o=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),list("abcdefghijklmnopqrstuvwxyz"),""
for i in range(len(S)):
    if i == 0 and S[i] in low:
        o = o + up[low.index(S[i])]
    elif i != 0 and S[i] in up:
        o = o + low[up.index(S[i])]
    else:
        o = o+S[i]
print(o)