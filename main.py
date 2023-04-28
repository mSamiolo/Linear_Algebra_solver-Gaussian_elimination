import numpy as np

def get_echelon_form(A, b):
    # Add a column to the last position to get a wider matrix
    echelon_form = np.c_[A,b]
    return echelon_form

def reduced_echelon_form(master):

    # Get matrix glued matrix from A and b and its shape
    rows, columns = master.shape
    reduced = np.array([])
    next_master = np.array([])

    ## ---------------  Algorithm expalnation  -------------------- ####
    # For column index
    # For all rows
    # Choose the lead equation
        # Use lead scalars to scale the other equations if necessary

    # Staring the loop at the first column
    for col in range (0, columns-1):

        # Array intiialized to contain only the equations that takes part at the row operation
        row_op_matrix = np.array([])
        # At second iteration update the master matrix
        if col > 0:
            master = next_master

        # Initialize the vectors that contain indexes to toggle equations in the system
        under_operation = np.array([])
        no_operation = np.array([])

        # Iteration through al the rows
        for row in range (0, master.shape[0]):
            # Save the index if the equation is/isn`t involved in the algorithm
            if master[row, col] == 0:
                no_operation = np.append(no_operation, row)
            elif master[row, col] != 0:
                under_operation = np.append(under_operation, row)

        # Find the lead equation between the "under operation",
        #  then create a reduced matrix and the next master
        lead_equation_idx = under_operation[0]
        reduced = np.append(reduced,
            master[int(lead_equation_idx)]).reshape(col +1, columns)
        next_master = np.delete(master, int(under_operation[0]), axis=0)

        # the variable is defined hence you can pass into the next iteration
        if under_operation.shape == (1,):
            continue

        # Build the matrix that will be under calculations
        row_op_matrix = master
        list =[]
        list.append(int(lead_equation_idx))
        for i in no_operation:
            list.append(int(i))
        row_op_matrix = np.delete(row_op_matrix, list, axis=0)
        next_master = reduce_row_op_matrix (next_master, reduced[col], col)

        ## Printing statements for debugging purpouse
        # print("Under operarion   ", under_operation, "\nNo operation   ", no_operation)
        # print("\nMaster\n", master, "\nReduced:\n", reduced,)
        # print("\nRow operation matrix:\n" ,row_op_matrix)
        # print("After reduction:\n" ,next_master)

        if col == rows -2:
            reduced = np.append(reduced, next_master.flatten()).reshape(rows, columns)
            return reduced



def reduce_row_op_matrix(row_op_matrix, lead_equation, col):

    # Get the scalar to base the row operation
    lead_scalar = lead_equation[col]
    
    # Inizialize the scalar to reduce order
    scalars_to_reduce_order = np.array([])
    row_op_matrix_reduced = np.array([])

    for row in range (0, row_op_matrix.shape[0]):
        scalars_to_reduce_order = np.append(
            scalars_to_reduce_order, -row_op_matrix[row, col] / lead_scalar)

    # Rewrite the matrix as reduced
    for row in range (0, row_op_matrix.shape[0]):
        row_op_matrix_reduced = np.append(
            row_op_matrix_reduced, row_op_matrix[row] + lead_equation * scalars_to_reduce_order[row])

    return row_op_matrix_reduced.reshape(row_op_matrix.shape)


def solve_reduce_matrix(A):
    n_variables = A.shape[0]
    solution = np.zeros(n_variables)
    columns = A.shape[1]

    # Choose variable
    for i in range(n_variables-1, -1, -1):
        solution[i] = A[i, columns -1]
        for col in range (0, columns-1):
            if col != i:
                solution[i] = solution[i] - A[i, col] * solution[col]
        solution[i] = solution[i] / A[i,i]

    return solution


if __name__ == '__main__':

    A = np.array([[2, 1, -1],
             [-3, -1, 2],
             [-2, 1, 2]])

    b = np.array([8, -11, -3])

    wider_matrix = get_echelon_form(A,b)
    reduced_matrix = reduced_echelon_form(wider_matrix)
    solution = solve_reduce_matrix(reduced_matrix)
    print("Resolving A: \n", A, "\n to respect b: \n", b, "\n It return the solution: \n", solution)

    ### --------------------   Testing unit - for system solution  ---------------------- ##

    np.testing.assert_equal(solution, np.array([2 ,3,-1]))

