a, b, c = map(int, input().split())
state=0
for i in range(a, b+1):
    if i>=c and i%c==0:
        state=1
        break

if state==0:
    print('YES')
else:
    print('NO')