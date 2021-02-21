a,b=int(input()),int(input())
c=[abs(a-b),abs(b-a),abs((a-10)-b),abs((b-10)-a)]
c.sort()
print(c[0])