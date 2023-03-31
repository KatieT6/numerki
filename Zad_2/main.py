import jordan_method


def read_coefficients(filename):
    # Open the file and read the contents
    with open(filename, 'r') as f:
        contents = f.read()

    # Split the contents into sections, each section represents a system of equations
    sections = contents.split('\n\n')

    # Print the list of available systems and prompt the user to choose one
    print('Available systems:')
    for i, section in enumerate(sections):
        print(f'{i+1}:')
        print(section)
        print('')
    choice = int(input('Choose a system: \n'))

    # Get the coefficients and constants for the chosen system
    coeffs_lines = sections[choice-1].split('\n')
    A = []
    b = []
    for line in coeffs_lines:
        # Split the line into coefficients and constants
        coeffs = line.split('|')[0].split()
        const = float(line.split('|')[1])

        # Append the coefficients and constants to A and b
        A.append([float(c) for c in coeffs])
        b.append(const)

    return A, b


A, b = read_coefficients('data.txt')

print(jordan_method.gauss_jordan_method(A, b))