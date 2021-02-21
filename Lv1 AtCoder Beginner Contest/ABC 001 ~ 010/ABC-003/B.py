S = input()
T = input()
at = ["a","t","c","o","d","e","r"]
s=t= ""

def dfrc(s,t):
    if s == t:
        return True
    else:
        if s == "@":
            if t in at:
                return True
            else:
                return False
        elif t == "@":
            if s in at:
                return True
            else:
                return False
        else:
            return False

for i in range(len(S)):
    if dfrc(S[i],T[i]):
        s = s+S[i]
        t = t+T[i]
    else:
        break

if len(s) == len(S):
    print("You can win")
else:
    print("You will lose")
