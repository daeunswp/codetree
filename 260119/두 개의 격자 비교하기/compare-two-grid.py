n, m = map(int, input().split())

a_matrix = []
b_matrix = []

for _ in range(n):
    a_row = list(map(int, input().split()))
    a_matrix.append(a_row)

for _ in range(n):
    b_row = list(map(int, input().split()))
    b_matrix.append(b_row)

for i in range(n):
    for j in range(m):
        if (a_matrix[i][j]==b_matrix[i][j]):
            print(0, end = " ")
        else:
            print(1, end = " ")
    print() 

