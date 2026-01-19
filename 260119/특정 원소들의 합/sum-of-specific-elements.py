sum = 0
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(i+1):
        sum += tmp[j]

print(sum)