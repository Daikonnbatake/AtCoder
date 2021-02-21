K=int(input())
a=[1,2,3,4,5,6,7,8,9]

while True:
    if K<len(a):
        print(a[K-1])
        exit()
    K-=len(a)
    old=[]
    old,a=a,old
    for i in old:
        for j in range(-1,2):
            d=i%10+j
            if d<0 or 9<d:continue
            a.append(i*10+d)