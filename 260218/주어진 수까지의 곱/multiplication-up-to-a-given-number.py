a, b = map(int, input().split())
multi=1
for i in range(a, b+1):
    multi*=i
print(multi)