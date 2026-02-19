n = int(input())
multi = 1
last = 0
for i in range(1, 12):
    multi*=i
    if(multi>=n):
        last = i
        break
print(last)