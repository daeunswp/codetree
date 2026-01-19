n = int(input())
cnt = 0
for i in range(n):
    for j in range(n):
        if(cnt%2==0):
            print(j+1, end="")
        else:
            print(n-j, end="")
    print()
    cnt+=1