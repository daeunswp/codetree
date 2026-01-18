n = int(input())

store=1

for i in range(n):
    for j in range(i+1):
        print(store, end=" ")
        store+=1
    print()
