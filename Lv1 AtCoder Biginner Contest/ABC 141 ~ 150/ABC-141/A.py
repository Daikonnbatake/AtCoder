S=input()
l=['Sunny','Cloudy','Rainy']
print(l[l.index(S)+1] if S!= 'Rainy' else 'Sunny')