c=[]
for i in list(input()):
    if not i in c: c.append(i)
    if len(c)>1:
        print('DIFFERENT')
        exit()
print('SAME')