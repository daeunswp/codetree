lst = [int(input()) for _ in range(10)]
cnt=0
sum=0
for i in lst:
    if 0<=i<=200:
        cnt+=1
        sum+=i
print(f"{sum} {sum/cnt:.1f}")