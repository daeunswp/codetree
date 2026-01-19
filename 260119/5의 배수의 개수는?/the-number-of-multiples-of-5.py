sum = 0

for _ in range(4):
    tmp = map(int, input().split())
    for i in tmp:
        if(i%5==0):
            sum+=1

print(sum)