def print_matrix(M):
    for row in range(len(M)):
        for col in range(len(M[0])):
            print(M[row][col]),
        print("")

def matrix_dimension(M):
    return str(len(M)) + " x " + str(len(M[0]))

M = [[5, 6, 7], [0, 3, 5]]
print_matrix(M)
print("\nThe dimensions of the matrix are: " + matrix_dimension(M))
