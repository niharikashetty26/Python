def matrix_elements(matrix):
    for row in matrix:
        for element in row:
            yield element

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for element in matrix_elements(matrix):
    print(element)
