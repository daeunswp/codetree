a, b = map(int, input().split())

less=0
equal=0

if (a<b):
    less = 1
if (a==b):
    equal = 1

print(less, equal)
