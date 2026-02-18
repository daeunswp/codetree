n = int(input())
lst = [int(input()) for _ in range(n)]
sum=0
for i in lst:
    sum+=i

print(f"{sum} {sum/n:.1f}")