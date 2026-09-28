#Діана
import numpy as np


def zero_diagonal(C, D):
    """x_i(1 - c_ii) = ... -> ділимо рядок на (1 - c_ii), діагональ = 0.
    Повертає (C0, d0)."""
    raise NotImplementedError


def norms(C0):
    """Повертає (n1, n2, n3): max суми рядків, max суми стовпців, евклідова."""
    raise NotImplementedError


def jacobi(C0, d0, eps):
    """Метод простої ітерації. Старт x0 = нулі.
    Повертає (x, history), history = [[k, x1, x2, x3, x4, max_e], ...]
    (для k = 0 max_e = None)."""
    raise NotImplementedError


def seidel(C0, d0, eps):
    """Метод Зейделя. Формат повернення як у jacobi."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import C, D, EPS
    C0, d0 = zero_diagonal(C, D)
    print(norms(C0))
    print(jacobi(C0, d0, EPS)[0])  # ≈ [1.9819, -1.6972, 3.1205, -2.3475]
    print(seidel(C0, d0, EPS)[0])
