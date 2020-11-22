S=input()
start,end=0,4
count=0

if(len(S) < 4):
    print(0)
else:
    while True:
        for i in range(len(S)-3-start):
            if int(S[start:end])%2019 == 0:
                count += 1
            end += 1
        start += 1
        end = start+4
        if start == len(S)-3:
            break
    print(count)