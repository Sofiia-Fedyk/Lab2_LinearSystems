# Вільгельм
import numpy as np


def solve_gauss(A, b, verbose=False):
    """Гаусс з вибором головного елемента у стовпці.
    verbose=True -> друкувати матрицю на кожному кроці (output.print_matrix).
    Повертає x (np.ndarray). A і b не змінювати (працювати з .copy())."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_gauss(A, b, verbose=True))  # очікується [5, -10, 3, -5]
