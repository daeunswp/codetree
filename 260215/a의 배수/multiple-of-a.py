n, a = map(int, input().split())
temp = 1
while temp<=n:
    if temp%a==0:
        print(1)
    else:
        print(0)
    temp+=1