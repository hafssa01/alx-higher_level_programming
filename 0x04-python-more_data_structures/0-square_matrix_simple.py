#!/user/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda sbmt: list(map(lambda el: el**2, sbmt)), matrix))
