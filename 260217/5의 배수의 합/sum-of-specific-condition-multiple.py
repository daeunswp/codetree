a, b = map(int, input().split())
max=0
min=0
if a>b:
    max=a
    min=b
else:
    max=b
    min=a

sum=0
for i in range(min, max+1):
    if i%5==0:
        sum+=i
print(sum)