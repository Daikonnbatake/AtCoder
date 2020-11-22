N,s=int(input()),list(input()+'00')

flag = ' '
m = []
for i in range(N):
    if s[i]=='f':
        if flag==' ': flag+='f'
        else:
            if flag!=' ':m.append(flag)
            flag = ' f'
        continue

    if s[i]=='o':
        if flag==' f':
            flag = ' fo'
            m.append(flag)
            flag = ' '
        else:
            if flag!=' ':m.append(flag)
            flag=' o'
        continue
    
    if s[i]=='x':
        if flag==' o':
            flag = ' ox'
            if flag!=' ':m.append(flag)
            flag = ' '
        else:
            if flag!=' ':m.append(flag)
            flag=' x'
        continue
    
    flag = ' '
for i in range(len(m)):
    print(m[i][1:])