sum_list = []

for _ in range(4):
    tmp = map(int, input().split())
    sum = 0
    for i in tmp:
        sum += i
    sum_list.append(sum)

for i in sum_list:
    print(i)