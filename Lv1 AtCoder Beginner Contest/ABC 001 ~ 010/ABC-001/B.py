m = int(input())

if m < 100: a = '00'
elif 100 <= m <= 5000: a = m//100 if (9<m//100) else '0'+str(m//100)
elif 6000 <= m <= 30000: a = m//1000 + 50
elif 35000 <= m <= 70000: a = (m//1000-30)//5+80
else: a = 89

print(a)