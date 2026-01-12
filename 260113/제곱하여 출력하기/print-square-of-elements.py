n = int(input())
num_list = list(map(int, input().split()))
double_list = []

for i in range(n):
    double_list.append(num_list[i]*num_list[i])

for i in range(n):
    print(double_list[i], end=" ")