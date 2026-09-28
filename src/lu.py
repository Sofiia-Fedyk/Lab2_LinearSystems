#Вільгельм
import numpy as np


def lu_decompose(A):
    """Повертає (L, U) за формулами (11) з методички."""
    raise NotImplementedError


def solve_lu(A, b, verbose=False):
    """Ly = b, потім Ux = y. Повертає x (np.ndarray)."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_lu(A, b, verbose=True))  # очікується [5, -10, 3, -5]
