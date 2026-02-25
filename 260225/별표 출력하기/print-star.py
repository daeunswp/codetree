n=int(input())
for i in range(1, n):
    for _ in range(i):
        print('*', end=" ")
    print()
for j in range(n, 0, -1):
    for _ in range(j):
        print('*', end=" ")
    print()