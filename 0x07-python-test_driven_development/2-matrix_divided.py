def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (list of lists): Matrix to be divided.
        div (number): Divisor to divide the matrix elements by.
    
    Returns:
        list of lists: New matrix with elements divided by div.
    
    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
