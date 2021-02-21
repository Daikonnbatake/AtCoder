S=input()
A=S[0:int((len(S)-1)/2)]
B=S[int((len(S)+3)/2):-1]
def kaibun(s):
    a,b="",""
    for i in range(len(s)):
        a = a+s[i]
        b = s[i]+b
    return a==b
print('Yes' if (kaibun(S) and kaibun(A) and kaibun(B)) else 'No')