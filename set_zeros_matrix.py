# Time: O(m.n), Space(m+n): better: O(1)
# an array noting column and row changes
# then convert respective rows to zeros then columns to zero
# better: start top to right. Set row column changes inplace

def setZeros(matrix):
    ROWS, COLS = len(matrix),  len(matrix[0])
    rowZero = False

    #see which rows/cols need to be zero
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r>0:
                    matrix[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0

    return matrix

matrix_array = [[1,0,0], [1,1,1], [1,1,1]]
print(setZeros(matrix_array))


