lst = [int(input()) for _ in range(10)]

cntt=0
cntf=0

for i in lst:
    if i%3==0:
        cntt+=1
    if i%5==0:
        cntf+=1

print(cntt, cntf)