n=int(input())

for i in range(1, n+1):
    for _ in range(0, i-1):
        print(end="  ")
    for _ in range(n*2 - 2*i + 1):
        print('*', end=" ")
    print()