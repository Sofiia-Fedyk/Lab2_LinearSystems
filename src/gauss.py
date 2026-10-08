# Вільгельм
import numpy as np
from output import print_matrix


def solve_gauss(A, b, verbose=False):
    A_copy = np.copy(A).astype(float)
    b_copy = np.copy(b).astype(float)

    n = len(b_copy)

    Ab = np.column_stack((A_copy, b_copy))

    if verbose:
        print_matrix(Ab, "Початкова розширена матриця:")

    for k in range(n):
        max_row_index = k + np.argmax(np.abs(Ab[k:n, k]))

        if max_row_index != k:
            Ab[[k, max_row_index]] = Ab[[max_row_index, k]]
            if verbose:
                print_matrix(Ab, f"Крок {k + 1}: Перестановка рядків {k + 1} та {max_row_index + 1}")
    """Гаусс з вибором головного елемента у стовпці.
    verbose=True -> друкувати матрицю на кожному кроці (output.print_matrix).
    Повертає x (np.ndarray). A і b не змінювати (працювати з .copy())."""



if __name__ == "__main__":
    from data import A, b
    print(solve_gauss(A, b, verbose=True))  # очікується [5, -10, 3, -5]
