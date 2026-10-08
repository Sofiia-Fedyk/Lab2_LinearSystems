#Софія
import numpy as np


def det(M):
    """Власний визначник (через зведення до трикутного вигляду)."""
    raise NotImplementedError


def solve_cramer(A, b):
    """Повертає x (np.ndarray, 4 елементи)."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_cramer(A, b))  # очікується [5, -10, 3, -5]
