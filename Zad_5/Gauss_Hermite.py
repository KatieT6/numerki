import numpy as np
from AbstractBaseFunction import AbstractBaseFunction

gauss_hermite_array = np.zeros((4, 5, 2), dtype=float)
gauss_hermite_array[0][0] = [-0.707107, 0.886227]
gauss_hermite_array[0][1] = [0.707107, 0.886227]
gauss_hermite_array[1][0] = [-1.224745, 0.295409]
gauss_hermite_array[1][1] = [0, 1.181636]
gauss_hermite_array[1][2] = [1.224745, 0.295409]
gauss_hermite_array[2][0] = [-1.650680, 0.081313]
gauss_hermite_array[2][1] = [-0.534648, 0.804914]
gauss_hermite_array[2][2] = [0.534648, 0.804914]
gauss_hermite_array[2][3] = [1.650680, 0.081313]
gauss_hermite_array[3][0] = [-2.020183, 0.019953]
gauss_hermite_array[3][1] = [-0.958572, 0.393619]
gauss_hermite_array[3][2] = [0, 0.945309]
gauss_hermite_array[3][3] = [0.958572, 0.393619]
gauss_hermite_array[3][4] = [2.020183, 0.019953]

def gauss_hermite_quadrature(
        nodes: int,
        function: AbstractBaseFunction):
    result = 0

    for i in range(len(gauss_hermite_array[nodes - 2])):
        if gauss_hermite_array[nodes - 2][i][1] != 0:
            result += (gauss_hermite_array[nodes - 2][i][1]
                       * function(gauss_hermite_array[nodes - 2][i][0]))

    return result