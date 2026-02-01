# Function to get 3x3 matrix input from user
def get_matrix(name):
    print(f"Enter elements for 3x3 Matrix {name} (row-wise):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return matrix

# 1. Get input for Matrix A and B
A = get_matrix("A")
B = get_matrix("B")

# 2. Initialize result matrix with zeros
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 3. Perform Matrix Multiplication (A * B)
# Iterate through rows of A
for i in range(3):
    # Iterate through columns of B
    for j in range(3):
        # Iterate through rows of B
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

# 4. Print the result
print("\nResulting 3x3 Matrix (A * B):")
for row in result:
    print(row)
