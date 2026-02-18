a, b = map(int, input().split())
multi=1
for _ in range(b):
    multi*=a
print(multi)