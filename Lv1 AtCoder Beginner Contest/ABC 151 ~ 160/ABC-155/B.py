N,A=int(input()),list(map(int,input().split()))
for i in A:
    if i%2==0:
        if i%3==0 or i%5==0:
            pass
        else:
            print("DENIED")
            exit()
    else:
        pass
print("APPROVED")