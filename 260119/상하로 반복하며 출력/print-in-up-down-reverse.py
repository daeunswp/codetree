n = int(input())

matrix = []
cnt = 1

for i in range(n):
    for j in range(n):
        if(j%2==0):
            print(cnt, end="")
        else:
            print(n+1-cnt, end="")
    cnt+=1
    print()