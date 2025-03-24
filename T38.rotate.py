def rotate_matrix(matrix):
    # Step 1: Transpose the matrix (swap rows and columns)
    n = len(matrix)
    
    # Transpose in place (swap element at [i][j] with [j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix(matrix)
print("Rotated Matrix:")
for row in rotated_matrix:
    print(row)