lst = [int(input()) for _ in range(5)]
state=1
for i in lst:
    if i%3==0:
        continue
    else:
        state=0
        break
print(state)