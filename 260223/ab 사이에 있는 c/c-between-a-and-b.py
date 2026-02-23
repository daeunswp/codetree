a, b, c = map(int, input().split())
temp=1
while(True):
    if a<=c<=b:
        print('YES')
        break
    temp+=1
    c*=temp
    if c>b:
        print('NO')
        break