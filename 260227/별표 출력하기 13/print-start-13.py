n=int(input())
cnt=n
for i in range(1, 2*n+1):
    if i%2==0:
        for _ in range(i//2):
            print('*', end=' ')
    else:
        for _ in range(cnt):
            print('*', end=' ')
        cnt-=1
    print()
