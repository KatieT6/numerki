def gauss_jordan_method(matrix, result):
    num_of_variables = len(result)
    bufor = [0] * num_of_variables

    for i in range(num_of_variables):
        for row in matrix:
            row_copy = [round(x, 8) for x in row]
            if row_copy == [0] * num_of_variables:
                res_copy = [round(w, 8) for w in result]
                if res_copy[matrix.index(row)] == 0.0:
                    return "Układ nieoznaczony"
                else:
                    return "Układ sprzeczny"

        base_max = abs(matrix[i][i])
        max_index = i

        for j in range(num_of_variables - i):
            if abs(matrix[i + j][i]) > base_max:
                base_max = abs(matrix[i + j][i])
                max_index = i + j

        if max_index != i:
            for j in range(num_of_variables):
                bufor[j] = matrix[i][j]
                matrix[i][j] = matrix[max_index][j]
                matrix[max_index][j] = bufor[j]
            tmp = result[max_index]
            result[max_index] = result[i]
            result[i] = tmp

        base = matrix[i][i]
        result[i] /= base
        for j in range(num_of_variables - i):
            matrix[i][i + j] /= base

        for j in range(num_of_variables):
            if j != i:
                num = matrix[j][i]
                result[j] -= result[i] * num

                for k in range(num_of_variables):
                    matrix[j][k] -= matrix[i][k] * num

    # print(f"\nNot rounded values: \n{result} \n")
    result = [round(x, 8) for x in result]
    print("Rounded values: ")
    return result
