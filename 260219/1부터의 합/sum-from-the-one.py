n = int(input())
sum = 0
last = 0
for i in range(1, 101):
    sum+=i
    if(sum>=n):
        last = i
        break
    
print(last)