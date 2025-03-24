def isValidSudoku(board):
    # Use sets to track seen numbers in rows, columns, and 3x3 subgrids
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue  # Skip empty cells
            
            # Check the row
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            # Check the column
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            # Check the 3x3 subgrid
            subgrid_index = (i // 3) * 3 + (j // 3)  # Calculate the subgrid index
            if num in subgrids[subgrid_index]:
                return False
            subgrids[subgrid_index].add(num)
    
    return True

# Example usage:
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '8', '.', '.', '.', '3', '2'],
    ['4', '.', '6', '8', '.', '3', '.', '.', '.'],
    ['7', '.', '.', '.', '2', '.', '6', '.', '9'],
    ['3', '.', '3', '.', '.', '.', '.', '5', '.'],
    ['2', '8', '.', '4', '1', '.', '.', '7', '6'],
    ['1', '2', '3', '.', '8', '9', '.', '.', '.']
]

print(isValidSudoku(board))  # Output: False (invalid board due to duplicate '8' in subgrid)
