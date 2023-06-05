from CLI import prompt_main
from Gauss_Hermite import gauss_hermite_quadrature
from hermitePolynomial import approximate, approximate_iterative, approximation_error
from plots import plot_approximation

if __name__ == '__main__':
    check, function, left, right, tmp, nodes = prompt_main()

    app = None
    if check == 2: # iterative
        error = tmp
        app = approximate_iterative(function, nodes, error)
        print('wspolczynniki wielomianu aproksymujacego:', app.approximationCoefficients)
        error = approximation_error(left, right, nodes, function, app)
		# gauss_hermite_quadrature(nodes, lambda x: (app(x) - function(x)) * (app(x) - function(x)))
        print('error:', error)
    else: # degree
        degree = tmp
        app = approximate(function, degree, nodes)
        error = approximation_error(left, right, nodes, function, app)

        print(f'Blad aproksymacji: {error:.5f}')
        print(f'Wspolczynniki wielomianu aproksymacji: ', app.approximationCoefficients)

    plot_approximation(function, app, left, right)
