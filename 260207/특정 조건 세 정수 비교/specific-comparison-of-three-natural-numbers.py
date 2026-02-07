a, b, c = map(int, input().split())

first = 0
second = 0
least = 0

if a<=b:
    if a<=c:
        least = a
    else:
        least = c
else:
    if b<=c:
        least = b
    else:
        least = c

if least == a:
    first = 1

if a==b==c:
    second = 1

print(first, second)

