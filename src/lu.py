#Вільгельм
import numpy as np

import numpy as np
from output import print_matrix


def leading_minors(A):
    """Обчислює та повертає головні мінори матриці."""
    n = A.shape[0]
    minors = []
    for i in range(1, n + 1):
        # np.linalg.det використовуємо як виняток за умовою
        minor_val = np.linalg.det(A[:i, :i])
        minors.append(np.round(minor_val, 4))
    return minors


def lu_decompose(A):
    """Повертає (L, U) за формулами (11) з методички."""
    raise NotImplementedError


def solve_lu(A, b, verbose=False):
    """Ly = b, потім Ux = y. Повертає x (np.ndarray)."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_lu(A, b, verbose=True))  # очікується [5, -10, 3, -5]
