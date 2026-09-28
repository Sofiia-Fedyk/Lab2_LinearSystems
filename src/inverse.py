#Софія
import numpy as np


def inverse_matrix(A):
    """A^-1 методом Гаусса: (A|E) -> (E|A^-1)."""
    raise NotImplementedError


def solve_inverse(A, b):
    """Повертає x = A^-1 · b."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_inverse(A, b))  # очікується [5, -10, 3, -5]
