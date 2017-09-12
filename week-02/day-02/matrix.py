
# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

def matrix2d(x, y):
    matrix = []
    for i in range(x):
        row = []
        for j in range(y):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append (row)
    return matrix

for row in matrix2d(4, 4):
    for elem in row:
        print(elem, end=' ')     
    print()