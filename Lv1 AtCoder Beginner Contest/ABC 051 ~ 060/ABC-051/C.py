sx,sy,tx,ty=map(int,input().split())
ans=''
ans+='U'*(ty-sy)
ans+='R'*(tx-sx)
ans+='D'*(ty-sy)
ans+='L'*(tx-sx+1)
ans+='U'*(ty-sy+1)
ans+='R'*(tx-sx+1)
ans+='DR'
ans+='D'*(ty-sy+1)
ans+='L'*(tx-sx+1)
ans+='U'
print(ans)