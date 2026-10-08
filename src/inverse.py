#Софія
import numpy as np
from output import print_matrix


def inverse_matrix(A):
    """A^-1 методом Гаусса: (A|E) -> (E|A^-1), з вибором головного елемента у стовпці."""
    n = A.shape[0]
    M = np.hstack([A.astype(float), np.eye(n)])
    for k in range(n):
        p = k + np.argmax(np.abs(M[k:, k]))
        if abs(M[p, k]) < 1e-12:
            raise ValueError("Матриця вироджена: оберненої не існує")
        if p != k:
            M[[k, p]] = M[[p, k]]
        M[k] /= M[k, k]
        for i in range(n):
            if i != k:
                M[i] -= M[i, k] * M[k]
    return M[:, n:]


def solve_inverse(A, b, verbose=False):
    """Повертає x = A^-1 · b."""
    A_inv = inverse_matrix(A.copy())
    if verbose:
        print_matrix(A_inv, "A^-1 =")
    return A_inv @ b


if __name__ == "__main__":
    from data import A, b
    print(solve_inverse(A, b, verbose=True))  # очікується [5, -10, 3, -5]
    print("A @ A^-1 ≈ E:", np.allclose(A @ inverse_matrix(A), np.eye(4)))
