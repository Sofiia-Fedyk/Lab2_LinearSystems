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

        pivot = Ab[k, k]
        Ab[k] = Ab[k] / pivot

        if verbose:
            print_matrix(Ab, f"Крок {k + 1}: Ділення рядка {k + 1} на головний елемент {pivot}")

        for i in range(k + 1, n):
            Ab[i] = Ab[i] - Ab[i, k] * Ab[k]
            if verbose:
                print_matrix(Ab, f"Крок {k + 1}: Обнулення рядка {i + 1} під головним")

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, n] - np.sum(Ab[i, i+1:n] * x[i+1:n])

    return x


if __name__ == "__main__":
    from data import A, b
    print(solve_gauss(A, b, verbose=True))  # очікується [5, -10, 3, -5]
