n=int(input())
temp=11
for i in range(n):
    for j in range(temp, temp+2*n, 2):
        print(j, end=" ")
    temp+=2
    print()
