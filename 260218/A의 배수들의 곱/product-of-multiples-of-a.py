a, b = map(int, input().split())
multi = 1
for i in range(1, b+1):
    if i%a==0:
        multi*=i
print(multi)