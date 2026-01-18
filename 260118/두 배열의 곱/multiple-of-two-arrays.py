a_matrix = []
b_matrix = []

for _ in range(3):
    a_row = list(map(int, input().split()))
    a_matrix.append(a_row)

input()

for _ in range(3):
    b_row = list(map(int, input().split()))
    b_matrix.append(b_row)

for i in range(3):
    for j in range(3):
        print(a_matrix[i][j]*b_matrix[i][j], end=" ")
    print()