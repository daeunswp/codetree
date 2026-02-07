a, b, c = map(int, input().split())

first = 0
second = 0

if a<=b<=c:
    first = 1

if a==b==c:
    second = 1

print(first, second)

