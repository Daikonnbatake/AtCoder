W = input()

out = ""
L = ["a","i","u","e","o"]

for i in range(len(W)):
    if not W[i] in L:
        out = out + W[i]

print(out)