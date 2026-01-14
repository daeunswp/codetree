n= int(input())
num_list = input().split()
even_list = []

for i in range(n):
    if(int(num_list[i])%2==0):
        even_list.append(int(num_list[i]))

for i in range(len(even_list)-1, -1, -1):
    print(even_list[i], end=" ")


