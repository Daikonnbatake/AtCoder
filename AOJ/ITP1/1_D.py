S=int(input())
h=S//3600;S-=h*3600
m=S//60;S-=m*60
print(str(h)+':'+str(m)+':'+str(S))